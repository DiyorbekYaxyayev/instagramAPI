from django.contrib import admin
from django.urls import path, include
from instagram import views

urlpatterns = [
    path('post-list/', views.PostListOrCreate.as_view(), name='post-list'),
    path('post-list/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
]