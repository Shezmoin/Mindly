from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import JournalEntry, MoodEntry


class JournalViewsTests(TestCase):
    def setUp(self):
        self.user_model = get_user_model()
        self.user = self.user_model.objects.create_user(
            username='journaluser',
            email='journal@example.com',
            password='StrongPass123!',
        )
        self.other_user = self.user_model.objects.create_user(
            username='otheruser',
            email='other@example.com',
            password='StrongPass123!',
        )

    def test_mood_create_redirects_for_logged_out_user(self):
        response = self.client.get(reverse('journal:mood-create'))

        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('login'), response.url)

    def test_mood_create_renders_slider_widget(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('journal:mood-create'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'type="range"')
        self.assertContains(response, 'id="id_mood_score"')

    def test_journal_create_assigns_logged_in_user(self):
        self.client.force_login(self.user)

        response = self.client.post(
            reverse('journal:journal-create'),
            {
                'title': 'My first entry',
                'content': 'Today I feel focused.',
                'is_private': 'on',
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('journal:journal-list'))

        entry = JournalEntry.objects.get(title='My first entry')
        self.assertEqual(entry.user, self.user)
        self.assertTrue(entry.is_private)

    def test_journal_list_only_shows_current_user_entries(self):
        JournalEntry.objects.create(
            user=self.user,
            title='My visible entry',
            content='Owned by current user',
            is_private=False,
        )
        JournalEntry.objects.create(
            user=self.other_user,
            title='Other user entry',
            content='Should never be visible',
            is_private=True,
        )

        self.client.force_login(self.user)
        response = self.client.get(reverse('journal:journal-list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'My visible entry')
        self.assertNotContains(response, 'Other user entry')

    def test_journal_list_orders_by_most_recent_updated_at(self):
        self.client.force_login(self.user)
        older = JournalEntry.objects.create(
            user=self.user,
            title='Older entry',
            content='Older content',
            is_private=True,
        )
        newer = JournalEntry.objects.create(
            user=self.user,
            title='Newer entry',
            content='Newer content',
            is_private=False,
        )
        older.content = 'Older content updated later'
        older.save()

        response = self.client.get(reverse('journal:journal-list'))
        entries = list(response.context['entries'])

        self.assertGreaterEqual(len(entries), 2)
        self.assertEqual(entries[0].id, older.id)
        self.assertIn(newer.id, [entry.id for entry in entries])

    def test_journal_edit_updates_only_current_users_entry(self):
        entry = JournalEntry.objects.create(
            user=self.user,
            title='Original title',
            content='Original content',
            is_private=True,
        )

        self.client.force_login(self.user)
        response = self.client.post(
            reverse('journal:journal-edit', args=[entry.pk]),
            {
                'title': 'Updated title',
                'content': 'Updated content',
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('journal:journal-list'))

        entry.refresh_from_db()
        self.assertEqual(entry.title, 'Updated title')
        self.assertEqual(entry.content, 'Updated content')
        self.assertFalse(entry.is_private)
        self.assertEqual(entry.user, self.user)

    def test_journal_edit_returns_404_for_other_users_entry(self):
        entry = JournalEntry.objects.create(
            user=self.other_user,
            title='Other title',
            content='Other content',
            is_private=True,
        )

        self.client.force_login(self.user)
        response = self.client.get(reverse('journal:journal-edit', args=[entry.pk]))

        self.assertEqual(response.status_code, 404)

    def test_journal_delete_confirmation_page_renders(self):
        entry = JournalEntry.objects.create(
            user=self.user,
            title='Delete me',
            content='To be deleted',
            is_private=True,
        )

        self.client.force_login(self.user)
        response = self.client.get(reverse('journal:journal-delete', args=[entry.pk]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This action cannot be undone.')
        self.assertContains(response, entry.title)

    def test_journal_delete_removes_entry_after_confirmation(self):
        entry = JournalEntry.objects.create(
            user=self.user,
            title='Delete after confirm',
            content='To be deleted after post',
            is_private=True,
        )

        self.client.force_login(self.user)
        response = self.client.post(
            reverse('journal:journal-delete', args=[entry.pk]),
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('journal:journal-list'))
        self.assertFalse(JournalEntry.objects.filter(pk=entry.pk).exists())

    def test_journal_delete_returns_404_for_other_users_entry(self):
        entry = JournalEntry.objects.create(
            user=self.other_user,
            title='Protected entry',
            content='Should not be deletable',
            is_private=True,
        )

        self.client.force_login(self.user)
        response = self.client.get(reverse('journal:journal-delete', args=[entry.pk]))

        self.assertEqual(response.status_code, 404)

    def test_mood_list_only_shows_current_user_entries(self):
        MoodEntry.objects.create(user=self.user, mood_score=7, note='Mine')
        MoodEntry.objects.create(
            user=self.other_user,
            mood_score=3,
            note='Other user',
        )

        self.client.force_login(self.user)
        response = self.client.get(reverse('journal:mood-list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Mine')
        self.assertNotContains(response, 'Other user')

    def test_mood_create_with_score_7_creates_entry_and_redirects(self):
        """Test 4: POST to mood create creates one entry and redirects."""
        self.client.force_login(self.user)

        response = self.client.post(
            reverse('journal:mood-create'),
            {'mood_score': 7, 'note': 'Feeling great today'},
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('pages:dashboard'))

        entries = MoodEntry.objects.filter(user=self.user)
        self.assertEqual(entries.count(), 1)
        self.assertEqual(entries.first().mood_score, 7)
        self.assertEqual(entries.first().note, 'Feeling great today')

    def test_mood_edit_updates_only_current_users_entry(self):
        entry = MoodEntry.objects.create(
            user=self.user,
            mood_score=5,
            note='Before update',
        )

        self.client.force_login(self.user)
        response = self.client.post(
            reverse('journal:mood-edit', args=[entry.pk]),
            {'mood_score': 8, 'note': 'After update'},
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('journal:mood-list'))

        entry.refresh_from_db()
        self.assertEqual(entry.mood_score, 8)
        self.assertEqual(entry.note, 'After update')
        self.assertEqual(entry.user, self.user)

    def test_mood_edit_returns_404_for_other_users_entry(self):
        entry = MoodEntry.objects.create(
            user=self.other_user,
            mood_score=4,
            note='Other user mood',
        )

        self.client.force_login(self.user)
        response = self.client.get(reverse('journal:mood-edit', args=[entry.pk]))

        self.assertEqual(response.status_code, 404)

    def test_free_user_cannot_create_more_than_five_journal_entries_in_a_month(self):
        self.client.force_login(self.user)

        for index in range(5):
            JournalEntry.objects.create(
                user=self.user,
                title=f'Entry {index}',
                content='Existing entry',
                is_private=True,
            )

        response = self.client.post(
            reverse('journal:journal-create'),
            {
                'title': 'Sixth entry',
                'content': 'This should be blocked.',
                'is_private': 'on',
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(JournalEntry.objects.filter(user=self.user).count(), 5)
        self.assertContains(
            response,
            'Free users can only create 5 journal entries per month',
        )
