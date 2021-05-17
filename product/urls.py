from django.urls import path,include
from product import views

app_name = 'product'

urlpatterns = [
   path('<int:id>', views.Product.as_view() ,name='product'),
]
