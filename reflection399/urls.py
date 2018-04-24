from django.conf.urls import url
from . import views


app_name = 'reflection399'
urlpatterns = [
     url(r'^$', views.reflection399_list, name = 'reflection399_list'),
     url(r'^(?P<id>\d+)/$', views.reflection399_detail, name = 'reflection399_detail'),
     url(r'^new/$', views.reflection399_new, name ='reflection399_new'),
     url(r'^(?P<id>\d+)/edit/$', views.reflection399_edit, name = 'reflection399_edit'),
     url(r'^cbv/(?P<pk>\d+)/delete/$', views.reflection399_delete, name ='reflection399_delete'),
]
