from django.shortcuts import render
from django.views import View
from product import models as product_models
class Index(View):
    def get(self, request):
        args = {}
        args['products'] = product_models.Product.objects.all()
        return render(request,'home/index.html',args)

class Profile(View):
    def get(self, request):
        args = {}
        return render(request,'home/profile.html',args)
