from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.db.models import Q
import simplejson as json
from django.forms.models import model_to_dict

from product import models as product_models

class Product(View):
    def post(self, request, id):
        args = {}
        product = get_object_or_404(product_models.Product, id=id)
        if(product):
            if(request.POST.get('quantity')):
                quantity=request.POST.get('quantity')
            else:
                quantity=1
            if(request.POST.get('cookie_cart')):
                args['product'] = {'id':product.id,'name':product.name,'price':product.price,'discount_price':product.discount_price,'cover':str(product.cover)}
            else:
                #check if the user has their cart
                if(product_models.Cart.objects.filter(user=request.user).exists()):
                    user_cart = product_models.Cart.objects.get(user=request.user)
                    if(product_models.Entry.objects.filter(Q(product=product, cart=user_cart)).exists()):
                        args['success'] = 2
                    else:  
                        entry = product_models.Entry.objects.create(product=product, cart=user_cart, quantity=quantity)
                        args['success'] = 1
                else:
                    user_cart=product_models.Cart.objects.create(user=request.user)
                    entry = product_models.Entry.objects.create(product=product, cart=user_cart, quantity=quantity)
                    args['success'] = 1
        else:
            args['success'] = 0
        return HttpResponse(json.dumps(args))

class Cart(View):
    def post(self, request, id):
        args = {}
        entry = get_object_or_404(product_models.Entry, id=id)
        args['success'] = 1
        args['idEntry'] = id
        entry.delete()
        args['cart'] = product_models.Cart.objects.filter(user=request.user).values('total').first()
        return HttpResponse(json.dumps(args))