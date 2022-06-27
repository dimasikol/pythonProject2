from datetime import date
from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.utils.text import slugify
class Category(models.Model):
    name = models.CharField('категория' ,max_length=150)
    description = RichTextUploadingField('описание')
    url = models.SlugField(max_length=160,unique=True)
    def __str__(self):
        return self.name
    def save(self,*args,**kwargs):
        if not self.url:
            self.url=slugify(self.name)
        return super().save(*args,**kwargs)
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural ='Категории'
class Actor(models.Model):
    name = models.CharField('имя',max_length=100)
    surname = models.CharField('фамилия',max_length=100)
    age = models.PositiveSmallIntegerField('возраст',default=0)
    description = RichTextUploadingField('описание')
    image = models.ImageField('изображение актера', upload_to='media/c_apps_kinopoisk/actors/%Y/%m/%d/')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Актер'
        verbose_name_plural ='Актеры'
class Genre(models.Model):
    name = models.CharField('жанр', max_length=150)
    description = RichTextUploadingField('описание')
    url = models.SlugField(max_length=160, unique=True)
    class Meta:
        verbose_name = 'Жанры'
        verbose_name_plural ='Жанры'
    def __str__(self):
        return self.name
    def save(self,*args,**kwargs):
        if not self.url:
            self.url=slugify(self.name)
        return self.url
class Movie(models.Model):
    title = models.CharField('название',max_length=150)
    tagline = models.CharField('слоган',max_length=150,default='')
    description = RichTextUploadingField('описание')
    poster = models.ImageField('poster', upload_to='media/c_apps_kinopoisk/posters/%Y/%m/%d/')
    year = models.PositiveSmallIntegerField('дата выхода',default=2022)
    country = models.CharField('страна',max_length=30)
    directors = models.ManyToManyField(Actor,verbose_name='режисер',related_name='film_director')
    actors = models.ManyToManyField(Actor,verbose_name='актер',related_name='film_actor')
    genres = models.ManyToManyField(Genre,verbose_name='жанр')
    world_premiere = models.DateField('премьера в мире',default=date.today)
    budget = models.PositiveIntegerField('бюджет',default=0)
    fees_in_usa = models.PositiveIntegerField('сборы в США',default=0)
    fees_in_world = models.PositiveIntegerField('сборы в мире',default=0)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    url = models.SlugField(max_length=160,unique=True)
    draft = models.BooleanField('черновик',default=False)
    def __str__(self):
        return self.title
    def save(self,*args,**kwargs):
        if not self.url:
            self.url=slugify(self.title)
        return super().save(*args,**kwargs)
    def get_absolute_url(self):
        return reverse('movie_detail',kwargs={'slug':self.url })
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural ='Фильмы'
        ordering = ['-country']
class MovieShots(models.Model):
    title = models.CharField('заголовки',max_length=150)
    description = RichTextUploadingField('описание')
    image = models.ImageField('изображение', upload_to='media/c_apps_kinopoisk/posters/%Y/%m/%d/')
    movie = models.ForeignKey(Movie,verbose_name='фильм',on_delete=models.CASCADE)
    def __str__(self):
        return self.movie.title
    class Meta:
        verbose_name = 'Фрагмент'
        verbose_name_plural ='Фрагменты'
class RattingStar(models.Model):
    value = models.PositiveSmallIntegerField('значение',default=0)
    class Meta:
        verbose_name = 'Рейтинг звезд'
        verbose_name_plural ='Рейтинг звезд'
class Rating(models.Model):
    ip = models.CharField('ip адресс',max_length=15)
    star = models.ForeignKey(RattingStar,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural ='Рейтинг'
class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=150)
    text = RichTextUploadingField()
    parent = models.ForeignKey('self',on_delete=models.SET_NULL,null=True, blank=True)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    def __str__(self):
        return self.movie.title
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural ='Отзывы'