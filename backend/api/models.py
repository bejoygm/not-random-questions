from django.db import models


class Goal(models.Model):
    name = models.CharField(max_length=400, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Goal: {}".format(self.name)


class Question(models.Model):
    """Questions associated with a Goal."""
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    text = models.CharField(max_length=400, blank=False)

    def __str__(self):
    	return "Question: {}".format(self.text)


class Answer(models.Model):
    """desired answer to a Question"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=400, blank=False)

    def __str__(self):
    	return "Answer: {}".format(self.text)

class User(models.Model):
	pass

class Response(models.Model):
	"""Users response to questions"""
	pass
