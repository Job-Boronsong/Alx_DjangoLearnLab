from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()          # Fetch all books
    serializer_class = BookSerializer      # Serialize with BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# New ViewSet for full CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()              # All books
    serializer_class = BookSerializer          # Use our serializer
    permission_classes = [IsAuthenticated] 