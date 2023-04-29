from rest_framework.permissions import IsAdminUser, BasePermission, SAFE_METHODS
# django.contrib.auth.password_validation.UserAttributeSimilarityValidator
# from django.contrib.auth.password_validation import UserAttributeSimilarityValidator

class AdminOnly(BasePermission):
    def has_permission(self, request, view):
        # return bool(request.user and request.user.is_staff)
        return request.user.is_superuser


class IsAuthor(BasePermission):
    """
    Разрешение:
    Если пользователь является автором данной статьи
    И если запросы SAFE_METHODS (GET или HEAD или OPTIONS).
    """
    def has_object_permission(self, request, view, obj):
        print('request.user', request.user)
        return bool(request.method in SAFE_METHODS or
                    obj.author == request.user)


class IsModerator(BasePermission):
    """
    Проверка: является ли данный пользователь Модератором
    """

    def has_object_permission(self, request, view, obj):
        print('\nIsModerator')
        print('request.user', request.user)
        print('obj.author', obj.author)
        print('IsModerator\n')
        return obj.author == request.user


class IsModeratorCategory(BasePermission):
    """
    Проверка: является ли данный пользователь Модератором данной Категории
    """
    def has_permission(self, request, view):
        # return bool(request.user and request.user.is_staff)
        return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        # return (
        #     self.op1.has_object_permission(request, view, obj) and
        #     self.op2.has_object_permission(request, view, obj)
        # )
        return request.user in obj.moderators


