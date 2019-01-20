from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from apps.usuario.forms import RegistroForm
from rest_framework import views, generics, permissions
from apps.usuario.serializers import UserSerializer
import json
from django.http import HttpResponse
from rest_framework.authtoken.models import Token
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.response import Response
# Create your views here.
class RegistroUsuario(CreateView):
    model = User
    template_name = "usuario/register.html"
    form_class =  RegistroForm
    success_url = reverse_lazy('mascota_listar')


class UserAPI(views.APIView):
    serializer = UserSerializer
    def get(self,request,format=None):
        lista = User.objects.all()
        response = self.serializer(lista, many=True)
        return HttpResponse(json.dumps(response.data), content_type='application/json')


class Register(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username,email,password)
        user.save()

        token = Token.objects.create(user = user)
        return Response()

class ChangePassword(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, username=request.user)
        user.set_password(request.POST.get('new_password'))
        user.save()
        return HttpResponse({"Contraseña cambiada"})
