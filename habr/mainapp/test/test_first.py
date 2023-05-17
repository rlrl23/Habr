import json
from django.test import TestCase
from rest_framework.authtoken.models import Token
# from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.test import (APIRequestFactory, force_authenticate,
                                 APIClient, APISimpleTestCase,
                                 APITestCase)
# from mixer.backend.django import mixer
from django.contrib.auth.models import User
# from .views import AuthorViewSet
# from .models import Author, Book
from mainapp.models import Category, Article, Author, Comment, Like, Moderator


# from mainapp.views import (ArticleViewSet, CategoryViewSet,
#                            ModeratorViewSet, AuthorViewSet,
#                            CommentViewSet, LikeViewSet)


class TestIndexAPI(TestCase):
    def test_get_index_api(self):
        # http://127.0.0.0:8000/
        client = APIClient()
        response = client.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         msg='TestIndex: NOT OK!!!')


class TestCategoryAPI(APITestCase):

    def setUp(self) -> None:
        Category.objects.create(name='Develop', slug='develop')
        Category.objects.create(name='Design', slug='design')

    def test_get_list_categories(self):
        # http://127.0.0.0:8000/categories/
        # category = Category.objects.create(name='Develop', slug='develop')
        # category = Category.objects.create(name='Design', slug='design')
        client = APIClient()
        response = client.get('/categories/')
        # print('category:response:', response)
        # print('category:response.data:', response.data)
        # for cat in response.data:
        #     print(dict(cat))
        # print('category:len(response.data):', len(response.data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_category(self):
        # http://127.0.0.0:8000/categories/1/
        # category = Category.objects.create(name='Develop', slug='develop')
        client = APIClient()
        response = client.get('/categories/1/')
        # print('category1:response:', response)
        # print('category1:response.data:', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data,
                         {'url': 'http://testserver/categories/1/',
                          'name': 'Develop',
                          'slug': 'develop'},
                         # {'id': 1, 'name': 'Develop', 'slug': 'develop'}
                         )


class TestUserAPI(APITestCase):

    def setUp(self) -> None:
        User.objects.create_user(username='user1',
                                 email='test@mail.ru',
                                 password='super7Pas')
        User.objects.create_user(username='user2',
                                 email='test2@mail.ru',
                                 password='super72Pas')

    def test_get_list_users(self):
        # http://127.0.0.0:8000/users/

        client = APIClient()
        response = client.get('/users/')
        # print('users:response:', response)
        # print('\nusers:response.data:', response.data)
        # print('users:len(response.data):', len(response.data))
        # for usr_i in response.data:
        #     print('\nusers:usr_i', usr_i)
        #     print('\nusers:usr_i', dict(usr_i))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_user1(self):
        # http://127.0.0.0:8000/users/1/

        client = APIClient()
        response = client.get('/users/1/')
        # print('user1:response:', response)
        # print('user1:response.data:', response.data)
        # print('user1:response.data[username]:', response.data['username'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data,
                         {'id': 1, 'url': 'http://testserver/users/1/',
                          'username': 'user1'}
                         )
        self.assertEqual(response.data['username'], 'user1')

    def test_get_user2(self):
        # http://127.0.0.0:8000/users/2/

        client = APIClient()
        response = client.get('/users/2/')
        # print('user2:response:', response)
        # print('user2:response.data:', response.data)
        # print('user2:response.data[username]:', response.data['username'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data,
                         {'id': 2,
                          'url': 'http://testserver/users/2/',
                          'username': 'user2'})
        self.assertEqual(response.data['username'], 'user2')

    def test_get_user3(self):
        # http://127.0.0.0:8000/users/3/

        client = APIClient()
        response = client.get('/users/3/')
        # print('user3:response:', response)
        # print('user3:response.data:', response.data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class TestUserPermissionsAPI(APITestCase):

    # @classmethod
    # def setUpTestData(cls):
    #     pass

    def setUp(self) -> None:
        User.objects.create_superuser(username='admin1',
                                      email='admin@test.ru',
                                      password='aDmin1234')
        User.objects.create_user(username='user1',
                                 email='test@mail.ru',
                                 password='super7Pas')
        User.objects.create_user(username='user2',
                                 email='test2@mail.ru',
                                 password='super72Pas')

    def test_get_list_users(self):
        # http://127.0.0.0:8000/users/
        self.client.login(username='admin1', password='aDmin1234')
        # print('client.login - admin')
        # self.client.force_login(username='admin', password='aDmin1234')

        client = APIClient()
        response = client.get('/users/')
        # print('users:response:', response)
        # print('\nusers:response.data:', response.data)
        # print('users:len(response.data):', len(response.data))
        # for usr_i in response.data:
        #     print('\nusers:usr_i', usr_i)
        #     print('\nusers:usr_i', dict(usr_i))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(len(response.data), 3)

    def test_get_user1(self):
        # http://127.0.0.0:8000/users/1/
        # user_admin = User.objects.get(pk=1)
        # user_admin = User.objects.create_superuser(username='admin',
        #                                            email='admin@test.ru',
        #                                            password='aDmin1234')
        # User.objects.create_user(username='user1',
        #                          email='test@mail.ru',
        #                          password='super7Pas')
        # User.objects.create_user(username='user2',
        #                          email='test2@mail.ru',
        #                          password='super72Pas')
        # m_user = User.objects.get(pk=1)
        # print('m_user', m_user)
        # # token = Token.objects.get(user__username='admin1')
        # token = Token.objects.get(m_user)
        # user_admin = self
        # print('\n160.user_admin:', user_admin)
        # self.client.force_login(user=user_admin)

        client = APIClient()
        auth = client.post('/api-token-auth/',
                           {"username": "admin1",
                            "password": "aDmin1234"},
                           format='json')
        token = auth.data['token']
        client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        response = client.get('/users/1/')
        # print('user1:response:', response)
        # print('user1:response.data:', response.data)
        # print('user1:response.data[username]:', response.data['username'])
        # print('user1:response.data[is_staff]:', response.data['is_staff'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data,
        #                  {'id': 1, 'url': 'http://testserver/users/1/',
        #                   'username': 'admin1'})
        self.assertEqual(response.data['username'], 'admin1')
        self.assertEqual(response.data['email'], 'admin@test.ru')

    def test_get_user2(self):
        # http://127.0.0.0:8000/users//

        client = APIClient()
        auth = client.post('/api-token-auth/',
                           {"username": "user1",
                            "password": "super7Pas"},
                           format='json')
        token = auth.data['token']
        client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        response = client.get('/users/2/')
        # print('user1:response:', response)
        # print('user1:response.data:', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'user1')
        self.assertEqual(response.data['email'], 'test@mail.ru')

    # =====================================================================
    def test_get_user23(self):
        # http://127.0.0.0:8000/users//

        client = APIClient()
        auth = client.post('/api-token-auth/',
                           {"username": "user1",
                            "password": "super7Pas"},
                           format='json')
        token = auth.data['token']
        client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        response = client.get('/users/3/')
        # print('user23:response:', response)
        # print('user23:response.data:', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data['username'], 'user1')
        # self.assertEqual(response.data['email'], 'test@mail.ru')
    # =====================================================================

    # def test_get_user2(self):
    #     # http://127.0.0.0:8000/users/2/
    #
    #     client = APIClient()
    #     response = client.get('/users/2/')
    #     # print('user2:response:', response)
    #     # print('user2:response.data:', response.data)
    #     # print('user2:response.data[username]:', response.data['username'])
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data,
    #                      {'id': 2, 'url': 'http://testserver/users/2/',
    #                       'username': 'user1'})
    #     self.assertEqual(response.data['username'], 'user1')

    # def test_get_user77(self):
    #     # http://127.0.0.0:8000/users/77/
    #
    #     client = APIClient()
    #     response = client.get('/users/77/',
    #                           headers={'Authorization': 'Token 123'})
    #     # print('user77:response:', response)
    #     # print('user77:response.data:', response.data)
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    #     # self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TestUserPermissions2API(APITestCase):

    # @classmethod
    # def setUpTestData(cls):
    #     pass

    def setUp(self) -> None:
        User.objects.create_superuser(username='admin1',
                                      email='admin@test.ru',
                                      password='aDmin1234')
        User.objects.create_user(username='user1',
                                 email='test@mail.ru',
                                 password='super7Pas')
        User.objects.create_user(username='user2',
                                 email='test2@mail.ru',
                                 password='super72Pas')

    def test_get_user12(self):
        # http://127.0.0.0:8000/users/3/

        client = APIClient()
        auth = client.post('/api-token-auth/',
                           {"username": "admin1",
                            "password": "aDmin1234"},
                           format='json')
        token = auth.data['token']
        # print('token', token)
        client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        response = client.get('/users/2/')
        # print('user12:response:', response)
        # print('user12:response.data:', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data['username'], 'user1')
        # self.assertEqual(response.data['email'], 'test@mail.ru')

    # =====================================================================

    def test_get_user22(self):
        # http://127.0.0.0:8000/users/3/

        client = APIClient()
        auth = client.post('/api-token-auth/',
                           {"username": "user1",
                            "password": "super7Pas"},
                           format='json')
        token = auth.data['token']
        # print('token', token)
        client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        response = client.get('/users/2/')
        # print('user22:response:', response)
        # print('user22:response.data:', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data['username'], 'user1')
        # self.assertEqual(response.data['email'], 'test@mail.ru')

    # =====================================================================

    def test_get_user23(self):
        # http://127.0.0.0:8000/users/3/

        client = APIClient()
        auth = client.post('/api-token-auth/',
                           {"username": "user1",
                            "password": "super7Pas"},
                           format='json')
        token = auth.data['token']
        # print('token', token)
        client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        response = client.get('/users/3/')
        # print('user23:response:', response)
        # print('user23:response.data:', response.data)
        user_data = {'id': 3, 'url': 'http://testserver/users/3/',
                     'username': 'user2'}
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data['username'], 'user1')
        # self.assertEqual(response.data['email'], 'test@mail.ru')
        self.assertEqual(response.data, user_data)

    # =====================================================================


class TestArticleAPI(APITestCase):

    def setUp(self) -> None:
        User.objects.create_superuser(username='admin1',
                                      email='admin@test.ru',
                                      password='aDmin1234')
        user_id_2 = User.objects.create_user(username='user1',
                                             email='test@mail.ru',
                                             password='super7Pas')
        User.objects.create_user(username='user2',
                                 email='test2@mail.ru',
                                 password='super72Pas')
        category1 = Category.objects.create(name='Develop', slug='develop')
        category2 = Category.objects.create(name='Design', slug='design')
        author1 = Author.objects.create(author=User.objects.get(pk=1))
        author2 = Author.objects.create(author=user_id_2)
        # Article.objects.create(category=1,
        Article.objects.create(
            title='Title of First Article. cat: Develop',
            short_description='Shot description 1',
            full_description='Article Text - full_description',
            author=author1,
            # author=Author.objects.get(pk=1),
            # author=Author.objects.get(pk=2),
            # category=Category.objects.get(pk=1)
            category=category1
        )
        # author=1)
        # Article.objects.create(
        #     title='Title of Second Article. cat: Develop',
        #     short_description='Shot description 2',
        #     full_description='Article 1 Text - full_description',
        #     author=2
        # )
        # # author=2)

    def test_list_articles(self):
        # print('\nArticle.objects.all()', Article.objects.all())
        client = APIClient()
        response = client.get('/articles/')
        # print('\narticles:response:', response)
        # print('\narticles:response.data:', response.data)
        # print('\narticles:response.status_code:', response.status_code)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_article(self):
        client = APIClient()
        response = client.get('/articles/1/')
        # print('\narticle1:response:', response)
        # print('\narticle1:response.data:', response.data)
        # print('\narticle1: len(response.data):', len(response.data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['short_description'],
                         'Shot description 1')


class TestArticlePermissionAPI(APITestCase):

    def setUp(self) -> None:
        User.objects.create_superuser(username='admin1',
                                      email='admin@test.ru',
                                      password='aDmin1234')
        user_id_2 = User.objects.create_user(username='user1',
                                             email='test@mail.ru',
                                             password='super7Pas')
        User.objects.create_user(username='user2',
                                 email='test2@mail.ru',
                                 password='super72Pas')
        # Category.objects.create(name='Develop', slug='develop')
        # Category.objects.create(name='Design', slug='design')
        category1 = Category.objects.create(name='Develop', slug='develop')
        category2 = Category.objects.create(name='Design', slug='design')
        Author.objects.create(author=User.objects.get(pk=1))
        # author1 = Author.objects.create(author=User.objects.get(pk=2))
        author1 = Author.objects.create(author=user_id_2)
        # Article.objects.create(category=1,
        Article.objects.create(
            category=category1,
            title='Title of First Article. cat: Develop',
            short_description='Shot description 1',
            full_description='Article Text - full_description',
            author=author1,
            is_published=True,
            is_deleted=False,
            is_approved=True
            # author=Author.objects.get(pk=1),
            # author=Author.objects.get(pk=2),
        )

    def test_get_articles(self):
        client = APIClient()
        response = client.get('/articles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_article_fail(self):
        # print('Article.objects.all()', Article.objects.all())
        # print('Article.objects.all()[0]', Article.objects.all()[0])
        # print('Article.objects.all()[0]', Article.objects.all()[0].id)
        # print('Article.objects.all()[0]', Article.objects.all()[0].category)
        # print('Article.objects.all()[0]', Article.objects.all()[0].title)
        client = APIClient()
        test_article = {'category': '/categories/1/',
                        'title': 'Test Article',
                        'short_description': 'Test Article. short description',
                        'full_description': 'Test Article. full description'}
        response = client.post('/articles/', data=test_article, format='json')
        # print('test_create_article:response:', response)
        # print('test_create_article:response.data:', response.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_article(self):
        client = APIClient()
        # response = client.get('/authors/')
        auth = client.post('/api-token-auth/',
                           {"username": "user1",
                            "password": "super7Pas"},
                           format='json')
        token = auth.data['token']
        # print('token', token)
        client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        # response = client.get('/users/3/')
        test_article = {'category': '/categories/1/',
                        'title': 'Test Article',
                        'short_description': 'Test Article. short description',
                        'full_description': 'Test Article. full description'}
        response = client.post('/articles/', data=test_article, format='json')
        # print('test_create_article:response:', response)
        # print('test_create_article:response.data:', response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['short_description'],
                         'Test Article. short description')

    def test_patch_article(self):
        client = APIClient()
        # response = client.get('/authors/')
        auth = client.post('/api-token-auth/',
                           {"username": "user1",
                            "password": "super7Pas"},
                           format='json')
        token = auth.data['token']
        # print('token', token)
        client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        # response = client.get('/users/3/')
        # 'short_description', 'Shot description 1')
        # test_article = {'category': '/categories/1/',
        #                 'title': 'Test Article',
        #                 'short_description': 'Test Article. short description',
        #                 'full_description': 'Test Article. full description'}
        update_article = {'short_description': 'Updated Shot description 1'}
        response = client.patch('/articles/1/',
                                data=update_article,
                                format='json')
        # response = client.put('/articles/1/',
        #                       data=update_article,
        #                       format='json')
        # response = client.get('/articles/')
        # response = client.get('/authors/2/')
        # print('test_create_article:response:', response)
        # print('test_create_article:response.data:', response.data)
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(5, 5)
        self.assertEqual(response.data['short_description'],
                         'Updated Shot description 1')

    def test_put_article(self):
        client = APIClient()
        auth = client.post('/api-token-auth/',
                           {"username": "user1",
                            "password": "super7Pas"},
                           format='json')
        token = auth.data['token']
        # print('token', token)
        client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        update_article = {
            'category': '/categories/2/',
            'title': 'Updated Title of First Article.',
            'short_description': 'Updated Shot description',
            'full_description': 'Updated Article full_description'
        }
        response = client.put('/articles/1/',
                              data=update_article,
                              format='json')
        # print('test_create_article:response:', response)
        # print('test_create_article:response.data:', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['short_description'],
                         'Updated Shot description')

    def test_put_article_fail(self):
        client = APIClient()
        auth = client.post('/api-token-auth/',
                           {"username": "user2",
                            "password": "super72Pas"},
                           format='json')
        token = auth.data['token']
        # print('token', token)
        client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        update_article = {
            'category': '/categories/2/',
            'title': 'Updated Title of First Article.',
            'short_description': 'Updated Shot description',
            'full_description': 'Updated Article full_description'
        }
        response = client.put('/articles/1/',
                              data=update_article,
                              format='json')
        # print('test_create_article:response:', response)
        # print('test_create_article:response.data:', response.data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_patch_article_fail(self):
        client = APIClient()
        auth = client.post('/api-token-auth/',
                           {"username": "user2",
                            "password": "super72Pas"},
                           format='json')
        token = auth.data['token']
        # print('token', token)
        client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        update_article = {'short_description': 'Updated Shot description 1'}
        response = client.patch('/articles/1/',
                                data=update_article,
                                format='json')
        # print('test_create_article:response:', response)
        # print('test_create_article:response.data:', response.data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TestAuthorAPI(APITestCase):
    def setUp(self) -> None:
        User.objects.create_superuser(username='admin1',
                                      email='admin@test.ru',
                                      is_staff=True,
                                      is_superuser=True,
                                      password='aDmin1234')
        User.objects.create_user(username='user1',
                                 email='test@mail.ru',
                                 password='super7Pas')
        User.objects.create_user(username='user2',
                                 email='test2@mail.ru',
                                 password='super72Pas')
        User.objects.create_user(username='user3',
                                 email='test3@mail.ru',
                                 password='super72Pas')
        # Author.objects.create(author=User.objects.get(pk=1))
        Author.objects.create(author=User.objects.get(pk=2))
        Moderator.objects.create(
            user_moder=User.objects.get(username='user2')
        )

    def test_list_author(self):
        client = APIClient()
        response = client.get('/authors/')
        # # print('Author.objects.all()', Author.objects.all())
        # # print('Author.objects.all()', Author.objects.all())
        # # Author.objects.create(author=1)
        # print(response.data)
        # print(response.data[0])
        # print(response.data[1])
        # print('*' * 5)
        # # print(dict(response.data))
        # # print([i for i in response.data])
        # # [print(*i) for i in response.data]
        # [print(dict(i)) for i in response.data]
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_one_author(self):
        client = APIClient()
        response = client.get('/authors/1/')
        # response = client.get('/authors/2/')
        # print('response.data', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'id': 1, 'author': 2})

    def test_admin_create_author(self):
        client = APIClient()
        auth = client.post('/api-token-auth/',
                           {"username": "admin1",
                            "password": "aDmin1234"},
                           format='json')
        token = auth.data['token']
        client.credentials(HTTP_AUTHORIZATION=f'Token {token}')

        test_author = {'author': '/users/4/'}
        response = client.post('/authors/', data=test_author, format='json')
        # print('response.data', response.data)
        # print('test: authors:', Author.objects.all())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['author'],
                         'http://testserver/users/4/')

    def test_moder_create_author(self):
        # # print('test: moders:', Moderator.objects.all())
        # t_users = User.objects.all()
        # print('test: users:', t_users)
        # # test: users: <QuerySet [<User: admin1>, <User: user1>, <User: user2>, <User: user3>]>
        # print('test: user1:', t_users.get(pk=1))
        # # test: user1: admin1
        # print('test: user2:', t_users.get(pk=2))
        # # test: user2: user1
        # print('test: user3:', t_users.get(pk=3))
        # # test: user3: user2
        # print('test: user4:', t_users.get(pk=4))
        # # test: user4: user3

        client = APIClient()
        auth = client.post('/api-token-auth/',
                           {"username": "user2",
                            "password": "super72Pas"},
                           format='json')
        token = auth.data['token']
        client.credentials(HTTP_AUTHORIZATION=f'Token {token}')

        test_author = {'author': '/users/4/'}
        response = client.post('/authors/', data=test_author, format='json')
        # print('response.data', response.data)
        # print('test: authors:', Author.objects.all())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # print([i for i in response.data])
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['author'],
                         'http://testserver/users/4/')

    def test_user_create_author_fail(self):
        # print('test before: authors:', Author.objects.all())
        # print('test: moders:', Moderator.objects.all())
        client = APIClient()
        # auth = client.post('/api-token-auth/',
        #                    {"username": "user2",
        #                     "password": "super72Pas"},
        #                    format='json')
        # token = auth.data['token']
        # client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        # test_author = {'author': '/users/3/'}
        test_author = {'author': '/users/4/'}
        response = client.post('/authors/', data=test_author, format='json')
        # response = client.get('/authors/')
        # response = client.get('/authors/3/')
        # print([i for i in response.data])
        # print('response.data', response.data)
        # print('test: authors:', Author.objects.all())
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
