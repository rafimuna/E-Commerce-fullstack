# accounts/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

# 🔵 কাস্টম ইউজার মডেল বানানো হয়েছে যাতে আমরা ভবিষ্যতে extra ফিল্ড দিতে পারি
class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)  # 🔹 অ্যাডমিন চেক
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username

