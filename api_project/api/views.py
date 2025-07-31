from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()          # Fetch all books
    serializer_class = BookSerializer      # Serialize with BookSerializer
