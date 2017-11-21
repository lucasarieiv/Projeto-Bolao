from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from copa import views


urlpatterns = [
    url(r'^$', views.login_redirect, name='login_redirect'),
    url(r'^$', include('django.contrib.auth.urls')),
    url(r'^accounts/login/$', auth_views.LoginView.as_view(template_name='bolao/login.html')),
    url(r'^admin/', admin.site.urls),
    url(r'^bolao/', include('bolao.urls', namespace='bolao')),
]
