from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Question, AnsweredQuestions

# Create your views here.


def quiz(request):
    if request.method == 'POST':
        question_pk = request.POST.get('question_pk')
        answered_question = User.attempts.select_related('question').get(question__pk=question_pk)
        answer_pk = request.POST.get('answer_pk')

        try:
            ChooseAnswer = AnsweredQuestions.question.questions.get(pk=answer_pk)
        except ObjectDoesNotExist:
            raise Http404

        User.validate_answer(answered_question, ChooseAnswer)
        return redirect('result', answuered_question.pk)
    else:
        answered = AnsweredQuestions.objects.values_list('question__pk', flat=True)
        question = Question.objects.exclude(pk__in=answered)
        context = {
            'question':question
        }
        return render(request, 'quiz/exam.html', context)
