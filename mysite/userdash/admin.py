from django.contrib import admin

from .models import Survey, QuestionsGroup, Question
# Register your models here.

admin.site.register([Survey, QuestionsGroup, Question])