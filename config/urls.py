from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin paneli
    path('api/', include('instagram.urls')),  # Instagram API marshrutlari
    path('api-auth/', include('rest_framework.urls')),  # DRF login/logout
    path('texnomart/', include('texnomart.urls')),  # Texnomart app marshrutlari
]
