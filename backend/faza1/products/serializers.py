from rest_framework import serializers
from .models import Product, Brand, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    # prod_brand = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Brand
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    # prod_cat = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'
        