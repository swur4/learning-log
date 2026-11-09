from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Topic, Entry


class LearningLogTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword123'
        )
        self.client.login(
            username='testuser',
            password='testpassword123'
        )
        self.topic = Topic.objects.create(
            text='Python',
            owner=self.user
        )

    def test_topics_page(self):
        response = self.client.get(reverse('learning_logs:topics'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Python')

    def test_create_topic(self):
        response = self.client.post(
            reverse('learning_logs:new_topic'),
            {'text': 'Django'}
        )

        self.assertTrue(
            Topic.objects.filter(
                text='Django',
                owner=self.user
            ).exists()
        )

    def test_create_entry(self):
        response = self.client.post(
            reverse(
                'learning_logs:new_entry',
                args=[self.topic.id]
            ),
            {'text': 'Изучаю Django'}
        )

        self.assertTrue(
            Entry.objects.filter(
                topic=self.topic,
                text='Изучаю Django'
            ).exists()
        )

    def test_user_cannot_see_other_users_topics(self):
        other_user = User.objects.create_user(
            username='otheruser',
            password='otherpassword123'
        )

        Topic.objects.create(
            text='Java',
            owner=other_user
        )

        response = self.client.get(reverse('learning_logs:topics'))

        self.assertContains(response, 'Python')
        self.assertNotContains(response, 'Java')