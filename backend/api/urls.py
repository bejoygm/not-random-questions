from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import GoalDetails, GoalList, QuestionList

urlpatterns = [
    path('goal/', GoalList.as_view(), name="goals"),
    path('goal/<id>', GoalDetails.as_view(), name="goal"),
    path('question/<goal_id>', QuestionList.as_view(), name="questions")
]

urlpatterns = format_suffix_patterns(urlpatterns)
