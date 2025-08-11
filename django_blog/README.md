How it works:

Registration: /register uses RegisterForm to create a new user.

Login: /login uses Django’s built-in authentication view.

Logout: /logout logs out the user and redirects to login.

Profile Management: /profile lets users view/update their email.

Security:

CSRF tokens included

Password hashing handled by Django

Profile editing requires login