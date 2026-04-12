from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class PagesViewTests(TestCase):
	def setUp(self):
		self.user_model = get_user_model()
		self.user = self.user_model.objects.create_user(
			username='testuser',
			email='test@example.com',
			password='TestPass123!'
		)

	def test_home_returns_200(self):
		"""Test 1: GET / returns 200"""
		response = self.client.get(reverse('pages:home'))
		self.assertEqual(response.status_code, 200)

	def test_dashboard_without_login_returns_302(self):
		"""Test 2: GET /dashboard/ without login returns 302"""
		response = self.client.get(reverse('pages:dashboard'))
		self.assertEqual(response.status_code, 302)
		self.assertIn(reverse('login'), response.url)

	def test_dashboard_with_login_returns_200(self):
		"""Test 3: GET /dashboard/ after login returns 200"""
		self.client.force_login(self.user)
		response = self.client.get(reverse('pages:dashboard'))
		self.assertEqual(response.status_code, 200)


class PagesNavigationTests(TestCase):
	def test_home_links_to_mood_create(self):
		response = self.client.get(reverse('pages:home'))

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, reverse('journal:mood-create'))

	def test_home_links_to_resources_page(self):
		response = self.client.get(reverse('pages:home'))

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, reverse('pages:resources'))

	def test_journal_index_hub_contains_feature_links(self):
		response = self.client.get(reverse('journal:index'))

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, reverse('journal:mood-create'))
		self.assertContains(response, reverse('journal:mood-list'))
		self.assertContains(response, reverse('journal:journal-create'))
		self.assertContains(response, reverse('journal:journal-list'))
