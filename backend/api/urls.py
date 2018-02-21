from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import GoalDetails, GoalList

urlpatterns = [
    path('goal/', GoalList.as_view(), name="goals"),
    path('goal/<id>', GoalDetails.as_view(), name="goal"),
]

urlpatterns = format_suffix_patterns(urlpatterns)