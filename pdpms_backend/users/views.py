from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        current_password = request.data.get('current_password')
        new_password = request.data.get('user_password')

        # Only check password if user_password is being changed
        if new_password:
            if not current_password or current_password != instance.user_password:
                return Response({'detail': 'Current password is incorrect.'}, status=status.HTTP_400_BAD_REQUEST)
        
        return super().update(request, *args, **kwargs)