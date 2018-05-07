from django.conf.urls import url
from . import views
from . import views_cbv

app_name = 'project'
urlpatterns = [
     url(r'^$', views_cbv.post_list, name = 'post_list'),
     #url(r'^$', views.post_list, name = 'post_list'),

     url(r'^(?P<id>\d+)/$', views.post_detail, name = 'post_detail'),
     url(r'^new/$', views.post_new, name ='post_new'),
     url(r'^(?P<id>\d+)/edit/$', views.post_edit, name = 'post_edit'),

     url(r'^cbv/(?P<pk>\d+)/delete/$', views_cbv.post_delete, name ='post_delete'),

     url(r'^post/(?P<pk>[0-9]+)/commentnew/$', views.comment_new, name ='comment_new'),
     url(r'^comments/$', views.comment_list, name='comment_list'),

     #url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),

     url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
     url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
]
