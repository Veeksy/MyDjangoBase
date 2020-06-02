from django.http import HttpResponse
from django.shortcuts import render
from Shop.models import *
from Shop.forms import ShopsForm
from streets.models import *
import json


def ViewShops(request):
    shops = Shop.objects.all()
    shopform = ShopsForm(request.GET)
    count = Shop.objects.all().count()
    with open('Shop/NewShop.json') as f:
        d = json.load(f)
    if request.POST:
        if 'add' in request.POST:
            shops = Shop()
            shops.id = count+1
            shops.name = d['name']
            shops.street = d['street']
            shops.house = d['house']
            shops.time_to_open = d['time_to_open']
            shops.time_to_close = d['time_to_close']
            Shop.save(shops)
            return HttpResponse(shops.id)
    if 'search' in request.GET:
        if shopform.is_valid():
            if shopform.cleaned_data["street"]:
                shops = shops.filter(street=shopform.cleaned_data["street"])
    return render(request, 'MainApp/shops.html', {"shops": shops, "ShopForm": shopform})


