# 📚 LibraryProject

Welcome to **LibraryProject**, a beginner-friendly Django web application created as part of a learning exercise to understand the Django framework.

## 🚀 Project Objective

The goal of this project is to set up a working Django development environment and get familiar with the core components of a Django project including:

- Creating a new project
- Understanding the project structure
- Running the development server

## 🛠️ Technologies Used

- Python 3.x
- Django 4.x (or latest version)
- SQLite3 (default development database)

## 🧱 Project Structure

# Permissions & Groups Guide

## Custom Permissions
Defined in `Book` model:
- `can_view`: View book list/details
- `can_create`: Create a new book
- `can_edit`: Edit a book
- `can_delete`: Delete a book

## Groups
Created via admin panel:

- **Viewers**:
  - Permissions: `can_view`

- **Editors**:
  - Permissions: `can_view`, `can_create`, `can_edit`

- **Admins**:
  - Permissions: `can_view`, `can_create`, `can_edit`, `can_delete`

## Usage in Views
Django's `@permission_required` decorator is used to enforce access:
```python
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):


