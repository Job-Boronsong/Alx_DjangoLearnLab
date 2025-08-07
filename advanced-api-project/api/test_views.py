from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client = APIClient()
        self.author = Author.objects.create(name="Chinua Achebe")
        self.book1 = Book.objects.create(title="Things Fall Apart", publication_year=1958, author=self.author)
        self.book2 = Book.objects.create(title="No Longer at Ease", publication_year=1960, author=self.author)
        self.book_url = reverse('book-list-create')  # from api/urls.py
        self.book_detail_url = lambda pk: reverse('book-detail', kwargs={'pk': pk})

    def test_list_books(self):
        response = self.client.get(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='testpass123')
        data = {
            "title": "Arrow of God",
            "publication_year": 1964,
            "author": self.author.id
        }
        response = self.client.post(self.book_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        data = {
            "title": "Man of the People",
            "publication_year": 1966,
            "author": self.author.id
        }
        response = self.client.post(self.book_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_book(self):
        response = self.client.get(self.book_detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Things Fall Apart")

    def test_update_book_authenticated(self):
        self.client.login(username='testuser', password='testpass123')
        data = {
            "title": "Updated Title",
            "publication_year": 1959,
            "author": self.author.id
        }
        response = self.client.put(self.book_detail_url(self.book1.id), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book_authenticated(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.delete(self.book_detail_url(self.book2.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_search_books(self):
        response = self.client.get(self.book_url, {'search': 'Things'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_publication_year(self):
        response = self.client.get(self.book_url, {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(response.data[0]['publication_year'], response.data[1]['publication_year'])

    def test_filter_books_by_title(self):
        response = self.client.get(self.book_url, {'title': 'Things Fall Apart'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
