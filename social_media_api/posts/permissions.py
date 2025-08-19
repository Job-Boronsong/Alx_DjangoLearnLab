from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    """
    Read for everyone; write only for owner.
    Works for Post.author and Comment.author.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        owner = getattr(obj, "author", None)
        return owner == request.user
