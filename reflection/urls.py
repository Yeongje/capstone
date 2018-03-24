from django.conf.urls import url
from . import views
from . import views_cbv

app_name = 'reflection'
urlpatterns = [
     url(r'^$', views.reflection_list, name = 'reflection_list'),
     url(r'^(?P<id>\d+)/$', views.reflection_detail, name = 'reflection_detail'),
     url(r'^new/$', views.reflection_new, name ='reflection_new'),
     url(r'^(?P<id>\d+)/edit/$', views.reflection_edit, name = 'reflection_edit'),
     url(r'^cbv/(?P<pk>\d+)/delete/$', views_cbv.reflection_delete, name ='reflection_delete'),
]
