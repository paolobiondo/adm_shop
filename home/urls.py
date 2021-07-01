from django.urls import path,include
from home import views

app_name = 'home'

urlpatterns = [
   path('',views.Index.as_view() ,name='index'),
   path('profile',views.Profile.as_view(), name='profile'),
   path('cart',views.Cart.as_view(),name='cart'),
   path('checkout',views.Checkout.as_view(), name='checkout'),
   path('orders',views.Orders.as_view(), name="orders")
]
