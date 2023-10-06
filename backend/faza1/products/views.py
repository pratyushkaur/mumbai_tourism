from django.shortcuts import get_object_or_404

from rest_framework.response import Response
# from rest_framework.exceptions import ValidationError
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics
# from rest_framework import mixins
# from rest_framework import viewsets
import json
from rest_framework.permissions import IsAuthenticated

from .models import (Product,
                     Category,
                     Brand,
                     Customer,
                     Complaint,
                     Cart,
                     Incart,
                    )
from .serializers import (ProductSerializer,
                          CategorySerializer,
                          BrandSerializer,
                          ReviewSerializer,
                          CustomerSerializer,
                          ComplaintSerializer,
                          )

class ProductListCV(generics.ListAPIView): #not needed with ProductPriceFilterCV
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

class ProductFilterCV(generics.ListAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
            queryset = Product.objects.all()
            low = int(self.request.query_params.get('low'))
            high = int(self.request.query_params.get('high'))
            ordered = self.request.query_params.get('ordered')
            queryset = queryset.filter(price__gt=low, price__lt=high).order_by(ordered)
            return queryset
class ProductSearchCV(generics.ListAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        searched = self.request.query_params.get('searched')
        queryset= Product.objects.filter(title__icontains=str(searched))
        return queryset

class ReviewCreateCV(generics.CreateAPIView):
    serializer_class = ReviewSerializer

@api_view(['POST'])
def signupFV(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
    else:
        return Response(serializer.errors, status=status.HTTP_200_OK)




class ProfileAV(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        customer = Customer.objects.get(username=request.user.username)
        serializer = CustomerSerializer(customer)
        print(serializer.data)
        return Response(serializer.data)

    # def post(self, request):
    #     serializer = StreamPlatformSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors)

class ComplaintCV(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer
    
    # def get_serializer_context(self):
    #     context = super().get_serializer_context()
    #     context['request'] = self.request
    #     return context
    
    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

class AddToCartAV(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            data = json.loads(request.body)
            # Assuming data is a list of dictionaries containing item_id and item_amount.
            for item_data in data:
                item_id = item_data.get("item_id")
                item_amount = item_data.get("item_ammount")

                # Retrieve the product and cart instances.
                product = get_object_or_404(Product, id=item_id)
                cart= Cart.objects.get(customer=request.user)

                # Create or update the entry in Incart.
                incart = Incart.objects.create(
                    cart=cart, product=product, amount=item_amount)
                print(incart.amount)
                print(item_amount)
                # incart.amount = item_amount  # Set the amount field explicitly
                # incart.save()

            return Response({"message": "Products added to cart successfully."})
        except Exception as e:
            return Response({"error": str(e)}, status=400)
