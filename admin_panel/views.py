from django.shortcuts import render
from django.views import View
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from product import models as products_model
from product import tools as tools_products

class Index(GroupRequiredMixin, View):
    group_required = "admin_panel"
    def get(self, request):
        args = {}
        return render(request,'admin_panel/index.html',args)

class Users(GroupRequiredMixin, View):
    group_required = "admin_panel"
    def get(self, request):
        args = {}
        User = get_user_model()
        args['users'] = User.objects.all()
        return render(request, 'admin_panel/users.html', args)

class Products(GroupRequiredMixin, View):
    group_required = "admin_panel"
    def get(self, request):
        args = {}
        args['products'] = products_model.Product.objects.all()
        return render(request,'admin_panel/products.html',args)

class EditProduct(GroupRequiredMixin, View):
    group_required = "admin_panel"
    def get(self,request,id):
        args = {}
        args['product'] = products_model.Product.objects.filter(id=id).first()
        return render(request,'admin_panel/editproduct.html', args)
        
    def post(self,request, id):
        args = {}
        args['product'] = products_model.Product.objects.filter(id=id).first()
        return render(request,'admin_panel/editproduct.html', args)

class Categories(GroupRequiredMixin, View):
    group_required = "admin_panel"
    def get(self, request):
        args = {}
        args['categories']=tools_products.getCategories()
        return render(request,'admin_panel/categories.html',args)