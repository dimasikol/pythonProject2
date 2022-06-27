from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Quiz

class ViewQuiz(ListView):
    model = Quiz
    template_name = 'd_apps_quiz/shabons/quiz.html'
    context_object_name = 'object_list'


class DetailQuiz(DetailView):
    model = Quiz
    slug_field = 'url'
    template_name = 'd_apps_quiz/shabons/detail_quiz.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        self.kwargs['tigrito']='димасия'
        print(self.kwargs.items())
        return super().get_context_data(**kwargs)


class ViewsQuiz(ListView):
    model = Quiz
    template_name = 'd_apps_quiz/shabons/quiz2.html'

