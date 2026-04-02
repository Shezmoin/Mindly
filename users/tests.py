<<<<<<< HEAD
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class UserAuthViewsTests(TestCase):
	def setUp(self):
		self.user_model = get_user_model()
		self.user = self.user_model.objects.create_user(
			username='testuser',
			email='test@example.com',
			password='StrongPass123!'
		)

	def test_register_page_renders(self):
		response = self.client.get(reverse('users:register'))

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Create Your Account')

	def test_login_page_renders(self):
		response = self.client.get(reverse('users:login'))

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Welcome Back')

	def test_profile_redirects_to_login_when_logged_out(self):
		response = self.client.get(reverse('users:profile'))

		self.assertEqual(response.status_code, 302)
		self.assertIn(reverse('users:login'), response.url)

	def test_profile_renders_for_authenticated_user(self):
		self.client.force_login(self.user)

		response = self.client.get(reverse('users:profile'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, self.user.username)

	def test_logout_logs_out_user(self):
		self.client.force_login(self.user)
		response = self.client.get(reverse('users:logout'))

		self.assertEqual(response.status_code, 200)
		self.assertFalse(response.wsgi_request.user.is_authenticated)
=======
# Create your tests here.
>>>>>>> 04c11c74a48edb4abaea6dc8325a8cb21860f238
