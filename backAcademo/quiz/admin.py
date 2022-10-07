from django.contrib import admin

# Register your models here.
from .models import Question, ChooseAnswer, AnsweredQuestions
from .forms import ChooseInlineFormSet

# Create tabular inline field
class ChooseAnswerInline(admin.TabularInline):
    model = ChooseAnswer
    can_delete = False
    max_num = ChooseAnswer.MAX_CHOICES 
    min_num = ChooseAnswer.MAX_CHOICES
    form_set = ChooseInlineFormSet

# For better visualization of organized fields in admin
class QuestionAdmin(admin.ModelAdmin):
    model = Question
    inlines = (ChooseAnswerInline, )
    list_display = ['text',]
    # Question has FK relation to ChooseAnswer with related_name 'questions'
    # We'll access to 'questions' and 'text' by "questions__text"
    search_fields = ['text', 'questions__text']

class AnsweredQuestionsAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'correct', 'score']

    class Meta:
        model = AnsweredQuestions

admin.site.register(AnsweredQuestions)
admin.site.register(Question, QuestionAdmin)
admin.site.register(ChooseAnswer)