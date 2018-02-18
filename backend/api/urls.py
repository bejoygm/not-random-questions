from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView

urlpatterns = [
    path('goal/', CreateView.as_view(), name="create"),
    path('goal/<id>', DetailsView.as_view(), name="details"),
]

urlpatterns = format_suffix_patterns(urlpatterns)