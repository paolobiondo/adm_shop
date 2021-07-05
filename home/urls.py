from django.urls import path,include
from home import views

app_name = 'home'

urlpatterns = [
   path('',views.Index.as_view() ,name='index'),
   path('profile',views.Profile.as_view(), name='profile'),
   path('cart',views.Cart.as_view(),name='cart'),
   path('checkout',views.Checkout.as_view(), name='checkout'),
   path('orders',views.Orders.as_view(), name="orders"),
   path('order/<int:id>',views.Order.as_view(), name="order"),

   #payment
   path('payment/<int:id>',views.Payment.as_view(), name="payment"),
   path('success/<int:id>',views.Success.as_view(), name="success"),
   path('cancelled/',views.Cancelled.as_view(), name="cancelled"),
   path('config/', views.stripe_config), 
   path('create-checkout-session/<int:id>', views.create_checkout_session), 
   path('stripe_webhook/', views.stripe_webhook),
]
