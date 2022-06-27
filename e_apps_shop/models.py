from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=255,unique=True)
    image = models.ImageField(verbose_name='Изображение',upload_to='uploads/shop/category/%Y/%m/%d/',null=True)
    url = models.SlugField(verbose_name='ссылка',max_length=300)
    description = RichTextUploadingField(verbose_name='описание')
    def __str__(self):
        return self.name


class Items(models.Model):
    name = models.CharField(max_length=255)
    url = models.SlugField(max_length=300)
    image = models.ImageField(upload_to='uploads/shop/items/%Y/%m/%d/',null=True)
    description = RichTextUploadingField(verbose_name='описание')
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    def get_absolute_url(self):
        return reverse('items',kwargs=self.kwargs['pk'])
    def save(self,*args,**kwargs):
        if not(self.url):
            self.url = slugify(self.name)
        return super().save(*args,**kwargs)