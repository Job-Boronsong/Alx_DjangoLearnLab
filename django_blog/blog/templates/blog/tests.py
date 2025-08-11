# blog/tests.py (very basic skeleton)
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post

class PostTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='alice', password='pass')
        self.post = Post.objects.create(title='Hello', content='Content', author=self.user)

    def test_posts_list_view(self):
        resp = self.client.get(reverse('posts-list'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Hello')

    def test_create_requires_login(self):
        resp = self.client.get(reverse('post-create'))
        self.assertNotEqual(resp.status_code, 200)  # redirected to login
