from django.shortcuts import render
from django.views import View
from product import models as product_models
from django.contrib.auth.mixins import LoginRequiredMixin

class Index(View):
    def get(self, request):
        args = {}
        args['products'] = product_models.Product.objects.all()
        return render(request,'home/index.html',args)

class Profile(LoginRequiredMixin, View):
    def get(self, request):
        args = {}
        return render(request,'home/profile.html',args)
