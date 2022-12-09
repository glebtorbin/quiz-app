from django.contrib import admin

from .models import Quiz, Question, Result

class QuestionInLine(admin.TabularInline):
    model = Question
    extra = 1


class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInLine]
    list_display = ('pk', 'title', 'description', 'is_active',)
    list_editable = ('is_active',)
    search_fields = ('title',)
    list_filter = ('created_at',)
    empty_value_display = '-пусто-'


class ResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'true_answers', 'false_answers', 'result_date')


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Result, ResultAdmin)

