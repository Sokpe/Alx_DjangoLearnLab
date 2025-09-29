import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.force_authenticate(user=self.user)

    def test_create_book(self):
        # Test creating a book
        url = reverse('book-list')
        data = {'title': 'Test Book', 'author': 'Test Author'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Test Book')
        self.assertEqual(response.data['author'], 'Test Author')

    def test_update_book(self):
        # Test updating a book
        book = Book.objects.create(title='Test Book', author='Test Author')
        url = reverse('book-detail', kwargs={'pk': book.pk})
        data = {'title': 'Updated Test Book', 'author': 'Test Author'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Test Book')
        self.assertEqual(response.data['author'], 'Test Author')

    def test_get_book(self):
        # Test getting a book
        book = Book.objects.create(title='Test Book', author='Test Author')
        url = reverse('book-detail', kwargs={'pk': book.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book')
        self.assertEqual(response.data['author'], 'Test Author')

    def test_unauthenticated_user(self):
        # Test unauthenticated user
        self.client.force_authenticate(user=None)
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
