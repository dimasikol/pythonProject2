from django.contrib import admin
from .models import Quiz,Category,Answer,FalseAnswer

class AnswerAd(admin.StackedInline):
    model = Answer
    extra = 1

class FalseAnswerAd(admin.StackedInline):
    model = FalseAnswer
    extra = 1

@admin.register(Quiz)
class AdminQuiz(admin.ModelAdmin):
    list_display = ('title','description',)
    inlines = [AnswerAd,FalseAnswerAd]

admin.site.register(Category)
admin.site.register(Answer)
admin.site.register(FalseAnswer)


# Register your models here.
