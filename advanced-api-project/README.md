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
