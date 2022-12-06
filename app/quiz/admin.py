from django.contrib import admin

from .models import Quiz, Question, Answer

class AnswersInLine(admin.TabularInline):
    model = Answer
    extra = 4

class QuestionInLine(admin.TabularInline):
    inlines = [AnswersInLine]
    model = Question

class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInLine, AnswersInLine]
    list_display = ('pk', 'title', 'description', 'is_active',)
    list_editable = ('is_active',)
    search_fields = ('title',)
    list_filter = ('created_at',)
    empty_value_display = '-пусто-'




admin.site.register(Quiz, QuizAdmin)


