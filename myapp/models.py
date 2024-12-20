from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)  # Updated max_length
    author = models.CharField(max_length=255)  # Updated max_length
    description = models.TextField(blank=True, null=True)  # Optional description field
    published_date = models.DateField(blank=True, null=True)  # Optional publication date
    isbn = models.CharField(max_length=13, blank=True, null=True)  # ISBN field
    image = models.ImageField(upload_to='book_images/', blank=True, null=True)  # Image field for book cover

    def __str__(self):
        return self.title
