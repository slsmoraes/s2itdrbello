from django.shortcuts import render
from django.http import HttpResponse

def cadmediuns(request):
    return render(request, 'cadmediuns.html')

def articles(request, year):
    return HttpResponse('O ano enviado foi:' + str(year))
