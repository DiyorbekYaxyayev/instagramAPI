from django.core.cache import cache
from rest_framework import generics
from texnomart.models import Category, Product, Comment
from texnomart.serializers import CategorySerializer, ProductModelSerializer, CommentSerializer
from rest_framework.response import Response
import datetime

# Category CRUD
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.prefetch_related('product_set').all()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        cache_key = "categories"
        data = cache.get(cache_key)
        if not data:
            response = super().list(request, *args, **kwargs)
            cache.set(cache_key, response.data, timeout=60*15)  # 15 daqiqa cache
            return response
        return Response(data)

    def perform_create(self, serializer):
        serializer.save()
        cache.delete("categories")  # Yangi kategoriya qo'shilganda cache ni o'chirish


class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.prefetch_related('product_set').all()
    serializer_class = CategorySerializer

    def perform_update(self, serializer):
        serializer.save()
        cache.delete("categories")

    def perform_destroy(self, instance):
        instance.delete()
        cache.delete("categories")


# Product CRUD
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.select_related('category').prefetch_related('comment_set').all()
    serializer_class = ProductModelSerializer

    def list(self, request, *args, **kwargs):
        cache_key = "products"
        data = cache.get(cache_key)
        if not data:
            response = super().list(request, *args, **kwargs)
            cache.set(cache_key, response.data, timeout=60*15)
            return response
        return Response(data)

    def perform_create(self, serializer):
        serializer.save()
        cache.delete("products")


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.select_related('category').prefetch_related('comment_set').all()
    serializer_class = ProductModelSerializer

    def perform_update(self, serializer):
        serializer.save()
        cache.delete("products")

    def perform_destroy(self, instance):
        instance.delete()
        cache.delete("products")


# Comment CRUD
class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.select_related('post').all()
    serializer_class = CommentSerializer
    filterset_fields = ('post',)

    def get_queryset(self):
        return super().get_queryset().order_by('-created_at')

    def list(self, request, *args, **kwargs):
        cache_key = "comments"
        data = cache.get(cache_key)
        if not data:
            response = super().list(request, *args, **kwargs)
            cache.set(cache_key, response.data, timeout=60*15)
            return response
        return Response(data)

    def perform_create(self, serializer):
        serializer.save()
        cache.delete("comments")


class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.select_related('post').all()
    serializer_class = CommentSerializer
    lookup_field = 'id'
    filterset_fields = ('post',)
    ordering = ('-created_at',)

    def perform_update(self, serializer):
        serializer.save(updated_at=datetime.datetime.now())
        cache.delete("comments")

    def perform_destroy(self, instance):
        instance.delete()
        cache.delete("comments")
