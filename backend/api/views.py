from rest_framework import generics
from .serializers import GoalSerializer
from .models import Goal

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our test api."""
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Goal."""
        serializer.save()