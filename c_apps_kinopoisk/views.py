from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView,DetailView
from django.views.generic.base import View

from .form import ReviewForm
from .models import Movie,Actor
class MovieView(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = 'c_apps_kinopoisk/base_temp/movie_list.html'
    context_object_name = 'movie_list'
class MovieDetailView(DetailView):
    model = Movie
    slug_field = 'url' #
    template_name = 'c_apps_kinopoisk/base_temp/movie_detail.html'
    context_object_name = 'movie_list'
class MovieViewfilter(View):
    def get(self,request):
        movies = Movie.objects.filter(genres=self.kwargs['id'])
        return render(request,'c_apps_kinopoisk/base_temp/movie_list.html',context={'movie_list':movies})
class AddReview(View):
    """отзывы"""
    def post(self,request,pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form=form.save(commit=False)
            form.movie_id = pk
            form.movie=movie
            form.save()
        return redirect(movie.get_absolute_url())
def tests(request):
    return render(request,template_name='c_apps_kinopoisk/test.html')
class Test(View):
    def get(self,request, *args,**kwargs):
        print(request.user.last_login)
        obj=Movie.objects.filter(country=self.kwargs['slug'])
        return render(request,template_name='test.html',context={'object_list':obj})
class Info(ListView):
    model = Movie
    template_name = 'Info.html'
    context_object_name = 'object_lisr'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dim'] = [1,2,3,4,5,6]
        return context