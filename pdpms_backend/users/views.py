from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
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
    
    @api_view(['POST'])
    def change_password(request):
        username = request.data.get('username')
        current_password = request.data.get('current_password')
        new_password = request.data.get('new_password')
        if not username or not current_password or not new_password:
            return Response({'detail': 'Missing fields.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(username=username)
            if user.user_password != current_password:
                return Response({'detail': 'Current password is incorrect.'}, status=status.HTTP_400_BAD_REQUEST)
            user.user_password = new_password
            user.save()
            return Response({'detail': 'Password changed successfully.'})
        except User.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)