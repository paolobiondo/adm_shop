from django.shortcuts import render
from django.views import View

class Index(View):
    def get(self, request):
        args = {}
        return render(request,'account/index.html',args)

class Profile(View):
    def get(self,request):
        args = {}
        return render(request,'account/profile.html',args)