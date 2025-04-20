# store/urls.py

from django.urls import path
from .views import register, user_login, user_logout
from .views import home, search, shop, add_to_cart, cart_view, remove_from_cart

urlpatterns = [
    path('', home, name='home'),  
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('search/', search, name='search'),
    path('shop/', shop, name='shop'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
     path('cart/', cart_view, name='cart'),
     path('remove_from_cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
]

