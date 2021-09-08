from django.db import models

# Create your models here.

class Question(models.Model):

    question = models.CharField()

class Answer(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)