from rest_framework import serializers
from .models import ProductDetail


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = ['id', 'name', 'description', 'price', 'created_at']
