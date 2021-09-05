from django.shortcuts import render

# Create your views here.
def home_screen_view(request):
    context = {}
    context['some_string'] = "this is some string that Im passing to the view"
    context['some_number'] =  141251

    return render(request, "personal/home.html", context)