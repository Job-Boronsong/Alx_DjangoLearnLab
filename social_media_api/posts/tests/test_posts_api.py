from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from posts.models import Post, Comment

User = get_user_model()

class PostsCommentsAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="u1", password="pass123")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

    def test_create_post_and_comment(self):
        # Create Post
        resp = self.client.post("/api/posts/", {"title": "T", "content": "C"}, format="json")
        self.assertEqual(resp.status_code, 201)
        post_id = resp.data["id"]

        # Create Comment
        resp2 = self.client.post("/api/comments/", {"post": post_id, "content": "Nice"}, format="json")
        self.assertEqual(resp2.status_code, 201)

        # List comments by post
        resp3 = self.client.get(f"/api/comments/?post={post_id}")
        self.assertEqual(resp3.status_code, 200)
        self.assertEqual(len(resp3.data["results"]), 1)

    def test_owner_only_edit(self):
        post = Post.objects.create(author=self.user, title="A", content="B")
        # Another user
        other = User.objects.create_user(username="u2", password="pass123")
        other_token = Token.objects.create(user=other)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {other_token.key}")
        r = self.client.patch(f"/api/posts/{post.id}/", {"title": "nope"}, format="json")
        self.assertEqual(r.status_code, 403)
