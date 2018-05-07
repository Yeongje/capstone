
from django.conf.urls import include, url
from . import views, views_team
from django.contrib.auth import views as auth_views
from django.conf import settings



urlpatterns = [
    url(r'^social/signup/$',views.socialsignup, name ='social_signup'),
    url(r'^signup/$',views.signup, name ='signup'),
    #url(r'^login/$', auth_views.login, name='login', kwargs={
    #    'authentication_form': LoginForm,
    #    'template_name': 'accounts/login_form.html', }),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout', kwargs={'next_page': settings.LOGIN_URL}),
    url(r'^profile/$',views.profile, name ='profile'),
    url(r'^profile/update/$', views.update_profile, name='update'),

    url(r'^students/$',views_team.students, name ='students'),
    url(r'^team_navi/$',views_team.team_navi, name ='team_navi'),
    url(r'^students/teams/(?P<team_number>.+)/$',views_team.teams, name ='teams'),

    url(r'^teams/list/$', views_team.team_list, name = 'team_list'),

    #url(r'^$', home, name='home'),
    #socialauth
#    url('', include('social_django.urls', namespace='social')),
]
