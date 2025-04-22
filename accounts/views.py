# accounts/views.py

from rest_framework import generics
from .serializers import RegisterSerializer
from .models import CustomUser

# 🔹 রেজিস্টার ভিউ - নতুন ইউজার তৈরি করে
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
