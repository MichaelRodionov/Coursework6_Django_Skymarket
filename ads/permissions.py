from rest_framework import permissions

from users.models import User


# ----------------------------------------------------------------
# This class defines user's permissions or user's role to edit instances
class IsUsersOrUserAdmin(permissions.BasePermission):
    message: str = 'You are not allowed to edit or delete this instance'

    def has_object_permission(self, request, view, obj) -> bool:
        return obj.author.id == request.user.id or request.user.role == User.Roles.ADMIN



