from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book

# Home Page View
class HomePageView(TemplateView):
    template_name = 'myapp/home.html'

# List Books View
class BookListView(ListView):
    model = Book
    template_name = 'myapp/book_list.html'
    context_object_name = 'books'

# Book Detail View
class BookDetailView(DetailView):
    model = Book
    template_name = 'myapp/book_detail.html'

# Create Book View
class BookCreateView(CreateView):
    model = Book
    template_name = 'myapp/book_form.html'
    fields = ['title', 'author', 'description', 'image']
    success_url = reverse_lazy('book_list')

# Update Book View
class BookUpdateView(UpdateView):
    model = Book
    template_name = 'myapp/book_form.html'
    fields = ['title', 'author', 'description', 'image']
    success_url = reverse_lazy('book_list')

# Delete Book View
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'myapp/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')
