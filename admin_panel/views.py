from django.shortcuts import render
from django.views import View
from django.contrib.auth import get_user_model

class Index(View):
    def get(self, request):
        args = {}
        return render(request,'admin_panel/index.html',args)

class Users(View):
    def get(self, request):
        args = {}
        User = get_user_model()
        args['users'] = User.objects.all()
        return render(request, 'admin_panel/users.html', args)