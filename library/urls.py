
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, BookViewSet, BookDetailsViewSet, BorrowedBooksViewSet

# Creating a router and registering our viewsets with it.
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'books', BookViewSet, basename='book')
router.register(r'bookdetails', BookDetailsViewSet, basename='bookdetails')
router.register(r'borrowedbooks', BorrowedBooksViewSet, basename='borrowedbooks')

urlpatterns = [
    path('', include(router.urls)),
]

