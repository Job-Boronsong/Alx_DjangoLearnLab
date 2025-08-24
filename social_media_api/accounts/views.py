from rest_framework import generics, permissions
from django.contrib.auth import authenticate, get_user_model
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .serializers import RegisterSerializer, UserSerializer
from rest_framework import status, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from .models import CustomUser   # ✅ Explicit CustomUser import

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()   # ✅ Explicit CustomUser.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=response.data["username"])
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user": response.data,
            "token": token.key
        })


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        return Response({"error": "Invalid credentials"}, status=400)


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserViewSet(viewsets.ModelViewSet, generics.GenericAPIView):  # ✅ Ensure GenericAPIView appears
    queryset = CustomUser.objects.all()   # ✅ Explicit CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def follow(self, request, pk=None):
        """Follow a user"""
        user_to_follow = self.get_object()
        request.user.follow(user_to_follow)
        return Response({"message": f"You are now following {user_to_follow.username}"})

    @action(detail=True, methods=['post'])
    def unfollow(self, request, pk=None):
        """Unfollow a user"""
        user_to_unfollow = self.get_object()
        request.user.unfollow(user_to_unfollow)
        return Response({"message": f"You unfollowed {user_to_unfollow.username}"})
