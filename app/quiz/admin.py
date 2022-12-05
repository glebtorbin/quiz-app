from django.contrib import admin

from .models import Quiz


class QuizAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'is_active',)
    list_editable = ('is_active',)
    search_fields = ('title',)
    list_filter = ('created_at',)
    empty_value_display = '-пусто-'


admin.site.register(Quiz, QuizAdmin)

