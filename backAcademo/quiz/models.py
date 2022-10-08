from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from courses.models import Classes

def validate_answer(self, AnsweredQuestions, ChooseAnswer):
    if AnsweredQuestions.question_id != ChooseAnswer.question_id:
        return
    
    AnsweredQuestions.ChooseAnswer = ChooseAnswer
    if ChooseAnswer.correctAnswer is True:
        AnsweredQuestions.correct = True
        AnsweredQuestions.score = ChooseAnswer.question.max_score
        AnsweredQuestions.answer = ChooseAnswer
    AnsweredQuestions.save()

class Question(models.Model):
    NUMBER_OF_ANSWERS_ALLOWED = 1
    max_score = models.DecimalField(verbose_name='Max Score', default=10, decimal_places=2, max_digits=6)
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
    
class AnsweredQuestions(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="attempts")
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(ChooseAnswer, on_delete=models.CASCADE, null=True)
    correct = models.BooleanField(verbose_name="Is this the correct answer?", default=False, null=False)
    score = models.DecimalField(verbose_name="Score Obtained", default=0, decimal_places=2, max_digits=6)
