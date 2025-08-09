from django.urls import path
from .views import (
    BookListView, BookDetailView, BookCreateView,
    BookUpdateView, BookDeleteView
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]
from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),              # List all books
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'), # Retrieve single book
    path('books/create/', BookCreateView.as_view(), name='book-create'),   # Create book
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'), # Update book
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'), # Delete book
]
from django.urls import path, include

urlpatterns = [
    # other paths...
    path('api/', include('api.urls')),
]
from django.urls import path
from .views import BookUpdateView, BookDeleteView

urlpatterns = [
    # existing URLs
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
]
from django.urls import path
from .views import BookListView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    # other paths...
]

from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),                 # List all books
    path('books/create/', BookCreateView.as_view(), name='book-create'),      # Create book
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),    # Retrieve single book
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'), # Update book
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'), # Delete book
]
from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateDestroyView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),
]

from django.urls import path
from .views import BookListView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
]
