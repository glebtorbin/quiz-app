from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Quiz, Question, Result, User
from django.contrib.auth.decorators import login_required

def index(request):
    quiz_list = Quiz.objects.all()
    context = {
        'quiz_list': quiz_list,
    }
    return render(request, 'quiz/index.html', context)

@login_required
def quiz_passing(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    if request.method == 'POST':
        questions=Question.objects.filter(quiz=quiz_id)
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            answer = request.POST.get(q.question)
            items = vars(q)
            print(items[answer])
            if q.ans ==  items[answer]:
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        Result.objects.create(
            user=request.user,
            quiz=quiz,
            true_answers=correct,
            false_answers=wrong,
            score=score
        )
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request, 'quiz/result.html',context)

    else:
        questions=Question.objects.filter(quiz=quiz_id)
        context = {
            'questions':questions,
            'quiz': quiz
        }
        return render(request,'quiz/quiz.html',context)

@login_required
def profile(request):
    user = User.objects.get(id=request.user.id)
    results = Result.objects.filter(user=user)
    context = {
        'user': user,
        'results': results
    }
    return render(request, 'quiz/profile.html', context)

