
import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book

class BookAPITestCase(APITestCase):
    def test_create_book(self):
        # Test creating a book
        url = reverse('book-list')
        data = {'title': 'Test Book', 'author': 'Test Author'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book(self):
        # Test updating a book
        book = Book.objects.create(title='Test Book', author='Test Author')
        url = reverse('book-detail', kwargs={'pk': book.pk})
        data = {'title': 'Updated Test Book', 'author': 'Test Author'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        # Test deleting a book
        book = Book.objects.create(title='Test Book', author='Test Author')
        url = reverse('book-detail', kwargs={'pk': book.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
