# 📚 Book API with Django REST Framework

This API provides endpoints to manage Book entries with full CRUD support using Django REST Framework’s generic views.

---

## 📘 Endpoints

| Method | URL Path                     | Description             | Auth Required |
|--------|------------------------------|-------------------------|---------------|
| GET    | `/api/books/`                | List all books          | ❌ No         |
| GET    | `/api/books/<id>/`           | Retrieve single book    | ❌ No         |
| POST   | `/api/books/create/`         | Create a new book       | ✅ Yes        |
| PUT    | `/api/books/<id>/update/`    | Update a book           | ✅ Yes        |
| DELETE | `/api/books/<id>/delete/`    | Delete a book           | ✅ Yes        |

---

## 🔐 Authentication

- **Token-based authentication** is supported.
- Obtain a token:

```bash
POST /api-token-auth/
{
  "username": "youruser",
  "password": "yourpass"
}


"""
Testing Strategy:
-----------------
- Tests focus on CRUD operations of the Book model via API.
- Checks for correct response codes, data, authentication/authorization.
- Tests use Django REST Framework's APITestCase with an isolated test DB.

How to Run:
-----------
$ python manage.py test api

Test Coverage:
--------------
- List books
- Create book (auth vs no-auth)
- Retrieve book
- Update book
- Delete book
- Search, filter, order
"""
