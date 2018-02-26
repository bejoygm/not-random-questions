from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

from django.test import TestCase
from .models import Goal, Question
from .serializers import GoalSerializer, QuestionSerializer


class GoalModelTestCase(TestCase):
    """Test suite for the Goal model."""

    def setUp(self):
        """Define the test client and other test variables"""
        self.goal_name = "Make a pizza"
        self.goal = Goal(name=self.goal_name)

    def test_modal_can_create_a_goal(self):
        """Test the goal modal can create a goal."""
        old_count = Goal.objects.count()
        self.goal.save()
        new_count = Goal.objects.count()
        self.assertNotEqual(old_count, new_count)


class GoalViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.goal_data = {'name': 'Make Crane Oragami'}
        self.response = self.client.post(
            reverse('goals'),
            self.goal_data,
            format="json"
        )

    def test_api_can_create_a_goal(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_goal(self):
        goal = Goal.objects.get()
        response = self.client.get(
            reverse('goal',
                    kwargs={'id': goal.id}), format='json'
        )
        serializer = GoalSerializer(goal)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    # add auth for update and delete
    def test_api_can_update_goal(self):
        goal = Goal.objects.get()
        update_goal = {'name': 'Cranes everywhere'}
        response = self.client.put(
            reverse('goal', kwargs={'id': goal.id}),
            update_goal, format='json'
        )
        self.assertEqual(response.data['name'], update_goal['name'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete_goal(self):
        goal = Goal.objects.get()
        response = self.client.delete(
            reverse('goal', kwargs={'id': goal.id}),
            format='json',
            follow=True
        )
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

class QuestionModelTestCase(TestCase):
    """Test suite for Question Model"""

    def setUp(self):
        # TODO: introduce factory
        self.goal_name = "Make a pizza"
        self.goal = Goal(name=self.goal_name)
        self.goal.save()
        self.question_text = 'Prepare dough'
        self.question = Question(text=self.question_text, goal=self.goal)

    def test_modal_can_create_a_question(self):
        old_count = Question.objects.count()
        self.question.save()
        new_count = Question.objects.count()
        self.assertNotEqual(old_count, new_count)

class QuestionViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        # TODO: mock api calls
        self.goal_name = "Make a pizza"
        self.goal = Goal(name=self.goal_name)
        self.goal.save()
        self.question_data = {'text': 'Prepare dough'}
        self.client = APIClient()
        self.response = self.client.post(
            reverse('questions',
                    kwargs={'goal_id': self.goal.id}),
            self.question_data,
            format='json'
        )

    def test_api_can_create_question_under_a_goal(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

