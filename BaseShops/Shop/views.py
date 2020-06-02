from django.http import HttpResponse
from django.shortcuts import render
from Shop.models import *
from Shop.forms import *


def ViewShops(request):
    shops = Shop.objects.all()
    return render(request, 'MainApp/shops.html', {"shops": shops})


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        return HttpResponse("<h2>Hello, {0}</h2>".format(name))
    else:
        shopform = ShopsForm()
        return render(request, "shops.html", {"ShopForm": shopform})