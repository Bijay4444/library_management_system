from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Book, BookDetails, BorrowedBooks
from .serializers import UserSerializer, BookSerializer, BookDetailsSerializer, BorrowedBooksSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class BookDetailsViewSet(viewsets.ModelViewSet):
    queryset = BookDetails.objects.all()
    serializer_class = BookDetailsSerializer
    
class BorrowedBooksViewSet(viewsets.ModelViewSet):
    queryset = BorrowedBooks.objects.all()
    serializer_class = BorrowedBooksSerializer