from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from instagram import views  # Instagram app ichidagi views ni import qilamiz
from instagram.views import jwt_login_view, jwt_logout_view  # To‘g‘ri import

router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='post')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post-list/', views.PostListOrCreate.as_view(), name='post-list'),
    path('post-list/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
    path('', include(router.urls)),
    path('api/jwt/login/', jwt_login_view, name='jwt_login'),
    path('api/jwt/logout/', jwt_logout_view, name='jwt_logout'),
]
