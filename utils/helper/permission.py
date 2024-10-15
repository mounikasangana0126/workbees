from rest_framework import permissions
from rest_framework.authentication import BasicAuthentication

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self,request,views,obj):
        return str(obj.employee_id)==str(request.user)