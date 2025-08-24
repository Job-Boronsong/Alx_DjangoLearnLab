from django.urls import path, include
from .views import RegisterView, LoginView, ProfileView, UserViewSet
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("profile/", ProfileView.as_view(), name="profile"),path("follow/<int:user_id>/", views.FollowUserView.as_view(), name="follow-user"),
    path("unfollow/<int:user_id>/", views.UnfollowUserView.as_view(), name="unfollow-user"),
    path('', include(router.urls)),
    
]


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
