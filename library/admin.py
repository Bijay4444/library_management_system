from django.contrib import admin
from .models import User, Book, BookDetails, BorrowedBooks

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('UserID', 'Name', 'Email', 'MembershipDate')
    search_fields = ('Name', 'Email')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('BookID', 'Title', 'ISBN', 'PublishedDate', 'Genre')
    search_fields = ('Title', 'ISBN')

@admin.register(BookDetails)
class BookDetailsAdmin(admin.ModelAdmin):
    list_display = ('DetailsID', 'Book', 'NumberOfPages', 'Publisher', 'Language')

@admin.register(BorrowedBooks)
class BorrowedBooksAdmin(admin.ModelAdmin):
    list_display = ('UserID', 'BookID', 'BorrowDate', 'ReturnDate')
