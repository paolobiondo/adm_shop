from django.shortcuts import render
from django.views import View
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.shortcuts import get_object_or_404

from product import models as products_model
from product import tools as tools_products
from admin_panel import forms 

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
        args['product'] = get_object_or_404(products_model.Product,id=id)
        args['form'] = forms.EditProductForm()
        args['categories'] = products_model.Category.objects.all()
        return render(request,'admin_panel/editproduct.html', args)
        
    def post(self,request, id):
        args = {}
        args['categories'] = products_model.Category.objects.all()
        args['product'] = get_object_or_404(products_model.Product,id=id)
        product = args['product']

        args['form'] = forms.EditProductForm(request.POST)
        if args['form'].is_valid():
            product.name=args['form'].cleaned_data['title']
            product.description = args['form'].cleaned_data['description']
            product.price = args['form'].cleaned_data['price']
            if(args['form'].cleaned_data['discounted_price'] != "None"):
                product.discount_price = args['form'].cleaned_data['discounted_price']
            product.units = args['form'].cleaned_data['units']
            if(args['form'].cleaned_data['category'] != 0):
                product.category = args['form'].cleaned_data['category']
            else:
                product.category = ""

            product.save()

        args['success'] = 1
        return render(request,'admin_panel/editproduct.html', args)

class Categories(GroupRequiredMixin, View):
    group_required = "admin_panel"
    def get(self, request):
        args = {}
        args['categories']=tools_products.getCategories()
        return render(request,'admin_panel/categories.html',args)