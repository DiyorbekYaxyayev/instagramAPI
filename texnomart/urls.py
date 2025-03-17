from django.urls import path
from texnomart import views

urlpatterns = [
    path('categories/', views.CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', views.CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),

    path('products/', views.ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', views.ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),

    path('products/<int:pk>/comments/', views.CommentList.as_view(), name='comment-list'),
    path('products/<int:pk>/comments/<int:comment_pk>/', views.CommentList.as_view(), name='comment-detail'),
    path('products/<int:pk>/comments/<int:comment_pk>/like/', views.CommentList.as_view(), name='comment-like'),
    path('products/<int:pk>/comments/<int:comment_pk>/dislike/', views.CommentList.as_view(), name='comment-dislike'),
]
