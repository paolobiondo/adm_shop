from django.urls import path,include
from admin_panel import views

app_name = 'admin_panel'

urlpatterns = [
   path('',views.Index.as_view() ,name='index'),
   path('users',views.Users.as_view(), name='users'),
   path('products', views.Products.as_view() ,name='products'),
   path('categories', views.Categories.as_view() ,name='categories'),
   path('editproduct/<int:id>', views.EditProduct.as_view(), name='editproduct')
]
