from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

from django.test import TestCase
from .models import Goal

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
            reverse('create'),
            self.goal_data,
            format="json"
        )

    def test_api_can_create_a_goal(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)