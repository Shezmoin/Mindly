from django.test import TestCase
from django.urls import reverse


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
