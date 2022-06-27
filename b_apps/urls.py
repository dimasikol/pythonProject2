from django.urls import path
from . import views
urlpatterns = [
    path('',views.test,name='test_view'),
    path('category_list/',views.test,name='category_url'),
    path('news_object/',views.test,name='news_objects_url'),

]
