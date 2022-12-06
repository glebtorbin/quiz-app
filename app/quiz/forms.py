from django import forms

from .models import Answer, Question


class QuizForm(forms.Form):
    def __init__(self, quiz_id):
        super(QuizForm, self).__init__()
        questions = Question.objects.filter(quiz=quiz_id)
        for question in questions:
            choices = []
            answers = Answer.objects.filter(question=question.id)
            for answer in answers:
                choices.append((answer.pk, answer.text))
                self.fields["question_%d" % question.pk] = forms.ChoiceField(label=question.text,
                                                                             required=True,
                                                                             choices=choices,
                                                                             widget=forms.CheckboxSelectMultiple)