# Social Media API  

A simple Social Media API built with **Django** and **Django REST Framework (DRF)**.  
This project is the foundation for a social networking platform, starting with **user authentication** and **profile management**.  

---

## 🚀 Features  

- Custom User Model (with `bio`, `profile_picture`, `followers`)  
- User Registration (with token generation)  
- User Login (returns authentication token)  
- User Profile Management (view/update profile)  
- Token Authentication using DRF  

---

## 🛠️ Tech Stack  

- **Python 3.x**  
- **Django 5.x**  
- **Django REST Framework**  
- **DRF Token Authentication**  

---

## 📂 Project Structure  

```
social_media_api/
│
├── accounts/               # User app
│   ├── migrations/         
│   ├── models.py           # Custom User model
│   ├── serializers.py      # User + Auth serializers
│   ├── views.py            # Register, Login, Profile views
│   ├── urls.py             # API routes for accounts
│
├── social_media_api/
│   ├── settings.py         # Project settings
│   ├── urls.py             # Main URL configuration
│
└── manage.py
```

---

## ⚙️ Setup & Installation  

1. **Clone the repository**  

```bash
git clone https://github.com/your-username/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/social_media_api
```

2. **Create a virtual environment & install dependencies**  

```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

pip install -r requirements.txt
```

3. **Apply migrations**  

```bash
python manage.py makemigrations
python manage.py migrate
```

4. **Run the server**  

```bash
python manage.py runserver
```

---

## 🔑 API Endpoints  

### 1. Register  
`POST /api/accounts/register/`  

Request:  
```json
{
  "username": "john",
  "email": "john@example.com",
  "password": "test123"
}
```

Response:  
```json
{
  "user": {
    "username": "john",
    "email": "john@example.com"
  },
  "token": "a1b2c3d4..."
}
```

---

### 2. Login  
`POST /api/accounts/login/`  

Request:  
```json
{
  "username": "john",
  "password": "test123"
}
```

Response:  
```json
{
  "token": "a1b2c3d4..."
}
```

---

### 3. Profile  
`GET /api/accounts/profile/`  

Headers:  
```
Authorization: Token <your_token>
```

Response:  
```json
{
  "id": 1,
  "username": "john",
  "email": "john@example.com",
  "bio": "",
  "profile_picture": null
}
```

---

## 📌 Next Steps  

- Add **posts** and **likes** models  
- Implement **JWT authentication** (optional upgrade)  
- Add **friend/follow requests**  
- Expand to comments, notifications, and feeds  

---

## 👨‍💻 Author  

Built for **ALX Django Learn Lab** 🚀  


New endpoints

GET /api/posts/ – list posts (paginated, ?search=<q>, ?author=<id>, ordering)

POST /api/posts/ – create (auth)

GET /api/posts/{id}/ – retrieve

PATCH/PUT /api/posts/{id}/ – update (owner only)

DELETE /api/posts/{id}/ – delete (owner only)

GET /api/comments/ – list comments (paginated, ?post=<id>, ?author=<id>, search)

POST /api/comments/ – create (auth)

GET /api/comments/{id}/ – retrieve

PATCH/PUT /api/comments/{id}/ – update (owner only)

DELETE /api/comments/{id}/ – delete (owner only)

### 🔗 Follow & Feed API

#### Follow a User
- Endpoint: `POST /users/{id}/follow/`
- Auth required: ✅
- Response:
```json
{ "message": "You are now following username" }