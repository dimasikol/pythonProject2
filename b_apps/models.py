from django.db import models
from django.urls import reverse

class Category_news(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(null=True)
    image = models.ImageField('Изображение',upload_to='media/category_news_pic/%Y/%m/%d/')
    slug = models.SlugField(max_length=50)
    def __str__(self):
        return self.name
    # def get_absolute_url(self):
    #     return reverse('category_url',kwargs={'id':self.id,'name':self.name})
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class News_objects(models.Model):
    name = models.CharField(max_length=100)
    description =models.TextField(null=True)
    image = models.ImageField('Изображение',upload_to='media/news_objects/%Y/%m/%d/')
    slug = models.SlugField(max_length=50)
    category_news = models.ForeignKey(Category_news,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('news_objects_url', kwargs={'id': self.id, 'name': self.name})

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'

# Create your models here.
