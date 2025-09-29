import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

    def test_create_book(self):
        # Test creating a book
        url = reverse('book-list')
        data = {'title': 'Test Book', 'author': 'Test Author'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Test Book')
        self.assertEqual(response.data['author'], 'Test Author')

    # Other tests...


Alternatively, you can use self.client.force_authenticate if you're using token-based authentication:

def setUp(self):
    self.user = User.objects.create_user(username='testuser', password='password')
    self.client.force_authenticate(user=self.user)
