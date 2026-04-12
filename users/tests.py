from django.contrib.auth import get_user_model
from django.test import TestCase

from users.models import UserProfile


class TestCustomUser(TestCase):
    def setUp(self):
        self.user_model = get_user_model()
        self.user = self.user_model.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='StrongPass123!'
        )

    def test_username_is_saved_correctly(self):
        self.assertEqual(self.user.username, 'testuser')

    def test_user_profile_is_created(self):
        profile = UserProfile.objects.filter(user=self.user).first()
        self.assertIsNotNone(profile)

    def test_default_subscription_tier_is_free(self):
        profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(profile.subscription_tier, 'free')
