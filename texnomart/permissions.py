from rest_framework.permissions import BasePermission
from datetime import datetime, timedelta

class GetOrPostPermissions(BasePermission):
    def has_permission(self, request, view):
        return request.method in ['GET', 'POST']

class UpdateTimeLimit(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (datetime.now() - obj.created_at) < timedelta(minutes=2)
