import json
from django.test import TestCase
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.test import (APIRequestFactory, force_authenticate,
                                 APIClient, APISimpleTestCase,
                                 APITestCase)
# from mixer.backend.django import mixer
from django.contrib.auth.models import User
from mainapp.models import Category, Article, Author, Comment, Like, Moderator


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
        client = APIClient()
        response = client.get('/categories/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_category(self):
        # http://127.0.0.0:8000/categories/1/
        client = APIClient()
        response = client.get('/categories/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data,
                         {'url': 'http://testserver/categories/1/',
                          'name': 'Develop',
                          'slug': 'develop'},
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
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_user1(self):
        # http://127.0.0.0:8000/users/1/

        client = APIClient()
        response = client.get('/users/1/')
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
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class TestUserPermissionsAPI(APITestCase):

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

        client = APIClient()
        response = client.get('/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user1(self):
        # http://127.0.0.0:8000/users/1/

        client = APIClient()
        auth = client.post('/api-token-auth/',
                           {"username": "admin1",
                            "password": "aDmin1234"},
                           format='json')
        token = auth.data['token']
        client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        response = client.get('/users/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
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
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestUserPermissions2API(APITestCase):

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
        client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        response = client.get('/users/2/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # =====================================================================

    def test_get_user22(self):
        # http://127.0.0.0:8000/users/3/

        client = APIClient()
        auth = client.post('/api-token-auth/',
                           {"username": "user1",
                            "password": "super7Pas"},
                           format='json')
        token = auth.data['token']
        client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        response = client.get('/users/2/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # =====================================================================

    def test_get_user23(self):
        # http://127.0.0.0:8000/users/3/

        client = APIClient()
        auth = client.post('/api-token-auth/',
                           {"username": "user1",
                            "password": "super7Pas"},
                           format='json')
        token = auth.data['token']
        client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        response = client.get('/users/3/')
        user_data = {'id': 3, 'url': 'http://testserver/users/3/',
                     'username': 'user2'}
        self.assertEqual(response.status_code, status.HTTP_200_OK)
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
        Article.objects.create(
            title='Title of First Article. cat: Develop',
            short_description='Shot description 1',
            full_description='Article Text - full_description',
            author=author1,
            category=category1
        )

    def test_list_articles(self):
        client = APIClient()
        response = client.get('/articles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_article(self):
        client = APIClient()
        response = client.get('/articles/1/')
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
        category1 = Category.objects.create(name='Develop', slug='develop')
        category2 = Category.objects.create(name='Design', slug='design')
        Author.objects.create(author=User.objects.get(pk=1))
        author1 = Author.objects.create(author=user_id_2)
        Article.objects.create(
            category=category1,
            title='Title of First Article. cat: Develop',
            short_description='Shot description 1',
            full_description='Article Text - full_description',
            author=author1,
            is_published=True,
            is_deleted=False,
            is_approved=True
        )

    def test_get_articles(self):
        client = APIClient()
        response = client.get('/articles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_article_fail(self):
        client = APIClient()
        test_article = {'category': '/categories/1/',
                        'title': 'Test Article',
                        'short_description': 'Test Article. short description',
                        'full_description': 'Test Article. full description'}
        response = client.post('/articles/', data=test_article, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_article(self):
        client = APIClient()
        auth = client.post('/api-token-auth/',
                           {"username": "user1",
                            "password": "super7Pas"},
                           format='json')
        token = auth.data['token']
        client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        test_article = {'category': '/categories/1/',
                        'title': 'Test Article',
                        'short_description': 'Test Article. short description',
                        'full_description': 'Test Article. full description'}
        response = client.post('/articles/', data=test_article, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['short_description'],
                         'Test Article. short description')

    def test_patch_article(self):
        client = APIClient()
        auth = client.post('/api-token-auth/',
                           {"username": "user1",
                            "password": "super7Pas"},
                           format='json')
        token = auth.data['token']
        client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        update_article = {'short_description': 'Updated Shot description 1'}
        response = client.patch('/articles/1/',
                                data=update_article,
                                format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['short_description'],
                         'Updated Shot description 1')

    def test_put_article(self):
        client = APIClient()
        auth = client.post('/api-token-auth/',
                           {"username": "user1",
                            "password": "super7Pas"},
                           format='json')
        token = auth.data['token']
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
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_patch_article_fail(self):
        client = APIClient()
        auth = client.post('/api-token-auth/',
                           {"username": "user2",
                            "password": "super72Pas"},
                           format='json')
        token = auth.data['token']
        client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        update_article = {'short_description': 'Updated Shot description 1'}
        response = client.patch('/articles/1/',
                                data=update_article,
                                format='json')
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
        Author.objects.create(author=User.objects.get(pk=2))
        Moderator.objects.create(
            user_moder=User.objects.get(username='user2')
        )

    def test_list_author(self):
        client = APIClient()
        response = client.get('/authors/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_one_author(self):
        client = APIClient()
        response = client.get('/authors/1/')
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
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['author'],
                         'http://testserver/users/4/')

    def test_moder_create_author(self):

        client = APIClient()
        auth = client.post('/api-token-auth/',
                           {"username": "user2",
                            "password": "super72Pas"},
                           format='json')
        token = auth.data['token']
        client.credentials(HTTP_AUTHORIZATION=f'Token {token}')

        test_author = {'author': '/users/4/'}
        response = client.post('/authors/', data=test_author, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['author'],
                         'http://testserver/users/4/')

    def test_user_create_author_fail(self):
        client = APIClient()
        test_author = {'author': '/users/4/'}
        response = client.post('/authors/', data=test_author, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
