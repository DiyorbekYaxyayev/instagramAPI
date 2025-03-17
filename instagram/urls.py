from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from instagram import views

# DRF router yaratamiz va PostViewSet ni ro‘yxatdan o‘tkazamiz
router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='post')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post-list/', views.PostListOrCreate.as_view(), name='post-list'),
    path('post-list/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
    path('', include(router.urls)),  # Routerdagi URL-larni qo‘shamiz
]
