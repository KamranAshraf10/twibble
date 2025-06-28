from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Tweet

class TweetModelTest(TestCase):
    def test_create_tweet(self):
        user = User.objects.create_user(username='testuser', password='pass')
        tweet = Tweet.objects.create(user=user, text='Hello!')
        self.assertEqual(str(tweet), 'testuser - Hello!')

class TweetViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='pass')
        self.tweet = Tweet.objects.create(user=self.user, text='Test tweet')

    def test_tweet_list_view(self):
        response = self.client.get(reverse('tweet_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test tweet')

    def test_tweet_create_view_authenticated(self):
        self.client.login(username='testuser', password='pass')
        response = self.client.post(reverse('tweet_create'), {
            'text': 'New tweet',
        })
        self.assertEqual(response.status_code, 302)  # Redirect after creation
        self.assertTrue(Tweet.objects.filter(text='New tweet').exists())

    def test_tweet_create_view_unauthenticated(self):
        response = self.client.post(reverse('tweet_create'), {
            'text': 'Should not work',
        })
        self.assertNotEqual(response.status_code, 200)  # Should redirect to login

    def test_tweet_edit_view(self):
        self.client.login(username='testuser', password='pass')
        response = self.client.post(reverse('tweet_edit', args=[self.tweet.id]), {
            'text': 'Edited tweet',
        })
        self.assertEqual(response.status_code, 302)
        self.tweet.refresh_from_db()
        self.assertEqual(self.tweet.text, 'Edited tweet')

    def test_tweet_delete_view(self):
        self.client.login(username='testuser', password='pass')
        response = self.client.post(reverse('tweet_delete', args=[self.tweet.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Tweet.objects.filter(id=self.tweet.id).exists())

    def test_search_functionality(self):
        Tweet.objects.create(user=self.user, text='UniqueSearchTerm')
        response = self.client.get(reverse('tweet_list'), {'q': 'UniqueSearchTerm'})
        self.assertContains(response, 'UniqueSearchTerm')
        self.assertNotContains(response, 'Test tweet')

class UserAuthTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')

    def test_user_registration(self):
        response = self.client.post(self.register_url, {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_user_login(self):
        User.objects.create_user(username='loginuser', password='pass12345')
        response = self.client.post(self.login_url, {
            'username': 'loginuser',
            'password': 'pass12345',
        })
        self.assertEqual(response.status_code, 302)