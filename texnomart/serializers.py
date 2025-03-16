from rest_framework import serializers
from texnomart.models import Product, Image, Category

class ImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        exclude = ('id', 'product')

class ProductModelSerializer(serializers.ModelSerializer):
    images = ImageModelSerializer(many=True, read_only=True)
    category = serializers.CharField(source='category.title', read_only=True)
    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
