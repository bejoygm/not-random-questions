from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

from django.test import TestCase
from .models import Goal
from .serializers import GoalSerializer

class ModelTestCase(TestCase):
    """This class defines the test suite for the Goal model."""

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

class ViewTestCase(TestCase):
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


