from django.shortcuts import render


def home_page(request):
    return render(request, 'home-page.html')


def cart(request):
    return render(request, 'cart.html')


def about(request):
    return render(request, 'about-page.html')


def sign_in(request):
    return render(request, 'sign-in-page.html')


def sign_up(request):
    return render(request, 'sign-up-page.html')
