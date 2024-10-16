
from rest_framework.permissions import BasePermission

class SuperuserPermission(BasePermission):
    """Permission class allowing access to superuser users."""

    def has_permission(self, request, view):
        """Check if the user is authenticated and is a superuser."""
        return request.user.is_authenticated and request.user.is_admin