from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Проверяет авторство для записи
    и метод запроса."""

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
