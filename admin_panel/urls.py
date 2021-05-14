from django.urls import path,include
from admin_panel import views

app_name = 'admin_panel'

urlpatterns = [
   path('',views.Index.as_view() ,name='index'),
   path('users',views.Users.as_view(), name='users')
]
