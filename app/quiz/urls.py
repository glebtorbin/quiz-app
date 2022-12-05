from . import views

from django.urls import path

app_name = 'quiz'

urlpatterns = [
    path('', views.index, name='index'),
]