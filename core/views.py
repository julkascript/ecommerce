from django.shortcuts import render


def home_page(request):
    return render(request, 'home-page.html')


def cart(request):
    return render(request, 'cart.html')
