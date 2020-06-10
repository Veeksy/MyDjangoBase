from django.http import HttpResponse
from django.shortcuts import render
from Shop.models import *
from Shop.forms import ShopsForm
from streets.models import *
import json
import datetime


def ViewShops(request):
    global Status
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
            street = Streets.objects.get(id=d['street'])
            shops.street = street
            shops.house = d['house']
            shops.time_to_open = d['time_to_open']
            shops.time_to_close = d['time_to_close']
            Shop.save(shops)
            return HttpResponse("<h2>Была создана запись {0}</h2>".format(shops.id))
    TimeNow = datetime.datetime.now().time()
    if 'search' in request.GET:
        if shopform.is_valid():
            if shopform.cleaned_data["street"]:
                shops = shops.filter(street__name=shopform.cleaned_data["street"])
            if shopform.cleaned_data["city"]:
                shops = shops.filter(street__city__name=shopform.cleaned_data["city"])
            if shopform.cleaned_data["status"]:
                if shopform.cleaned_data["status"] == '1':
                    shops = shops.filter(time_to_open__lt=TimeNow, time_to_close__gt=TimeNow)
                if shopform.cleaned_data["status"] == '0':
                    shops = shops.filter(time_to_open__lt=TimeNow, time_to_close__lt=TimeNow)
    return render(request, 'MainApp/shops.html', {"shops": shops, "ShopForm": shopform, "servtime": TimeNow})
