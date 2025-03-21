from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # settings ni import qilish

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin paneli
    path('api/', include('instagram.urls')),  # Instagram API marshrutlari
    path('api-auth/', include('rest_framework.urls')),  # DRF login/logout
    path('texnomart/', include('texnomart.urls')),  # Texnomart app marshrutlari
]

if settings.DEBUG:  # DEBUG rejimini tekshirish
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
