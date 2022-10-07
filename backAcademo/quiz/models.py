from django.db import models

# Create your models here.
from courses.models import Classes

class Question(models.Model):
    text = models.TextField(verbose_name="Question text")
    classes = models.ForeignKey(Classes, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.text
    
class ChooseAnswer(models.Model):
    MAX_CHOICES = 4
    question = models.ForeignKey(Question, related_name="questions", on_delete=models.CASCADE)
    correctAnswer = models.BooleanField(verbose_name="Is this the correct answer?", default=False, null=False)
    text = models.TextField(verbose_name="Text of answer")

    def __str__(self):
        return self.text
    
