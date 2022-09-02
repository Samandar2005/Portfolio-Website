from .models import *
from django.db.models import *
from django.contrib.auth import *
from django.contrib.auth import login
from unicodedata import *
from django.shortcuts import render


# Create your views here.


def index(request):
    my = My.objects.all()
    myhistory = MyHistory.objects.all()
    mywork = MyWork.objects.all()
    mygoals = MyGoals.objects.all()
    cooperation = Cooperation.objects.all()
    context = {'my': my, 'myhistory': myhistory, 'mywork': mywork,
               'mygoals': mygoals, 'cooperation': cooperation}
    return render(request, "index.html", context=context)
