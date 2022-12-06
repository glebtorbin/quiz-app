from django.shortcuts import render, redirect, get_object_or_404
from .models import Quiz, Answer
from django.contrib.auth.decorators import login_required
from .forms import QuizForm
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
    quiz = Quiz.objects.get(id = quiz_id)
    questions = Question.objects.filter(quiz=quiz)
    answers = Answer.objects.filter(quiz=quiz, question=questions)
    if request.method == "POST":
        form = QuizForm(quiz_id, request.POST or None)
        if form.is_valid():
            ans = form.save(commit=False)
            ans.save()
            return redirect('quiz:index')
    else:
        form = QuizForm(quiz_id)
    return render(request, 'quiz/quiz.html', {'form': form, 'quiz': quiz, 'questions': questions, 'answers': answers})