from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product  # কোন মডেল ব্যবহার হবে
        fields = '__all__'  # সব ফিল্ডকেই সিরিয়ালাইজ করো
