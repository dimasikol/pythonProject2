from django.shortcuts import render
from django.views import View,generic
from .models import Category,Items
from c_apps_kinopoisk.models import Movie
class HomePage(View):
    def get(self,request):
        print(type(request.user))
        if str(request.user) in ['admin','dimas','olesik']:
            context = {'one': [1,2,3,4,5,6,7,8,9,20],'two':request.user,'movie_list':Movie.objects.all()}
        elif str(request.user) == 'AnonymousUser':
            context = {'one': [22, 23, 24, 25, 27, 26, 28], 'two': 'братик? ты не зареган?" не надо так!','movie_list':Movie.objects.all()}
        else:
            context = {'one':Items.objects.all(),'two':request.user,'movie_list':Movie.objects.all()}
        return render(request,template_name='e_apps_shop/shablons/home.html',context=context)

class ViewCategory(generic.ListView):
    template_name = 'e_apps_shop/shablons/category_list.html'
    model = Category
    context_object_name = 'object_list'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['count_element'] = 5
        return context

class ViewItem(generic.DetailView):
    template_name = 'e_apps_shop/shablons/viewitem_detail.html'
    model = Items
    context_object_name = 'object'
