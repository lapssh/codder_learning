import unittest

from django.test import TestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from users.models import User


class LoginAuth(APITestCase):

    def test_create_user(self):
        self.first_name = "John"
        self.last_name = "Connor"
        self.email = "john_connor@skynet.ru"
        self.password = "P@ssw0rd9"
        self.company = "SkyNet"
        self.position = "destroyer"
        self.user = User.objects.create_user(email=self.email, password=self.password)
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.assertEqual(str(type(self.token)), f"<class 'rest_framework.authtoken.models.Token'>")


class TestGetUrl(TestCase):

    def test_get_200_ok(self):
        resp = self.client.get('/api/v1/shops/')
        self.assertEqual(resp.status_code, 200)

        resp = self.client.get('/api/v1/categories/')
        self.assertEqual(resp.status_code, 200)

        resp = self.client.get('/api/v1/products?shop_id=1&category_id=2')
        self.assertEqual(resp.status_code, 200)

    def test_get_301(self):
        resp = self.client.get('/api/v1/shops')
        self.assertEqual(resp.status_code, 301)

        resp = self.client.get('/api/v1/categories')
        self.assertEqual(resp.status_code, 301)


if __name__ == '__main__':
    unittest.main()
