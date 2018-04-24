from django.conf.urls import url
from . import views


app_name = 'ifb'

urlpatterns = [
     url(r'^$', views.first_page, name = 'first_page'),
     url(r'^IFB398/$', views.ifb398_first_page, name = 'ifb398_first_page'),
     url(r'^IFB399/$', views.ifb399_first_page, name = 'ifb399_first_page'),
]
