from rest_framework import generics
from .serializers import GoalSerializer, QuestionSerializer
from .models import Goal, Question


class GoalList(generics.ListCreateAPIView):
    """Creates Goals"""
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Goal."""
        serializer.save()


class GoalDetails(generics.RetrieveUpdateDestroyAPIView):
    """Handles individual goals.
    TOOD: Add write rules for admins of goals only"""
    lookup_field = 'id'
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer


class QuestionList(generics.ListCreateAPIView):
    """Creates Questions Under a Goal"""
    serializer_class = QuestionSerializer

    def get_queryset(self):
        """Get questions associated with the goal"""
        return Question.objects.filter(goal_id=self.kwargs['goal_id'])

    def perform_create(self, serializer):
        goal = Goal.objects.get(id=self.kwargs['goal_id'])
        serializer.save(goal=goal)

