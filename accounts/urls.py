# accounts/urls.py

from django.urls import path
from .views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # 🔹 কাস্টম রেজিস্ট্রেশন API
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # 🔐 JWT Login API
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # ♻️ Token Refresh
]
