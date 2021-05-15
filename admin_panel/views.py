from django.shortcuts import render
from django.views import View
from django.contrib.auth import get_user_model
from product import models as products_model

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
        args['categories'] = []
        categories = products_model.Category.objects.all()
        for category in categories:     
            childs = products_model.Category_Parents.objects.all().filter(parent=category)
            if childs:
                childs_array=[]
                for child in childs:
                    childs_array.append(child.child)
                args['categories'].append({'category':category,'parents':childs_array})
            elif category not in childs_array:
                args['categories'].append({'category':category,'parents':0})
        return render(request,'admin_panel/categories.html',args)