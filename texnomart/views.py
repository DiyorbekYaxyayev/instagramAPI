from rest_framework import generics
from texnomart.models import Category, Product, Comment
from texnomart.serializers import CategorySerializer, ProductModelSerializer, CommentSerializer
from rest_framework import status
from rest_framework.response import Response
import datetime

# Category CRUD
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.prefetch_related('product_set').all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.prefetch_related('product_set').all()
    serializer_class = CategorySerializer


# Product CRUD
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.select_related('category').prefetch_related('comment_set').all()
    serializer_class = ProductModelSerializer


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.select_related('category').prefetch_related('comment_set').all()
    serializer_class = ProductModelSerializer


# Comment CRUD
class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.select_related('post').all()
    serializer_class = CommentSerializer
    filterset_fields = ('post',)

    def get_queryset(self):
        return super().get_queryset().order_by('-created_at')


class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.select_related('post').all()
    serializer_class = CommentSerializer
    lookup_field = 'id'
    filterset_fields = ('post',)
    ordering = ('-created_at',)

    def perform_update(self, serializer):
        serializer.save(updated_at=datetime.datetime.now())
