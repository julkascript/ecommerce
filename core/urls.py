from django.urls import path

from core.views import home_page, cart, about, sign_in, sign_up

urlpatterns = [
    path('', home_page, name='home'),
    path('cart/', cart, name='cart page'),
    path('about/', about, name='about page'),
    path('signin/', sign_in, name='sign in'),
    path('signup/', sign_up, name='sign up'),
]
