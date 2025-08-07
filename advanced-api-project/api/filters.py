# api/filters.py
import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    """
    A filter class for the Book model.
    It allows filtering by title, publication_year, and author's name.
    """
    author_name = django_filters.CharFilter(field_name='author__name', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = {
            'title': ['exact', 'icontains'],
            'publication_year': ['exact', 'gte', 'lte'],
        }