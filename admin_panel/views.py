from django.shortcuts import render
from django.views import View
from django.contrib.auth import get_user_model
from product import models as products_model
from product import tools as tools_products

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

class Products(View):
    def get(self, request):
        args = {}
        args['products'] = products_model.Product.objects.all()
        return render(request,'admin_panel/products.html',args)

class Categories(View):
    def get(self, request):
        args = {}
        args['categories']=tools_products.getCategories()
        return render(request,'admin_panel/categories.html',args)