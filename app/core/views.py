# from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,generics, authentication, permissions, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import  UserSerializer,UserLoginSerializer,PostSerializer
from rest_framework.settings import api_settings
from .models import User,Post,Photo
from rest_framework.response import Response
from rest_framework.decorators import api_view

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def list(self,request,username):
        queryset = User.objects.all()
        serializer = self.get_serializer(queryset.filter(username=username), many=True)
        return Response(serializer.data)

class signup(generics.CreateAPIView):
    serializer_class = UserSerializer

class CreateUserViewSet(viewsets.ViewSet):
    def post(self,request):
        queryset = User.objects.create(username = request.data['password'])
        return

class CreateTokenView(ObtainAuthToken):
    serializer_class = UserLoginSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().select_related()
    serializer_class = PostSerializer