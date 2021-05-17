from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
import json

from product import models as product_models

class Product(View):
    def post(self, request, id):
        args = {}

        product = get_object_or_404(product_models.Product, id=id)
        #check if the user has their cart
        if(product_models.Cart.objects.filter(user=request.user).exists()):
            user_cart = product_models.Cart.objects.get(user=request.user)
            entry = product_models.Entry.objects.create(product=product, cart=user_cart, quantity=int(request.POST.get('unit')))
            args = {'success':'1'}
        else:
            user_cart=product_models.Cart.objects.create(user=request.user)
            entry = product_models.Entry.objects.create(product=product, cart=user_cart, quantity=int(request.POST.get('unit')))
            args = {'success':'1'}
        return HttpResponse(json.dumps(args))