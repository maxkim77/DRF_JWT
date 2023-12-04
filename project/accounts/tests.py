from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model

class SignupTestCase(APITestCase):
    def test_signup(self):
        data = {
            'email': 'test@example.com',
            'password1': 'somepassword',
            'password2': 'somepassword',
        }
        response = self.client.post(reverse('rest_register'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # 추가적인 검증이 필요할 수 있습니다.

class LoginTestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(email='test@example.com', password='somepassword')

    def test_login(self):
        data = {
            'email': 'test@example.com',
            'password': 'somepassword',
        }
        response = self.client.post(reverse('rest_login'), data)  # URL 이름 수정
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class LogoutTestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(email='test@example.com', password='somepassword')
        # 로그인 후 토큰 획득
        response = self.client.post(reverse('dj_rest_auth:login'), {'email': 'test@example.com', 'password': 'somepassword'})
        self.refresh_token = response.data['refresh_token']

    def test_logout(self):
        response = self.client.post(reverse('rest_logout'), {'refresh': self.refresh_token})  # URL 이름 수정
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class MyPageTestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(email='test@example.com', password='somepassword')
        # 로그인 요청 후 토큰을 얻는다면 이를 사용
        response = self.client.post(reverse('dj_rest_auth:login'), {'email': 'test@example.com', 'password': 'somepassword'})
        self.token = response.data['access_token']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_mypage(self):
        response = self.client.get(reverse('mypage'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'test@example.com')