from django.conf.urls import url
from .views import Index, Detail, CategoryView, TagView, AboutMe

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^about/$', AboutMe.as_view(), name='about'),
    url(r'^article/(?P<article_id>\d+)$', Detail.as_view(), name='detail'),
    url(r'^category/(?P<cate_id>\d+)$', CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<tag_id>\d+)$', TagView.as_view(), name='tag'),
    # url(r'^archive/(?P<year>\d+)/(?P<month>\d+)$', views.ArchiveView.as_view(), name='archive'),
    # url(r'^me', views.me, name='me'),
]