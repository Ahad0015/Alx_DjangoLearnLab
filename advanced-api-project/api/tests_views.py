from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        # Create some Book instances
        self.book1 = Book.objects.create(title='Book One', author='Author A', publication_year=2000)
        self.book2 = Book.objects.create(title='Book Two', author='Author B', publication_year=2010)
        # Authenticate client for endpoints requiring login
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass')

    def test_list_books(self):
        url = reverse('book-list')  # Make sure your URL name matches
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Expect 2 books

    def test_filter_books_by_author(self):
        url = reverse('book-list') + '?author=Author A'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], 'Author A')

    def test_search_books_by_title(self):
        url = reverse('book-list') + '?search=Book One'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book One')

    def test_order_books_by_publication_year(self):
        url = reverse('book-list') + '?ordering=publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years))

    def test_create_book(self):
        url = reverse('book-list')
        data = {'title': 'New Book', 'author': 'Author C', 'publication_year': 2023}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.get(title='New Book').author, 'Author C')

    def test_update_book(self):
        url = reverse('book-update', args=[self.book1.id])
        data = {'title': 'Updated Book One', 'author': 'Author A', 'publication_year': 2001}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book One')

    def test_delete_book(self):
        url = reverse('book-delete', args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_permissions(self):
        # Logout user to test unauthenticated access
        self.client.logout()
        url = reverse('book-list')
        response = self.client.post(url, {'title': 'Unauthorized Book', 'author': 'X', 'publication_year': 2025})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Or 401 depending on your setup

