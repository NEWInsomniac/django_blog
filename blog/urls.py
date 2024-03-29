from django.conf.urls import url
from . import views
app_name = 'blog'

urlpatterns = [
                # url(r'^$', views.index, name='index'),
                # url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
                # url(r'^category/(?P<pk>\d+)/$', views.category, name='category'),
                url(r'^$', views.IndexView.as_view(), name='index'),
                url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
                url(r'^category/(?P<pk>\d+)/$', views.CategoryView.as_view(), name='category'),
                url(r'^tag/(?P<pk>\d+)/$', views.TagView.as_view(), name='tag'),
                url(r'^post/(?P<pk>\d+)/$', views.detail, name='detail'),

                ]