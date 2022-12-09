from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Quiz(models.Model):
    title = models.CharField('Title', max_length=192)
    description = models.TextField('Description', blank=True, null=True)
    is_active = models.BooleanField('Is active?', default=True)
    created_at = models.DateTimeField('Created at', auto_now_add=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, verbose_name='Quiz',
                             on_delete=models.CASCADE,
                             related_name='questions')
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question


class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='client')
    quiz = models.ForeignKey(Quiz, verbose_name='Quiz',
                             on_delete=models.CASCADE,
                             related_name='results')
    true_answers = models.PositiveSmallIntegerField('True answers', default=0)
    false_answers = models.PositiveSmallIntegerField('False answers', default=0)
    result_date = models.DateTimeField('Done at', auto_now_add=True)
    score = models.PositiveSmallIntegerField('score', default=0)
