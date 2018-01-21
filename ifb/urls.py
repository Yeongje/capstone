from django.conf.urls import url
from . import views


app_name = 'ifb'

urlpatterns = [
     url(r'^$', views.first_page, name = 'first_page'),
]
