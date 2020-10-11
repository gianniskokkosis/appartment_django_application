from django.shortcuts import render
from django.http import HttpResponse
from .models import Appartment

def home(request):
    appartments = Appartment.objects.all()

    context = {
        'appartments': appartments
    }

    return render(request, 'appartments/home.html', context)


def details(request, pk):
    obj = Appartment.objects.get(id=pk)

    context = {
        'obj': obj
    }

    return render(request, 'appartments/details.html', context)

def purchase(request, pk):
    return render(request, 'appartments/purchase.html')