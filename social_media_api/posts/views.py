from rest_framework import viewsets, permissions, status, generics
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .models import Post, Comment,Like
from .serializers import PostSerializer, CommentSerializer
from notifications.utils import create_notification
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if self.get_object().author != self.request.user:
            raise PermissionDenied("You can only edit your own posts.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied("You can only delete your own posts.")
        instance.delete()

    @action(detail=False, methods=["get"], permission_classes=[permissions.IsAuthenticated])
    def feed(self, request):
        """Return posts from followed users, ordered by date"""
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by("-created_at")
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if self.get_object().author != self.request.user:
            raise PermissionDenied("You can only edit your own comments.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied("You can only delete your own comments.")
        instance.delete()


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if not created:
        return Response({"error": "Already liked"}, status=status.HTTP_400_BAD_REQUEST)

    # Send notification to post author
    if post.author != request.user:
        create_notification(
            recipient=post.author,
            actor=request.user,
            verb="liked your post",
            target=post
        )

    return Response({"message": "Post liked"}, status=status.HTTP_201_CREATED)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def unlike_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

    try:
        like = Like.objects.get(post=post, user=request.user)
        like.delete()
        return Response({"message": "Post unliked"}, status=status.HTTP_200_OK)
    except Like.DoesNotExist:
        return Response({"error": "You haven’t liked this post"}, status=status.HTTP_400_BAD_REQUEST)
    

class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            # create notification for post owner
            if post.author != request.user:
                Notification.objects.create(
                    recipient=post.author,
                    actor=request.user,
                    verb="liked your post",
                    target=post
                )
            return Response({"message": "Post liked"}, status=status.HTTP_201_CREATED)
        return Response({"message": "You already liked this post"}, status=status.HTTP_400_BAD_REQUEST)


class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(user=request.user, post=post).first()
        if like:
            like.delete()
            return Response({"message": "Post unliked"}, status=status.HTTP_200_OK)
        return Response({"message": "You have not liked this post"}, status=status.HTTP_400_BAD_REQUEST)