from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Quiz, Answer
from django.contrib.auth.decorators import login_required
from .models import (
    Question,
    Quiz,
    Answer
)

def index(request):
    quiz_list = Quiz.objects.all()
    context = {
        'quiz_list': quiz_list,
    }
    return render(request, 'quiz/index.html', context)


def quiz_passing(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    questions = Question.objects.filter(quiz=quiz_id)
    paginator = Paginator(questions, 1)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        all_que = paginator.page(page)
    except:
        all_que = paginator.page(paginator.num_pages)
    return render(request, 'quiz/quiz.html', {'questions': questions, 'quiz': quiz, 'all_que': all_que})

def result_page(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)