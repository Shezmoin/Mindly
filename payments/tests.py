from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from users.models import UserProfile


class PaymentsSubscriptionUpgradeTests(TestCase):
    def setUp(self):
        self.user_model = get_user_model()
        self.user = self.user_model.objects.create_user(
            username='premiumupgrade',
            email='',
            password='StrongPass123!',
        )

    @patch('payments.views.stripe.checkout.Session.create')
    def test_checkout_sets_user_metadata_for_mapping(self, mock_create):
        mock_create.return_value.url = 'https://example.com/stripe-checkout'
        self.client.force_login(self.user)

        response = self.client.get(reverse('payments:checkout'))

        self.assertEqual(response.status_code, 302)
        _, kwargs = mock_create.call_args
        self.assertIn('metadata', kwargs)
        self.assertEqual(kwargs['metadata'].get('user_id'), str(self.user.id))
        self.assertIn('session_id={CHECKOUT_SESSION_ID}', kwargs.get('success_url', ''))

    @patch('payments.views.stripe.checkout.Session.retrieve')
    def test_success_view_upgrades_premium_from_session_metadata(self, mock_retrieve):
        mock_retrieve.return_value = {
            'mode': 'subscription',
            'status': 'complete',
            'metadata': {'user_id': str(self.user.id)},
            'customer_email': '',
        }
        self.client.force_login(self.user)

        response = self.client.get(
            reverse('payments:success') + '?type=subscription&session_id=cs_test_123',
        )

        self.assertEqual(response.status_code, 200)
        profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(profile.subscription_tier, UserProfile.TIER_PREMIUM)
