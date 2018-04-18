from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import UpdateView, ListView
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.urls import reverse

#from .forms import NewTopicForm, PostForm
from .models import Project, ProjectType, Client, ProjectImage, Role


class BnsListView(ListView):
    model = Bns
    context_object_name = 'bns'
    template_name = 'bns.html'


class ProductsbnsListView(ListView):
    model = Productsbns
    context_object_name = 'productbns'
    template_name = 'productsbns.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        kwargs['board'] = self.board
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.board = get_object_or_404(Board, pk=self.kwargs.get('pk'))
        queryset = self.bns.productsbns.order_by('-last_updated').annotate(replies=Count('posts') - 1)
        return queryset




@login_required
def reply_topic(request, pk, topic_pk):
    topic = get_object_or_404(Topic, bns__pk=pk, pk=productbns_pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()

            topic.last_updated = timezone.now()
            topic.save()

            topic_url = reverse('productbns_posts', kwargs={'pk': pk, 'productbns_pk': productbns_pk})
            topic_post_url = '{url}?page={page}#{id}'.format(
                url=topic_url,
                id=bns.pk,
                page=productbns.get_page_count()
            )

            return redirect(topic_post_url)
    else:
        form = PostForm()
    return render(request, 'reply_topic.html', {'topic': topic, 'form': form})
