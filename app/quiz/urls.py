from . import views

from django.urls import path

app_name = 'quiz'

urlpatterns = [
    path('', views.index, name='index'),
    path('quiz_passing/<int:quiz_id>', views.quiz_passing, name='quiz_passing'),
    # path('quiz/<int:quiz_id>/result', views.result_page, name='quiz_result')
]