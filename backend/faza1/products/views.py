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
    
    # def perform_create(self, serializer):
    #     category_name = self.request.data.get('category')
    #     category = Category.objects.get(name=category_name)
    #     serializer.save(category=category)

class CategoryListCV(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

        
class BrandListCV(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class OneCategoryListCV(generics.ListAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        pk = self.kwargs['slug']
        pkr = Category.objects.get(slug=pk).name
        return Product.objects.filter(category=pkr)


class OneBrandListCV(generics.ListAPIView):
    serializer_class = ProductSerializer
   
    def get_queryset(self):
        pk = self.kwargs['slug']
        pkr = Brand.objects.get(slug=pk).name
        return Product.objects.filter(brand=pkr)
"""
the OneCat and OneBrand classes can be written so that they utilize nested
serialization not sure what is better solution at the momment
"""
    