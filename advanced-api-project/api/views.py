from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
import django_filters

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Add filtering, search, and ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Filter by specific fields (exact matches or ranges)
    filterset_fields = ['title', 'author', 'publication_year']

    # Enable search on these fields (text search)
    search_fields = ['title', 'author']

    # Allow ordering by these fields
    ordering_fields = ['title', 'publication_year']

    # Optional: default ordering
    ordering = ['title']

    from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read-only for unauthenticated, create allowed if authenticated

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['title', 'author', 'publication_year']  # Allow filtering by these fields
    search_fields = ['title', 'author']  # Enable search on title and author
    ordering_fields = ['publication_year', 'title']  # Allow ordering by these fields

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update or delete



from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
        SearchFilter
    ]
    filterset_fields = ['publication_year', 'author__name']
    ordering_fields = ['title', 'publication_year']
    search_fields = ['title', 'author__name']


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    from django_filters import rest_framework as django_filters
from rest_framework import filters

filter_backends = [
    django_filters.DjangoFilterBackend,
    filters.OrderingFilter,
    filters.SearchFilter,
]

# Example: enable filtering, searching, and ordering
filterset_fields = ['title', 'author', 'publication_year']
search_fields = ['title', 'author']
ordering_fields = ['title', 'publication_year']

from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    # Filtering options
    filterset_fields = ['title', 'author__name', 'publication_year']

    # Searching options
    search_fields = ['title', 'author__name']

    # Ordering options
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering

"""
BookListView provides list and create operations for books.

Features:
- Filtering by title, author name, and publication year.
- Searching by title and author name.
- Ordering by title and publication year.

Example queries:
    /api/books/?author__name=John
    /api/books/?search=python
    /api/books/?ordering=-publication_year
"""
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    """
    GET: List all books
    POST: Create a new book (authenticated users only)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a single book by ID
    PUT/PATCH: Update a book (authenticated users only)
    DELETE: Delete a book (authenticated users only)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
