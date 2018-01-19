from django.conf.urls import url
from . import views
from . import views_cbv

app_name = 'assignment'
urlpatterns = [
     url(r'^$', views_cbv.assignment_list, name = 'assignment_list'),
     url(r'^(?P<id>\d+)/$', views.assignment_detail, name = 'assignment_detail'),
     url(r'^new/$', views.assignment_new, name ='assignment_new'),
     url(r'^(?P<id>\d+)/edit/$', views.assignment_edit, name = 'assignment_edit'),


     url(r'^cbv/(?P<pk>\d+)/delete/$', views_cbv.assignment_delete, name ='assignment_delete'),
]
