from django.urls import path,include
from account import views

app_name = 'account'

urlpatterns = [
   path('',views.Index.as_view() ,name='index'),
   path('profile',views.Profile.as_view() ,name='profile'),
]
