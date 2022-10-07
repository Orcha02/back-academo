from django import forms
from .models import Question, ChooseAnswer, AnsweredQuestions

class ChooseInlineFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super(ChooseInlineFormSet, self).clean()

        correct_answer = 0
        for form in self.forms:
            if not form.is_valid():
                return
            
            if form.cleaned_data and form.cleaned_data.get('correctAnswer') is True:
                correct_answer += 1
