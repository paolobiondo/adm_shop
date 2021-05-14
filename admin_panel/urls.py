from django.urls import path,include
from admin_panel import views

app_name = 'admin_panel'

urlpatterns = [
   path('',views.Index.as_view() ,name='index'),
   path('profile',views.Profile.as_view() ,name='profile'),
]
