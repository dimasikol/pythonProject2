from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('tm/',views.Info.as_view(),name='tigr'),
    path('<slug:slug>/ts/',views.Test.as_view(),name='test_class'),#testviewclass
    path('',views.MovieView.as_view(),name='test_view'),#testViewDef
    path('<slug:slug>/',views.MovieDetailView.as_view(),name='movie_detail'),
    path('review/<int:pk>/',views.AddReview.as_view(),name='add_review'),
    path('<int:id>/',views.MovieViewfilter.as_view(),name='movie_view_filter'),
]
