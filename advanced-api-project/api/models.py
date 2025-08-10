from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime

class Author(models.Model):
    """
    Represents an author who has written one or more books.
    """
    name = models.CharField(max_length=100)  # Author's full name

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Represents a book written by an author.
    Each book is linked to exactly one author.
    """
    title = models.CharField(max_length=200)  # Book title
    publication_year = models.IntegerField()  # Year of publication
    author = models.ForeignKey(
        Author,
        related_name='books',  # Allows reverse access: author.books.all()
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
    
    from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    pages = models.IntegerField()
    cover = models.URLField(blank=True, null=True)
    language = models.CharField(max_length=30)

    def __str__(self):
        return self.title


