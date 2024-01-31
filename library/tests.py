from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import User, Book, BookDetails, BorrowedBooks

class LibraryAPITests(TestCase):
    #user and book tests
    def setUp(self):
        # Create sample data for testing
        self.user = User.objects.create(Name="John Doe", Email="john@example.com", MembershipDate="2022-01-01")
        self.book = Book.objects.create(Title="Sample Book", ISBN="1234567890123", PublishedDate="2022-01-01", Genre="Fiction")
        self.book_details = BookDetails.objects.create(Book=self.book, NumberOfPages=200, Publisher="Sample Publisher", Language="English")

    def test_create_user(self):
        url = reverse('user-list')  # Actual name: 'user-list'
        data = {'Name': 'New User', 'Email': 'newuser@example.com', 'MembershipDate': '2023-01-01'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)  # Assuming one user is created in setUp

    def test_list_all_users(self):
        url = reverse('user-list')  # Actual name: 'user-list'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Assuming one user is created in setUp

    def test_get_user_by_id(self):
        url = reverse('user-detail', args=[self.user.pk])  # Actual name: 'user-detail'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['Name'], 'John Doe')

    #bookdetails tests
    def test_assign_update_book_details(self):
        url = reverse('bookdetails-detail', args=[self.book_details.pk])
        data = {
            'Book': self.book_details.Book.pk,  # Provide the existing Book ID
            'NumberOfPages': 250,
            'Publisher': 'Updated Publisher',
            'Language': 'Spanish',
        }
        response = self.client.put(url, data, content_type='application/json')
        # print(response.content)  #debugging response content to see what's wrong
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book_details.refresh_from_db()
        self.assertEqual(self.book_details.NumberOfPages, 250)
        self.assertEqual(self.book_details.Publisher, 'Updated Publisher')

    #borrow and return books tests
    def test_borrow_return_books(self):
        # Created another user and book for testing
        another_user = User.objects.create(Name="Jane Doe", Email="jane@example.com", MembershipDate="2022-01-01")
        another_book = Book.objects.create(Title="Another Book", ISBN="9876543210123", PublishedDate="2022-01-01", Genre="Non-fiction")

        # Borrowed a book
        borrow_url = reverse('borrowedbooks-list')  # Actual name: 'borrowedbooks-list'
        borrow_data = {'UserID': another_user.pk, 'BookID': another_book.pk, 'BorrowDate': '2023-01-01'}
        borrow_response = self.client.post(borrow_url, borrow_data, format='json', content_type='application/json')
        self.assertEqual(borrow_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BorrowedBooks.objects.count(), 1)

        # Returned the book
        return_url = reverse('borrowedbooks-detail', args=[BorrowedBooks.objects.first().pk])  # Actual name: 'borrowedbooks-detail'
        return_data = {'ReturnDate': '2023-02-01'}
        return_response = self.client.patch(return_url, return_data, format='json', content_type='application/json')
        self.assertEqual(return_response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(BorrowedBooks.objects.first().ReturnDate)

        # more tests for other CRUD operations on BorrowedBooks and other models
        def test_update_borrowed_book(self):
            url = reverse('borrowedbooks-detail', args=[self.borrowed_book.pk])
            data = {'ReturnDate': '2022-03-01'}
            response = self.client.patch(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.borrowed_book.refresh_from_db()
            self.assertEqual(self.borrowed_book.ReturnDate, '2022-03-01')

        def test_delete_borrowed_book(self):
            url = reverse('borrowedbooks-detail', args=[self.borrowed_book.pk])
            response = self.client.delete(url)
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
            self.assertFalse(BorrowedBooks.objects.filter(pk=self.borrowed_book.pk).exists())
