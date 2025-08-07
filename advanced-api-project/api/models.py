from django.db import models
from datetime import datetime

# Author model represents a single book author
class Author(models.Model):
    name = models.CharField(max_length=100)  # Stores the author's name

    def __str__(self):
        return self.name

# Book model represents a single book
class Book(models.Model):
    title = models.CharField(max_length=200)  # Book's title
    publication_year = models.IntegerField()  # Year of publication
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    # Establishes a many-to-one relationship to Author

    def __str__(self):
        return self.title
