from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('name','get_some_image',)
    prepopulated_fields = {'url': ('name',)}
    def get_some_image(self,obj):
        return mark_safe(f'<img src = "{obj.image.url}" width="50" height = "40">')
    get_some_image.short_description = 'фото'

@admin.register(Items)
class AdminItem(admin.ModelAdmin):
    list_display = ('name', 'get_some_image',)
    prepopulated_fields = {'url': ('name',)}
    def get_some_image(self, obj):
        return mark_safe(f'<img src = "{obj.image.url}" width="50" height = "40">')

    get_some_image.short_description = 'фото'
