from personal.models import Question
from django.shortcuts import render

# Create your views here.
def home_screen_view(request):
    context = {}
    #context['some_string'] = "this is some string that Im passing to the view"
    #context['some_number'] =  141251

    #context = {
    #       'some_string': "this is some string that Im passing to the view",
    #       'some_number': 123456,
    #}

    #list_of_values = []
    #list_of_values.append("first entry")
    #list_of_values.append("second entry")
    #list_of_values.append("third entry")
    #list_of_values.append("fourth entry")
    #context['list_of_values'] = list_of_values

    questions = Question.objects.all()
    context['questions'] = questions

    return render(request, "personal/home.html", context)