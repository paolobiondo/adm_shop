from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.db.models import Q
import json

from product import models as product_models

class Product(View):
    def post(self, request, id):
        args = {}
        product = get_object_or_404(product_models.Product, id=id)
        if(request.POST.get('unit')):
            quantity=request.POST.get('unit')
        else:
            quantity=1
        #check if the user has their cart
        if(product_models.Cart.objects.filter(user=request.user).exists()):
            user_cart = product_models.Cart.objects.get(user=request.user)
            if(product_models.Entry.objects.filter(Q(product=product, cart=user_cart)).exists()):
                args = {'success':'2'}
            else:  
                entry = product_models.Entry.objects.create(product=product, cart=user_cart, quantity=quantity)
                args = {'success':'1'}
        else:
            user_cart=product_models.Cart.objects.create(user=request.user)
            entry = product_models.Entry.objects.create(product=product, cart=user_cart, quantity=quantity)
            args = {'success':'1'}
        return HttpResponse(json.dumps(args))