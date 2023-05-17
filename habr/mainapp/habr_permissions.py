from rest_framework.permissions import IsAdminUser, BasePermission, \
    SAFE_METHODS

from mainapp.models import Author, Moderator


class AdminOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


class IsAuthorExists(BasePermission):
    def has_permission(self, request, view):
        author_exists = False
        if request.user.is_authenticated:
            author_exists = Author.objects.filter(author=request.user).exists()
        return bool(request.method in SAFE_METHODS or
                    author_exists)


class IsAuthor(BasePermission):
    """
    Разрешение:
    Если пользователь является автором данной статьи
    И если запросы SAFE_METHODS (GET или HEAD или OPTIONS).
    """

    def has_object_permission(self, request, view, obj):
        return bool(request.method in SAFE_METHODS or
                    obj.author.author == request.user)


class IsAdminOrModerator(BasePermission):
    """
    Проверка: является ли данный пользователь Модератором
    """

    def has_permission(self, request, view):
        moder_or_admin = False
        if request.user.is_authenticated:
            moder = Moderator.objects.filter(user_moder=request.user).exists()
            moder_or_admin = moder or request.user.is_staff
        return bool(request.method in SAFE_METHODS or moder_or_admin)
