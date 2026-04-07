from django.test import TestCase
from django.urls import reverse


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
