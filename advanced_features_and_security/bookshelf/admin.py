from django.contrib import admin
from .models import Book

# Register the Book model
# admin.site.register(Book)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns shown in the list view
    search_fields = ('title', 'author')                     # Enables search bar for these fields
    list_filter = ('publication_year',)                     # Adds a filter sidebar for year

# Register with the custom configuration
admin.site.register(Book, BookAdmin)
