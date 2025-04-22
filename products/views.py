from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()  # সব প্রোডাক্ট দেখাবে
    serializer_class = ProductSerializer  # কোন serializer ব্যবহার হবে
    permission_classes = [IsAdminOrReadOnly]  # পারমিশন চেক করবে

    # শুধু অ্যাডমিন create/update/delete করতে পারবে
