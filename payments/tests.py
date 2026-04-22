from unittest.mock import patch
import json

from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings
from django.urls import reverse
import stripe

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

    @patch('payments.views.stripe.checkout.Session.retrieve')
    def test_success_view_donation_does_not_upgrade_subscription(self, mock_retrieve):
        self.client.force_login(self.user)

        response = self.client.get(reverse('payments:success') + '?type=donation')

        self.assertEqual(response.status_code, 200)
        self.user.profile.refresh_from_db()
        self.assertEqual(self.user.profile.subscription_tier, UserProfile.TIER_FREE)
        mock_retrieve.assert_not_called()

    @patch('payments.views.stripe.checkout.Session.retrieve')
    def test_success_view_subscription_payment_mode_does_not_upgrade(self, mock_retrieve):
        mock_retrieve.return_value = {
            'mode': 'payment',
            'status': 'complete',
            'metadata': {'user_id': str(self.user.id)},
            'customer_email': '',
        }
        self.client.force_login(self.user)

        response = self.client.get(
            reverse('payments:success') + '?type=subscription&session_id=cs_test_123',
        )

        self.assertEqual(response.status_code, 200)
        self.user.profile.refresh_from_db()
        self.assertEqual(self.user.profile.subscription_tier, UserProfile.TIER_FREE)

    @override_settings(STRIPE_WEBHOOK_SECRET='whsec_test')
    @patch('payments.views.stripe.Webhook.construct_event')
    def test_webhook_subscription_event_upgrades_profile(self, mock_construct_event):
        payload = {
            'type': 'checkout.session.completed',
            'data': {
                'object': {
                    'mode': 'subscription',
                    'metadata': {'user_id': str(self.user.id)},
                    'customer_email': '',
                }
            },
        }
        mock_construct_event.return_value = payload

        response = self.client.post(
            reverse('payments:stripe-webhook'),
            data=json.dumps(payload),
            content_type='application/json',
            HTTP_STRIPE_SIGNATURE='sig_test',
        )

        self.assertEqual(response.status_code, 200)
        self.user.profile.refresh_from_db()
        self.assertEqual(self.user.profile.subscription_tier, UserProfile.TIER_PREMIUM)

    @override_settings(STRIPE_WEBHOOK_SECRET='whsec_test')
    @patch('payments.views.stripe.Webhook.construct_event')
    def test_webhook_payment_event_does_not_upgrade_profile(self, mock_construct_event):
        payload = {
            'type': 'checkout.session.completed',
            'data': {
                'object': {
                    'mode': 'payment',
                    'metadata': {'user_id': str(self.user.id)},
                    'customer_email': self.user.email,
                }
            },
        }
        mock_construct_event.return_value = payload

        response = self.client.post(
            reverse('payments:stripe-webhook'),
            data=json.dumps(payload),
            content_type='application/json',
            HTTP_STRIPE_SIGNATURE='sig_test',
        )

        self.assertEqual(response.status_code, 200)
        self.user.profile.refresh_from_db()
        self.assertEqual(self.user.profile.subscription_tier, UserProfile.TIER_FREE)

    @override_settings(STRIPE_WEBHOOK_SECRET='whsec_test')
    def test_webhook_without_signature_returns_400(self):
        response = self.client.post(
            reverse('payments:stripe-webhook'),
            data='{}',
            content_type='application/json',
        )

        self.assertEqual(response.status_code, 400)

    @override_settings(DEBUG=False, STRIPE_WEBHOOK_SECRET='whsec_test')
    @patch('payments.views.stripe.Webhook.construct_event')
    def test_webhook_invalid_signature_returns_400_in_non_debug(self, mock_construct_event):
        mock_construct_event.side_effect = stripe.error.SignatureVerificationError(
            'invalid signature',
            'sig_test',
            '{}',
        )

        response = self.client.post(
            reverse('payments:stripe-webhook'),
            data='{}',
            content_type='application/json',
            HTTP_STRIPE_SIGNATURE='sig_test',
        )

        self.assertEqual(response.status_code, 400)

    @override_settings(DEBUG=True, STRIPE_WEBHOOK_SECRET='whsec_test')
    @patch('payments.views.stripe.Webhook.construct_event')
    def test_webhook_debug_fallback_parses_payload_and_upgrades(self, mock_construct_event):
        mock_construct_event.side_effect = stripe.error.SignatureVerificationError(
            'invalid signature',
            'sig_test',
            '{}',
        )
        payload = {
            'type': 'checkout.session.completed',
            'data': {
                'object': {
                    'mode': 'subscription',
                    'metadata': {'user_id': str(self.user.id)},
                    'customer_email': '',
                }
            },
        }

        response = self.client.post(
            reverse('payments:stripe-webhook'),
            data=json.dumps(payload),
            content_type='application/json',
            HTTP_STRIPE_SIGNATURE='sig_test',
        )

        self.assertEqual(response.status_code, 200)
        self.user.profile.refresh_from_db()
        self.assertEqual(self.user.profile.subscription_tier, UserProfile.TIER_PREMIUM)
