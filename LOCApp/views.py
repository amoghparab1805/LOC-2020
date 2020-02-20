from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from . serializers import UserSerializer
from . models import User

class CreateUserView(CreateAPIView):
    model = User
    serializer_class = UserSerializer