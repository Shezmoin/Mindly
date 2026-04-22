from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import AssessmentResult


class AssessmentViewTests(TestCase):
    def test_assessment_hub_renders_tools(self):
        response = self.client.get(reverse('assessments:index'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Mood Self-Check')
        self.assertContains(response, 'Stress Self-Check')
        self.assertContains(response, 'Sleep Habits Check')

    def test_mood_self_check_returns_result(self):
        response = self.client.post(
            reverse('assessments:index'),
            {
                'assessment_type': 'mood',
                'q1': '2',
                'q2': '2',
                'q3': '1',
                'q4': '1',
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Your result')
        self.assertContains(response, 'Suggested next step')

    def test_stress_self_check_returns_result(self):
        response = self.client.post(
            reverse('assessments:index'),
            {
                'assessment_type': 'stress',
                'q1': '3',
                'q2': '2',
                'q3': '2',
                'q4': '3',
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Stress Self-Check')
        self.assertContains(response, 'Suggested next step')

    def test_authenticated_user_submission_is_persisted(self):
        user = get_user_model().objects.create_user(
            username='assessment_user',
            email='assessment@example.com',
            password='StrongPass123!',
        )
        self.client.force_login(user)

        response = self.client.post(
            reverse('assessments:index'),
            {
                'assessment_type': 'sleep',
                'q1': '3',
                'q2': '2',
                'q3': '1',
                'q4': '0',
            },
        )

        self.assertEqual(response.status_code, 200)
        saved = AssessmentResult.objects.get(user=user)
        self.assertEqual(saved.assessment_type, 'sleep')
        self.assertEqual(saved.total_score, 6)
        self.assertEqual(saved.level, 'Moderate concern')

    def test_anonymous_submission_is_not_persisted(self):
        self.client.post(
            reverse('assessments:index'),
            {
                'assessment_type': 'mood',
                'q1': '1',
                'q2': '1',
                'q3': '1',
                'q4': '1',
            },
        )

        self.assertEqual(AssessmentResult.objects.count(), 0)
