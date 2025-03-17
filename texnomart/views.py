# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status
# from texnomart.models import Product
# from texnomart.serializers import ProductModelSerializer
from rest_framework import generics
from texnomart.models import Category, Product, Comment
from texnomart.serializers import CategorySerializer, ProductModelSerializer
from rest_framework import status
from rest_framework.response import Response
from texnomart.serializers import CategorySerializer, ProductModelSerializer, CommentSerializer
import datetime
# class CategoryList(APIView):
#     ...
#
#
# class ProductList(APIView):
#     def get(self, request, format=None):
#         products = Product.objects.all()
#         serializer = ProductModelSerializer(products, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)



# Category CRUD
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Product CRUD
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer

# class CommentView(generics.CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductModelSerializer
#     comment_model = Comment
#     comment_field = 'comments'
#     comment_create_field = 'text'
#     ordering = ('-created_at',)

class CommentCreateModel(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    comment_model = Comment

    def post(self, request, pk):
        product = self.get_object()
        serializer = self.serializer_class(product)
        comment = Comment(post=product, **request.data)
        comment.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filterset_fields = ('post',)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-created_at')



class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'
    filterset_fields = ('post',)
    ordering = ('-created_at',)
    def perform_update(self, serializer):
        serializer.save(updated_at=datetime.now())

