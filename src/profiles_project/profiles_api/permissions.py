from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile. """

    def has_object_permission(self, request, view, obj):
         """Check user is trying to edit their own profile."""

         if request.method in permissions.SAFE_METHODS:
              return True
         
         return obj.id == request.user.id
    

class PostOwnStatus(permissions.BasePermission):
    """Allow users to modify only their own feed items."""

    def has_object_permission(self, request, view, obj):
        # SAFE methods are always allowed
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write operations only allowed on owner's status
        return obj.user_profile.id == request.user.id