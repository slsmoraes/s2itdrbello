from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return render(request, 'index.html')

def articles(request, year):
    return HttpResponse('O ano enviado foi:' + str(year))
