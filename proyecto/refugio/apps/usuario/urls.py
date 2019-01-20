from django.conf.urls import url
from apps.usuario.views import RegistroUsuario, UserAPI, Register, ChangePassword
from rest_framework.authtoken import views
urlpatterns = [
    url('registrar', RegistroUsuario.as_view(),name='registrar'),
    url('api', UserAPI.as_view(),name='api'),
    url('register', Register.as_view(),name='register'),
    url('change', ChangePassword.as_view(),name='change_pass'),
    url('login', views.obtain_auth_token,name='login'),
]

