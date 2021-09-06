from django.shortcuts import render

from account.models import Account

# Create your views here.
def home_screen_view(request):
    context = {}
    accounts = Account.objects.all().order_by('username')
    context['accounts'] = accounts
    print(accounts)
    return render(request, "personal/home.html", context)