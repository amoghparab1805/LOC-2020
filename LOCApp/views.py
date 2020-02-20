from django.shortcuts import render
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.generics import CreateAPIView
from . serializers import UserSerializer
from . models import User

@permission_classes((permissions.AllowAny, ))
class CreateUserView(CreateAPIView):
    model = User
    serializer_class = UserSerializer