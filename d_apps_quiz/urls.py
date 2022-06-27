from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('quiz/',views.ViewQuiz.as_view(),name='quiz'),
    path('quiz2/',views.ViewsQuiz.as_view(),name = 'quiz2'),
    #path('<int:pk>/',views.DetailQuiz.as_view(),name = 'quiz_detail'),
    path('<int:pk>/',views.DetailQuiz.as_view(),name = 'quiz_detail')
]
