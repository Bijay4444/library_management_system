# Library Management System

**NOTE**: I am using XAMPP's mysql so my settings.py database is created accordingly with my UBUNTU enviroment. Please use convinent database settings in settings.py
          for your use.  

## Description
This is a library management system API that allows users to manage books, users, and borrowed books.

## Installation Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Bijay4444/library_management_system.git

2. Create a virtual environment (optional but recommended):
    _bash:-_ python -m venv venv
   
    _Activate the virtual environment:_

    _For Windows:_ .\venv\Scripts\activate

3. Install dependencies:
    ~ pip install -r requirements.txt

4. Apply database migrations:
    ~ python manage.py migrate

5. Run the development server:
   ~python manage.py runserver

##API Documentation##

**Note**: Remeber to create a superuser and login to admin example: "http://127.0.0.1:8000/admin" and take authentication JWT token from there
      OR, You can take the token from POSTMAN using POST method with "http://127.0.0.1:8000/auth/login/ and provide body JSON like:-
          
          #as per your created super user
          {
            "username": "admin",
            "password": "admin"          
           }

           then you will get the result in body like this:
           {
              "token": "b4e8166c716423969057edf18e4debedccf75883"
           }

          Finally, use this token while sending request by including it Headers of POSTMAN like: 

              "key field" : Authorization
              "Value field" : Token b4e8166c716423969057edf18e4debedccf75883
              
##WORKINGS OF API ENDPOINTS

**Users**
    
    GET /library/users/
        > Retrieve a list of all users.
        > Authentication required.

    POST /library/users/
        > Create a new user.
        > Authentication required.
        > Request Body:
                        {
                          "Name": "John Doe",
                          "Email": "john@example.com",
                          "MembershipDate": "2022-01-01"
                        }


    PUT/PATCH /library/users/{user_id}/
        > Update a user's information.
        > Authentication required.
        > Request Body: 
                      {
                          "Name": "Updated Name",
                          "Email": "updated_email@example.com",
                          "MembershipDate": "2021-01-01"
                      }


    DELETE /library/users/{user_id}/
        > Delete a user.
        > Authentication required.

  **Books**
     
    _ Get all Books_

    GET /library/books/
        > Retrieve a list of all books.
        > Authentication required.

    _Create a Book_

    POST /library/books/
        > Create a new book.
        > Authentication required.
        > Request Body:

        json

        {
            "Title": "Psycocybernetics",
            "ISBN": "1234567890123",
            "PublishedDate": "2022-01-01",
            "Genre": "Science Fiction"
        }

    _Update a Book_

    PUT /library/books/{book_id}/
        > Update a book's information.
        > Authentication required.
        > Request Body:

        json

        {
            "Title": "Updated Book Title",
            "Genre": "Non-fiction"
        }

    _Delete a Book_

    DELETE /library/books/{book_id}/
        > Delete a book.
        > Authentication required.
  
  **Book Details**
    
    __Get all Book Details_
    
    GET /library/bookdetails/
        > Retrieve a list of all book details.
        > Authentication required.

    _Create Book Details_

    POST /library/bookdetails/
        > Create details for a book.
        > Authentication required.
        > Request Body:

        json

        {
            "BookID": 1,
            "NumberOfPages": 200,
            "Publisher": "Sample Publisher",
            "Language": "English"
        }

    _Update Book Details_

    PUT /library/bookdetails/{bookdetails_id}/
        > Update details for a book.
        > Authentication required.
        > Request Body:

        json

        {
            "NumberOfPages": 250,
            "Publisher": "Updated Publisher"
        }
  
    _Delete Book Details_

    DELETE /library/bookdetails/{bookdetails_id}/
        > Delete details for a book.
        > Authentication required.

  **Borrowed Books**
    
    _Get all Borrowed Books_

    GET /library/borrowedbooks/
        > Retrieve a list of all borrowed books.
        > Authentication required.

    _Borrow a Book_

    POST /library/borrowedbooks/
        > Borrow a book.
        > Authentication required.
        > Request Body:

        json

        {
            "UserID": 1,
            "BookID": 1,
            "BorrowDate": "2023-01-01"
        }
    
    _Return a Borrowed Book_

    PUT /library/borrowedbooks/{borrowedbook_id}/
        > Return a borrowed book.
        > Authentication required.
        > Request Body:

        json

        {
            "ReturnDate": "2023-02-01"
        }
    
    _Delete a Borrowed Book_

    DELETE /library/borrowedbooks/{borrowedbook_id}/
        > Delete a borrowed book.
        > Authentication required.
