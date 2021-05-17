from django.urls import path,include
from home import views

app_name = 'home'

urlpatterns = [
   path('',views.Index.as_view() ,name='index'),
   path('profile',views.Profile.as_view(), name='profile'),
   path('cart',views.Cart.as_view(),name='cart')
]
