from rest_framework import mixins, viewsets
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer, UserCustomSerializers, UserSerializers
from .models import User
from rest_framework import generics
from django.contrib.auth.models import User


class UserViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def get_serializer_class(self):
        if self.request.version == 'v1':
            return UserCustomSerializers
        return UserSerializers
