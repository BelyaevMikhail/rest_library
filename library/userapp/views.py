from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerialaizer
from .models import User


class userviewSet(ModelViewSet):
    serializer_class = UserSerialaizer
    queryset = User.objects.all()

# Create your views here.
