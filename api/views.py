import logging

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes, authentication_classes

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import AccessToken

from django.shortcuts import render

from tasks.models import Task
from users.models import CustomUser

from .serializers import (
    RegisterSerializer,
    ChangePasswordSerializer,
    TaskSerializer,
)

logger = logging.getLogger(__name__)


class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    queryset = queryset.order_by("name")
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)


class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)


class TaskUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)


class TaskDeleteView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    authentication_classes = []
    permission_classes = [permissions.AllowAny]


class ChangePasswordView(APIView):
    """
    An endpoint for changing password.
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, queryset=None):
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            old_password = serializer.data.get("old_password")
            new_password1 = serializer.data.get("new_password1")
            new_password2 = serializer.data.get("new_password2")
            if not self.object.check_password(old_password):
                message = "A senha atual está inválida."
                return Response(message, status=status.HTTP_400_BAD_REQUEST)

            if old_password:
                if old_password == new_password1:
                    message = "A nova senha deve ser diferente da atual."
                    return Response(message, status=status.HTTP_400_BAD_REQUEST)

            if new_password1 and new_password2:
                if new_password1 != new_password2:
                    message = "A nova senha deve ser igual à sua confirmação."
                    return Response(message, status=status.HTTP_400_BAD_REQUEST)

            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password1"))
            self.object.force_password_change = False
            self.object.save()
            message = "A senha foi alterada com sucesso!"
            return Response(message, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
