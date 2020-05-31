from django.shortcuts import render
from Shop.models import *


def ViewShops(request):
    shops = Shop.objects.all()
    return render(request, 'MainApp/shops.html', {"shops": shops})
