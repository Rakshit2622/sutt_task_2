from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User


class Question(models.Model):
	question_content = models.CharField(max_length=200)
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.question_content

	def was_published_recently(self):
		return self.date_posted >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
	question = models.ForeignKey(Question , on_delete = models.CASCADE)
	choice_content = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_content


