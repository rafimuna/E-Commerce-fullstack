# accounts/serializers.py

from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password

# 🔹 রেজিস্ট্রেশন Serializer
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)  # 🔹 পাসওয়ার্ড কনফার্ম

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'password2', 'phone')

    # 🔸 Custom validation to check password match
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn’t match."})
        return attrs

    # 🔸 Save method override করে ইউজার তৈরি
    def create(self, validated_data):
        validated_data.pop('password2')
        user = CustomUser.objects.create_user(**validated_data)  # 🔐 create_user পাসওয়ার্ড হ্যাশ করে
        return user
