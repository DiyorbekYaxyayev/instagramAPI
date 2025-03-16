# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status
# from texnomart.models import Product
# from texnomart.serializers import ProductModelSerializer
from rest_framework import generics
from texnomart.models import Category, Product
from texnomart.serializers import CategorySerializer, ProductModelSerializer

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
