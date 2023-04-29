import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
# from mixer.backend.django import mixer
from django.contrib.auth.models import User
# from .views import AuthorViewSet
# from .models import Author, Book
from mainapp.models import Category, Article, Author, Comment, Like, Moderator
from mainapp.views import ArticleViewSet, CategoryViewSet, ModeratorViewSet, AuthorViewSet, CommentViewSet, LikeViewSet


class TestIndexAPI(TestCase):
    def test_get_index_api(self):
        client = APIClient()
        response = client.get('/')
        # self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST,
        #                  msg='TestIndex: NOT OK!!!')
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         msg='TestIndex: NOT OK!!!')
        # self.assertEqual(response, status.HTTP_400_BAD_REQUEST,
        #                  msg=f'response={response.path_info}')
        # pass

    def test_get_list_categories(self):
        # http://127.0.0.0:8000/categories/
        article = Category.objects.create(name='Develop', slug='develop')
        client = APIClient()
        response = client.get('/categories/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

