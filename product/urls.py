from django.urls import path,include
from product import views

app_name = 'product'

urlpatterns = [
   path('<int:id>', views.Product.as_view() ,name='product'),
   path('cart/<int:id>', views.Cart.as_view(), name='cart'),
   path('entry/',views.Entry.as_view(), name='entry'),
]
