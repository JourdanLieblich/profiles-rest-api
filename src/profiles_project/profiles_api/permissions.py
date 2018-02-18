from rest_framework import permissions

class PostOwnStatus(permissions.BasePermission):
    """Checks that users are only able to update their own status"""

    def has_object_permission(self, request, view, obj):
        """Check if the user is trying to do what they should"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id;

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
