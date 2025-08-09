from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="password123")

        # Create a sample book
        self.book = Book.objects.create(
            title="Sample Book",
            author="John Doe",
            publication_year=2020
        )

        # Endpoints
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', args=[self.book.id])
        self.create_url = reverse('book-create')
        self.update_url = reverse('book-update', args=[self.book.id])
        self.delete_url = reverse('book-delete', args=[self.book.id])

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Sample Book", str(response.data))

    def test_retrieve_single_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Sample Book")

    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="password123")
        data = {"title": "New Book", "author": "Jane Doe", "publication_year": 2023}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        data = {"title": "Unauthorized Book", "author": "No Auth", "publication_year": 2023}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        self.client.login(username="testuser", password="password123")
        data = {"title": "Updated Book", "author": "John Doe", "publication_year": 2021}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_update_book_unauthenticated(self):
        data = {"title": "Hack Update", "author": "John Doe", "publication_year": 2021}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_book_authenticated(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_delete_book_unauthenticated(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_search_books(self):
        response = self.client.get(self.list_url, {"search": "Sample"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Sample Book", str(response.data))

    def test_order_books(self):
        Book.objects.create(title="A Book", author="Another Author", publication_year=2019)
        response = self.client.get(self.list_url, {"ordering": "title"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [book['title'] for book in response.data]
        self.assertEqual(titles, sorted(titles))
