from django.urls import path,include
from product import views

app_name = 'product'

urlpatterns = [
   path('<int:id>', views.Product.as_view() ,name='product'),
   path('delete_entry/<int:id>', views.DeleteEntry.as_view(), name='delete_entry'),
   path('entry',views.Entry.as_view(), name='entry'),
   path('update_cart', views.UpdateCart.as_view(), name="update_cart")
]
