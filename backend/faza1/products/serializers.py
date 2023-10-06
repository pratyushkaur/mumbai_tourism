from rest_framework import serializers
from .models import (Product, 
                    Brand, 
                    Category, 
                    Review, 
                    Customer,
                    Complaint,
                    Incart
                    )
from django.contrib.auth.hashers import make_password


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     try:
    #         representation['brand'] = instance.brand.name
    #         representation['category'] = instance.category.name
    #     except:
    #         representation['brand'] = None
    #         representation['category'] = None
    #     return representation

class BrandSerializer(serializers.ModelSerializer):
    # prod_brand = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Brand
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    # prod_cat = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields =  '__all__'
    
class ReviewSerializer(serializers.ModelSerializer):
    # customer_name = serializers.StringRelatedField(read_only=True)
    # product_name =serializers.StringRelatedField(read_only=True)
   
    # class Meta:
    #     model = Review
    #     fields = '__all__'
        
    # def get_customer_name(self,obj):
    #     return obj.customer.name
    pass

class CustomerSerializer(serializers.ModelSerializer):
    def validate_password(self, value: str) -> str: 
        return make_password(value)
    class Meta:
        model = Customer
        fields = '__all__'

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = ['title', 'content','customer']
    # def create(self, validated_data):
    #     request = self.context.get('request')
    #     customer = request.user
    #     validated_data['customer'] = customer
    #     return super().create(validated_data)

class IncartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incart
        fields = ('id', 'product', 'amount')