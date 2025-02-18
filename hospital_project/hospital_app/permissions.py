from rest_framework import permissions

class AllowAllPermissions(permissions.BasePermission):
    """
    Custom permission to grant all authenticated users full access.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return True


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow object owners to edit it, but read-only for others.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions only for the owner
        return hasattr(obj, 'owner') and obj.owner == request.user
