from django.conf.urls import url
from . import views
from . import views_cbv

app_name = 'assignment399'
urlpatterns = [
     url(r'^$', views_cbv.assignment399_list, name = 'assignment399_list'),
     url(r'^(?P<id>\d+)/$', views.assignment399_detail, name = 'assignment399_detail'),
     url(r'^new/$', views.assignment399_new, name ='assignment399_new'),
     url(r'^(?P<id>\d+)/edit/$', views.assignment399_edit, name = 'assignment399_edit'),


     url(r'^cbv/(?P<pk>\d+)/delete/$', views_cbv.assignment399_delete, name ='assignment399_delete'),
]
