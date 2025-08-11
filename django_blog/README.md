How it works:

Registration: /register uses RegisterForm to create a new user.

Login: /login uses Django’s built-in authentication view.

Logout: /logout logs out the user and redirects to login.

Profile Management: /profile lets users view/update their email.

Security:

CSRF tokens included

Password hashing handled by Django

Profile editing requires login

Blog Post Management (CRUD)
--------------------------
URLs:
- /posts/               -> list all posts (anyone)
- /posts/new/           -> create a post (authenticated users only)
- /posts/<int:pk>/      -> view post detail (anyone)
- /posts/<int:pk>/edit/ -> edit post (author only)
- /posts/<int:pk>/delete/-> delete post (author only)

Forms:
- Uses blog/forms.py PostForm (ModelForm). author auto-assigned from request.user.

Views:
- Class-based views in blog/views.py:
  ListView, DetailView, CreateView, UpdateView, DeleteView
  Create/Update/Delete protected by LoginRequiredMixin and UserPassesTestMixin.

Testing:
- Run the server and manually verify flows.
- Use automated tests in blog/tests.py as needed.

Security:
- CSRF protection enabled (use {% csrf_token %} in templates).
- Passwords/higher-security flows are handled by Django's auth system.
- Only the author may edit/delete their posts.
