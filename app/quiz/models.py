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
    text = models.TextField('Text')


class Answer(models.Model):
    question = models.ForeignKey(Question, verbose_name='Question',
                                 on_delete=models.CASCADE,
                                 related_name='answers')
    text = models.TextField('Text')
    is_true = models.BooleanField('Is true', default=False)


class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='client')
    quiz = models.ForeignKey(Quiz, verbose_name='Quiz',
                             on_delete=models.CASCADE,
                             related_name='results')
    true_answers = models.PositiveSmallIntegerField('True answers', default=0)
    false_answers = models.PositiveSmallIntegerField('False answers', default=0)
    result_date = models.DateTimeField('Done at', auto_now_add=True)
