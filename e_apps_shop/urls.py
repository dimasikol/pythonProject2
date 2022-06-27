from django.urls import path
from . import views
urlpatterns = [
    path('',views.HomePage.as_view()),
    path('category/',views.ViewCategory.as_view()),
    path('category/<int:pk>/',views.ViewItem.as_view(),name='items'),
]
