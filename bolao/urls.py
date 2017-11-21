from django.conf.urls import url, include
from .import views
from django.contrib.auth.views import (
    login, logout, password_reset, password_reset_done, password_reset_confirm,
    password_reset_complete
)

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', login, {'template_name': 'login.html'}),
    url(r'^logout/$', logout, {'template_name': 'logout.html'}),
    url(r'^register/$', views.register, name='register'),
    url(r'^listajogos/$', views.listajogos, name='listajogos'),
    url(r'^times/$', views.times, name='times'),
    url(r'^apostas/$', views.apostar, name='apostar'),
    url(r'^apostas/(?P<partida>\w+)/$', views.apostar, name='apostar'),
    url(r'^lista_apostas/(?P<partida>\w+)/$', views.listaposta),
    url(r'^perfil/$', views.view_perfil, name='view_perfil'),
    url(r'^perfil/editar/$', views.editar_perfil, name='editar_perfil'),
    url(r'^minhas_apostas/$', views.minhas_apostas, name='minhas_apostas'),
    url(r'^mudar-senha/$', views.mudar_senha, name='mudar_senha'),
    url(r'^reset-senha/$', password_reset, name='reset_password'),
    url(r'^reset-senha/resetada/$', password_reset_done, name='password_reset_done'),
    url(r'^reset-senha/confirma/$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset-senha/confirma/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
    password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset-senha/complete/$', password_reset_complete, name='password_reset_complete'),
]

# python -m smtpd -n -c DebuggingServer localhost:1025  MANDAR EMAIL PARA RESETAR SENHA
