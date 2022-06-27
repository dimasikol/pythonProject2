from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models

@admin.register(models.Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('name','id','url')
    list_display_links = ('name',)
    prepopulated_fields = {'url':('name',)}

@admin.register(models.Movie)
class AdminMovie(admin.ModelAdmin):
    list_display = ('id','title','url','draft','get_image') #выводит инфоррмацию в админке
    list_filter = ('category','genres','year','draft')    # фильтрация с боку
    list_editable = ('title','draft',) # чекбокс для черновиков
    search_fields = ('title','category__name')
    prepopulated_fields = {'url':('title',)}
    readonly_fields = ('get_image',)
    save_on_top = True  # значек сохнанения с верху
    save_as = True  # пересохранение в новый объект
    fieldsets = (
        ("Основные",{'fields':(('title','tagline','url',),)}),
        ("Текст",{'fields':(('description',),)}),
        ("Даты",{'fields':(('year','country','world_premiere','budget','fees_in_usa','fees_in_world'),)}),
        ("Состав",{'fields':(('actors','directors','genres'),)}),
        ("Доп информация",{'fields':(('poster','draft','get_image'),)}),)

    def get_image(self,obj):
        return mark_safe(f'<img src="{obj.poster.url}" width="55" height="60">')
    get_image.short_description = 'изображение'

@admin.register(models.Actor)
class AdminActor(admin.ModelAdmin):
    list_display = ('id','name','age','get_image')
    list_editable = ('name','age',)
    readonly_fields = ('get_image',)
    def get_image(self,obj):
        return mark_safe(f'<img src="{obj.image.url}" width="50" height="66">')
    get_image.short_description = 'фото'

@admin.register(models.Genre)
class AdminGenre(admin.ModelAdmin):
    list_display = ('name','description',)
    prepopulated_fields = {'url':('name',)}


admin.site.register(models.MovieShots)
admin.site.register(models.Rating)
admin.site.register(models.RattingStar)
admin.site.register(models.Reviews)