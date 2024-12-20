from django.urls import path
from .views import (
    HomePageView, BookListView, BookDetailView,
    BookCreateView, BookUpdateView, BookDeleteView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  # Home page
    path('books/', BookListView.as_view(), name='book_list'),  # List all books
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),  # View book details
    path('book/new/', BookCreateView.as_view(), name='book_create'),  # Add a new book
    path('book/<int:pk>/edit/', BookUpdateView.as_view(), name='book_update'),  # Edit a book
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),  # Delete a book
]
