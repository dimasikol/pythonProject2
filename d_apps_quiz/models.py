from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField('Название категории',max_length=255)
    image = models.ImageField('минифото категории',upload_to='uploads/quiz_category/%Y/%m/%d/',null=True)
    def __str__(self):
        return self.name
    # class Meta:
    #     verbose_name = 'Категория вопросов'
    #     verbose_name_plural = "Категории вопросов"
    #
class Quiz(models.Model):
    title = models.CharField('Название',max_length=255)
    image = models.ImageField(verbose_name='Изображение',upload_to='uploads/quiz/%Y/%m/%d/',null=True)
    description = RichTextUploadingField('Вопрос')
    url = models.SlugField(max_length=300,unique=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.title
    def save(self,*args,**kwargs):
        if not self.url:
            self.url = slugify(self.title)
        return super().save(*args,**kwargs)
    def get_absolute_url(self):
        return reverse('quiz',kwargs=self.kwargs['url'])
    # class Meta:
    #     verbose_name = 'Вопрос'
    #     verbose_name_plural = "Вопросы"
class Answer(models.Model):
    answer = models.CharField('Правильный ответ',max_length=1000)
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    def __str__(self):
        return self.answer
    # class Meta:
    #     verbose_name = 'Правильный ответ'
    #     verbose_plural = "Правильные ответы"
class FalseAnswer(models.Model):
    answer = models.CharField('Неправильный ответ',max_length=1000)
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    def __str__(self):
        return self.answer
    # class Meta:
    #     verbose_name = "Не правильный ответ"
    #     verbose_name_plural = "Не правильные ответы"
class TypeAnsOpenAnswer(models.Model):
    pass
class TypeAnsRatioAnswer(models.Model):
    pass
class TypeAnsCheckBoxAnswer(models.Model):
    pass
class TypeAnsTextArea(models.Model):
    pass