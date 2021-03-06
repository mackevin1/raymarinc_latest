from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from bns.models import Project
from django.conf.urls import url, include
from django.contrib.sitemaps.views import sitemap
from django.conf.urls.static import static
from django.conf import settings

from bns import views as bns_views
from accounts import views as accounts_views
from boards import views
info_dict = {
    'queryset': Project.objects.all(),
}

urlpatterns = [
    url(r'^$', views.BoardListView.as_view(), name='home'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    #url(r'^bns/', include('bns.urls')),

    url(r'^reset/$',
        auth_views.PasswordResetView.as_view(
            template_name='password_reset.html',
            email_template_name='password_reset_email.html',
            subject_template_name='password_reset_subject.txt'
        ),
        name='password_reset'),
    url(r'^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),

    url(r'^settings/account/$', accounts_views.UserUpdateView.as_view(), name='my_account'),
    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change'),
    url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        name='password_change_done'),

    url(r'^boards/(?P<pk>\d+)/$', views.TopicListView.as_view(), name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', views.PostListView.as_view(), name='topic_posts'),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$', views.reply_topic, name='reply_topic'),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/posts/(?P<post_pk>\d+)/edit/$',
        views.PostUpdateView.as_view(), name='edit_post'),
    url(r'^admin/', admin.site.urls),
    #url(r'^bns/project/(?P<project_pk>\d+)/$', views.ProjectListView.as_view(template_name='project_detail.html'), info_dict),
    #url(r'^work/(?P<slug>\d+)/$', views.ProjectListView.as_view(template_name='showcase/project_detail.html'), info_dict),
    url(r'^work/bns/(?P<project_pk>\d+)/$', views.ProjectListView.as_view(template_name='project_object.html'), info_dict),
    url(r'^work/bns/$', views.ProjectListView.as_view(template_name='project_detail.html'), info_dict),
    url(r'^work/$', views.ProjectListView.as_view(template_name='project_detail.html'), info_dict, name='bns'),
    #url(r'^work/bns/(?P<product_pk>\d+)/$', views.ProjectListView.as_view(template_name='project_detail.html'), name='project'),
    #url(r'^bns/$', views.ProjectListView.as_view(template_name='product.html'), name='product'),
    #('pages/', include('django.contrib.flatpages.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
