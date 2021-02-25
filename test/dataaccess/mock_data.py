from BookManager.model.user import User
from BookManager.model.book import Book
from BookManager.model.author import Author
from BookManager.model.category import Category


def load_test_data(test_db):
    # Role.insert_many([
    #     {"id": 1, "role": "user"},
    #     {"id": 2, "role": "admin"},
    # ]).execute()
    # User.insert_many([
    #     {"id": 1, "name": "defaultuser",  "username": "defaultuser", "role": 1, "password": "abcd"},
    #     {"id": 2, "name": "superuser", "username": "superuser", "role": 2, "password": "abcd"},
    # ]).execute()

    Author.insert_many([
        {"id": 1, "author_name": "Chetan"},
        {"id": 2, "author_name": "Mohan"}
    ]).execute()

    Category.insert_many([
        {"id": 1, "category_name": "Adventure", "cat_count": 1},
        {"id": 2, "category_name": "Thriller", "cat_count": 1}
    ]).execute()

    Book.insert_many([
        {"id": 1, "name": "hp", "author": 1, "category": 2, "count": 2},
        {"id": 2, "name": "david copperfield", "author": 2, "category": 1, "count": 3},
        {"id": 3, "name": "frankenstein", "author": 1, "category": 2, "count": 5}

    ]).execute()

    User.insert_many([
        {"id": 1, "username": "admin", "password": "admin", "Role": "Admin"},
        {"id": 2, "username": "user", "password": "user", "Role": "Customer"},
        {"id": 3, "username": "user2", "password": "user2", "Role": "Customer"}
    ])

    # User.insert_many([
    #     {""}
    # ])
