from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# ======================
#  Book Generic Views
# ======================

class BookListView(generics.ListAPIView):
    """
    GET /books/
    Returns a list of all books.
    Accessible to everyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Public read access


class BookDetailView(generics.RetrieveAPIView):
    """
    GET /books/<pk>/
    Returns details for a specific book by its ID.
    Accessible to everyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookCreateView(generics.CreateAPIView):
    """
    POST /books/
    Creates a new book entry.
    Requires authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Hook to handle extra logic before saving.
        """
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH /books/<pk>/
    Updates an existing book.
    Requires authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /books/<pk>/
    Deletes a book by ID.
    Requires authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # or custom permission

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]  # only admins can delete
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  
    # Allow anyone to read, but only authenticated users can create

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  
    # Only authenticated users can update

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  
    # Only authenticated users can delete (you can restrict further if needed)

from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

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
filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
filterset_fields = ['title', 'author', 'publication_year']

from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter

from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [filters.DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering
# Add these imports at the top
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter

# Add these to your BookListView class:
filter_backends = [filters.DjangoFilterBackend, SearchFilter, OrderingFilter]
filterset_fields = ['title', 'author', 'publication_year']
search_fields = ['title', 'author']
ordering_fields = ['title', 'publication_year']
ordering = ['title']

# api/views.py

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering
from django_filters import rest_framework as filters
filter_backends = [filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]

from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from rest_framework.filters import SearchFilter
filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from rest_framework.filters import SearchFilter
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from rest_framework.filters import SearchFilter
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']
