from rest_framework import serializers
from .models import Product, Brand, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        try:
            representation['brand'] = instance.brand.name
            representation['category'] = instance.category.name
        except:
            representation['brand'] = None
            representation['category'] = None
        return representation

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
        