from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import UpdateView, ListView
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.urls import reverse

from .models import Board, Category, ProductImages
from bns.models import Project

class BoardListView(ListView):
    model = Board
    context_object_name = 'boards'
    template_name = 'home.html'


class CategoryListView(ListView):
    model = Category
    context_object_name = 'categorys'
    template_name = 'home.html'
    paginate_by = 20

class ProductImagesListView(ListView):
    model = ProductImages
    context_object_name = 'productimages'
    template_name = 'home.html'
    paginate_by = 20


    def get_context_data(self, **kwargs):
        kwargs['board'] = self.board
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.board = get_object_or_404(Board, pk=self.kwargs.get('pk'))
        queryset = self.board.topics.order_by('-last_updated').annotate(replies=Count('posts') - 1)
        return queryset

    def get_context_data(self, **kwargs):
        kwargs['products'] = self.products
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.board = get_object_or_404(Products, pk=self.kwargs.get('pk'))
        queryset = self.products.order_by('-last_updated').annotate(replies=Count('posts') - 1)
        return queryset


@login_required
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = request.user
            topic.save()
            Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=request.user
            )
            return redirect('topic_posts', pk=pk, topic_pk=topic.pk)
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})


@login_required
def reply_topic(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()

            topic.last_updated = timezone.now()
            topic.save()

            topic_url = reverse('topic_posts', kwargs={'pk': pk, 'topic_pk': topic_pk})
            topic_post_url = '{url}?page={page}#{id}'.format(
                url=topic_url,
                id=post.pk,
                page=topic.get_page_count()
            )

            return redirect(topic_post_url)
    else:
        form = PostForm()
    return render(request, 'reply_topic.html', {'topic': topic, 'form': form})



class ProjectListView(ListView):
    model = Project
    context_object_name = 'Project'
    template_name = 'project.html'

def get_queryset(self):
    self.project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
    queryset = self.project.order_by('-last_updated')
    return queryset
