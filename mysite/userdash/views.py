from django.shortcuts import render
from django.http import HttpResponse
from .models import Survey, QuestionsGroup
from django.template import loader
# Create your views here.


def index(request):
    template = loader.get_template("monitor-client/examples/index.html")
    context = {

    }
    return HttpResponse(template.render(context, request))


def get_survey(request, name):
    survey = Survey.objects.get(name=name)
    return HttpResponse("<h1>"+str(survey.questionsgroup_set.all()[0])+"</h1>")


