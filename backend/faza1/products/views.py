# from django.shortcuts import get_object_or_404

# from rest_framework.response import Response
# from rest_framework.exceptions import ValidationError
# from rest_framework import status

# from rest_framework.decorators import api_view
# from rest_framework.views import APIView
from rest_framework import generics
# from rest_framework import mixins
# from rest_framework import viewsets

from .models import Product, Category, Brand
from .serializers import ProductSerializer,CategorySerializer,BrandSerializer

class ProductListCV(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailCV(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'

class ProductRUDCV(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'

class ProductCRCV(generics.ListCreateAPIView):
    queryset= Product.objects.all()
    serializer_class=ProductSerializer

class CategoryListCV(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BrandListCV(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class OneCategoryListCV(generics.ListAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Product.objects.filter(category=pk)


class OneBrandListCV(generics.ListAPIView):
    serializer_class = ProductSerializer
   
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Product.objects.filter(brand=pk)
"""
the OneCat and OneBrand classes can be written so that they utilize nested
serialization not sure what is better solution at the momment
"""
    