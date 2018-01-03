from django.db import models

class Goal(models.Model):
    """This class represents the Goal model."""
    name = models.CharField(max_length=400, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Goal: {}".format(self.name)
