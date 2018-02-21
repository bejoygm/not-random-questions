from rest_framework import generics
from .serializers import GoalSerializer
from .models import Goal


class CreateView(generics.ListCreateAPIView):
    """Creates Goals"""
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Goal."""
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """Handles individual goals.
    TOOD: Add write rules for admins of goals only"""
    lookup_field = 'id'
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
