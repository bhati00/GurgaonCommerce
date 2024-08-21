from users.models import UserProfile
from .serializers import UserProfileSerializer
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from rest_framework import generics
# Create your views here.

    
class DeleteUser(generics.DestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


        
    
   
    
