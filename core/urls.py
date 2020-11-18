from django.urls import path

from core.views import home_page, cart

urlpatterns = [
    path('', home_page, name='home'),
    path('cart/', cart, name='cart page'),
]
