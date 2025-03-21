from rest_framework import serializers
from texnomart.models import Product, Category, Comment, Image


# Image serializer
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


# Comment serializer
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


# Category serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# Product serializer
class ProductModelSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title', read_only=True)  # ForeignKey bo‘lgani uchun
    images = ImageSerializer(many=True, read_only=True)  # Related images
    comments = CommentSerializer(many=True, read_only=True)  # Related comments

    class Meta:
        model = Product
        fields = '__all__'
