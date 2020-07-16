from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        # SAFE_METHODS = methods that don't change the object itself (like GET)
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id # RETURNS A BOOLEAN BY COMPARISON - if obj.is doesn't equal the request.user.id, returns False

