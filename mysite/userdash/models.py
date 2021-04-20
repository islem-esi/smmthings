from django.db import models

# Create your models here.


class Survey(models.Model):
    name = models.CharField(max_length=200)
    c_date = models.DateTimeField('data created')

    def __str__(self):
        return self.name


class QuestionsGroup(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    group_label = models.CharField(max_length=200)

    def __str__(self):
        return self.group_label

class Question(models.Model):
    group = models.ForeignKey(QuestionsGroup, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=500)

    def __str__(self):
        return self.question_text
