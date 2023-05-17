from rest_framework.permissions import IsAdminUser, BasePermission, \
    SAFE_METHODS

from mainapp.models import Author, Moderator


# django.contrib.auth.password_validation.UserAttributeSimilarityValidator
# from django.contrib.auth.password_validation import UserAttributeSimilarityValidator


class AdminOnly(BasePermission):
    def has_permission(self, request, view):
        # return bool(request.user and request.user.is_staff)
        return request.user.is_superuser


class IsAuthorExists(BasePermission):
    def has_permission(self, request, view):
        # print()
        author_exists = False
        if request.user.is_authenticated:
            author_exists = Author.objects.filter(author=request.user).exists()
            # print("!!! perm: IsAuthorExists", f'{request.user = }',
            #       author_exists, type(author_exists))
        return bool(request.method in SAFE_METHODS or
                    author_exists)
        # return x


class IsAuthor(BasePermission):
    """
    Разрешение:
    Если пользователь является автором данной статьи
    И если запросы SAFE_METHODS (GET или HEAD или OPTIONS).
    """

    def has_object_permission(self, request, view, obj):
        # print('\nperm.request.user', request.user)
        # # perm.request.user user1
        # print('perm.view', view)
        # # perm.view <mainapp.views.ArticleViewSet object at 0x7f707b232dd0>
        # print('perm.view.action', view.action)
        # print('perm.view.__dir__', view.__dir__())
        # print('perm.obj', obj, '\n', '*' * 15)
        # # perm.obj Заголовок моей первой статьи
        # #  ***************
        # print('perm: type(obj)', type(obj), '\n', '*' * 15)
        # # perm: type(obj) <class 'mainapp.models.Article'>
        # #  ***************
        # print('perm: obj.__dir__', obj.__dir__(), '\n', '*' * 15)

        # perm: obj.__dir__ ['_state', 'id', 'category_id', 'title', 'short_description', 'full_description', 'author_id', 'created_at', 'updated_at', 'is_published', 'is_deleted', 'is_approved', '__module__', '__str__', '__doc__', '_meta', 'DoesNotExist', 'MultipleObjectsReturned', 'category', 'author', 'get_next_by_created_at', 'get_previous_by_created_at', 'get_next_by_updated_at', 'get_previous_by_updated_at', 'objects', 'article', 'like_set', '__init__', 'from_db', '__repr__', '__eq__', '__hash__', '__reduce__', '__getstate__', '__setstate__', '_get_pk_val', '_set_pk_val', 'pk', 'get_deferred_fields', 'refresh_from_db', 'arefresh_from_db', 'serializable_value', 'save', 'asave', 'save_base', '_save_parents', '_save_table', '_do_update', '_do_insert', '_prepare_related_fields_for_save', 'delete', 'adelete', '_get_FIELD_display', '_get_next_or_previous_by_FIELD', '_get_next_or_previous_in_order', '_get_field_value_map', 'prepare_database_save', 'clean', 'validate_unique', '_get_unique_checks', '_perform_unique_checks', '_perform_date_checks', 'date_error_message', 'unique_error_message', 'get_constraints', 'validate_constraints', 'full_clean', 'clean_fields', 'check', '_check_default_pk', '_check_db_table_comment', '_check_swappable', '_check_model', '_check_managers', '_check_fields', '_check_m2m_through_same_relationship', '_check_id_field', '_check_field_name_clashes', '_check_column_name_clashes', '_check_model_name_db_lookup_clashes', '_check_property_name_related_field_accessor_clashes', '_check_single_primary_key', '_check_index_together', '_check_unique_together', '_check_indexes', '_check_local_fields', '_check_ordering', '_check_long_column_names', '_get_expr_references', '_check_constraints', '__init_subclass__', '__dict__', '__weakref__', '__new__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__ne__', '__gt__', '__ge__', '__reduce_ex__', '__subclasshook__', '__format__', '__sizeof__', '__dir__', '__class__']

        #  ***************

        # print('perm: obj.author_id', obj.author_id, '\n', '*' * 15)
        # # perm: obj.author_id 1
        # #  ***************
        # print('!!! perm: type(obj.author_id)', type(obj.author_id), '\n', '*' * 15)
        # # !!! perm: type(obj.author_id) <class 'int'>
        #  ***************

        # print('perm: obj.author', obj.author, '\n', '*' * 15)
        # # perm: obj.author admin
        # #  ***************
        # print('perm: type(obj.author)', type(obj.author), '\n', '*' * 15)
        # # perm: type(obj.author) <class 'mainapp.models.Author'>
        #  ***************

        # print('perm: obj.author.__dir__', obj.author.__dir__(), '\n', '*' * 15)
        # print('perm: type(obj.author.author)', type(obj.author.author), '\n', '*' * 15)
        # print('perm: obj.author.author.__dir__', obj.author.author.__dir__(), '\n', '*' * 15)

        # # request.user == obj.author
        # print('perm: request.user == obj.author:',
        #       request.user == obj.author, '\n', '*' * 15)
        # # perm: request.user == obj.author: False
        #  ***************

        # request.user == obj.author.author
        # print('perm: request.user == obj.author.author:',
        #       request.user == obj.author.author, '\n', '*' * 15)
        # perm: request.user == obj.author.author: True
        #  ***************

        # return bool(request.method in SAFE_METHODS or
        #             obj.author == request.user)
        return bool(request.method in SAFE_METHODS or
                    obj.author.author == request.user)


class IsAdminOrModerator(BasePermission):
    """
    Проверка: является ли данный пользователь Модератором
    """

    def has_permission(self, request, view):
        moder_or_admin = False
        if request.user.is_authenticated:
            # print('request.user:', request.user)
            moder = Moderator.objects.filter(user_moder=request.user).exists()
            moder_or_admin = moder or request.user.is_staff
            # print('IsAdminOrModerator:')
            # print('moder:', moder)
            # print('moder_or_admin:', moder_or_admin)
            # print('request.user.is_staff:', request.user.is_staff)
        # return bool(request.user and request.user.is_staff)
        # print('boooooool:',
        #       bool(request.method in SAFE_METHODS or moder_or_admin))
        # return True
        return bool(request.method in SAFE_METHODS or moder_or_admin)

    # def has_object_permission(self, request, view, obj):
    #     zm = IsAdminUser
    #     moder = Moderator.objects.filter(user_moder=request.user).exists()
    #     # print('\nIsModerator')
    #     # print('request.user', request.user)
    #     # print('obj.author', obj.author)
    #     # print('IsModerator\n')
    #     return obj.author == request.user

# class IsModeratorCategory(BasePermission):
#     """
#     Проверка: является ли данный пользователь Модератором данной Категории
#     """
#     def has_permission(self, request, view):
#         # return bool(request.user and request.user.is_staff)
#         return request.user.is_superuser
#
#     def has_object_permission(self, request, view, obj):
#         # return (
#         #     self.op1.has_object_permission(request, view, obj) and
#         #     self.op2.has_object_permission(request, view, obj)
#         # )
#         return request.user in obj.moderators
