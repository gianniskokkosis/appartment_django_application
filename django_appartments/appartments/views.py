from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Appartment, Purchase

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
    app_obj = Appartment.objects.get(id=pk)
    if request.method == 'POST':
        firstname = request.POST.get('name', '')
        surname = request.POST.get('surname', '')
        email = request.POST.get('email', '')
        cvv = request.POST.get('cvv', '')
        iban = request.POST.get('iban', '')
        card_type = request.POST.get('card_type', '')
        address = request.POST.get('address', '')
        country = request.POST.get('country', '')
        city = request.POST.get('city', '')
        postal_code = request.POST.get('postal', '')
        Purchase.objects.create(name=firstname, surname=surname, email=email,
                                  cvv=cvv, iban=iban, card_type=card_type,
                                  address=address, country=country, city=city,
                                  postal_code=postal_code, appartment=app_obj)
        return HttpResponseRedirect('/')
    return render(request, 'appartments/purchase.html')


def my_purchases(request):
    data = Purchase.objects.all()

    context = {
        'purchases': data
    }

    return render(request, 'appartments/my_purchases.html', context)