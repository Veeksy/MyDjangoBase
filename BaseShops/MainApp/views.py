from django.shortcuts import render


def Main(request) -> render:
    return render(request, 'MainApp/Main.html')
