from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.db.models import Q
import simplejson as json
from django.forms.models import model_to_dict
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from product import tools as tools_product

from product import tools
from product import models as product_models
import product

class Product(LoginRequiredMixin, View):
    def post(self, request, id):
        args = {}
        product = get_object_or_404(product_models.Product, id=id)
        if(product):
            if(request.POST.get('cookie_cart')):
                args['product'] = {'id':product.id,'name':product.name,'price':product.price,'discount_price':product.discount_price,'cover':str(product.cover)}
            else:
                if(request.POST.get('quantity')):
                    quantity=request.POST.get('quantity')
                else:
                    quantity=1
                user_cart = product_models.Cart.objects.get(user=request.user)
                if(product_models.Entry.objects.filter(Q(product=product, cart=user_cart)).exists()):
                    args['success'] = 2
                else:  
                    entry = product_models.Entry.objects.create(product=product, cart=user_cart, quantity=quantity)
                    args['success'] = 1
        else:
            args['success'] = 0
        return HttpResponse(json.dumps(args))

class DeleteEntry(View):
    def get(self, request):
        return HttpResponseRedirect(reverse('home:cart'))

    # Delete Entry
    def post(self, request, id):
        args = {}
        entry = get_object_or_404(product_models.Entry, id=id)
        args['success'] = 1
        args['idEntry'] = id
        args['quantity'] = entry.quantity
        entry.delete()
        args['cart'] = product_models.Cart.objects.filter(user=request.user).values('total').first()
        return HttpResponse(json.dumps(args))

class UpdateCart(View):
    def get(self, request):
        return HttpResponseRedirect(reverse('home:cart'))

    def post(self, request):
        args = {}
        user_cart = product_models.Cart.objects.filter(user=request.user).first()
        entries = product_models.Entry.objects.filter(cart=user_cart)
        for entry in entries:
            quantity_edited = request.POST.get("quantity_"+str(entry.id))
            if quantity_edited.isnumeric() and int(quantity_edited) != 0:
                quantity_difference = int(quantity_edited) - entry.quantity
                product_models.Entry.objects.filter(id=int(entry.id)).update(quantity=int(quantity_edited))
                tools_product.updateCart(entry,quantity_difference)

        return HttpResponseRedirect(reverse('home:cart'))

class Entry(View):
    def get(self, request):
        return HttpResponseRedirect(reverse('home:cart'))

    def post(self, request):
        args = {}
        products = request.POST.get('products').split(',')
        user_cart = product_models.Cart.objects.filter(user=request.user).first()
        for product in products:
            idProduct = product.split('|')[0][1:]
            quantity = product .split('|')[1][:-1]
            objProduct = product_models.Product.objects.filter(id=idProduct).first()
            entry = product_models.Entry.objects.create(product=objProduct, cart=user_cart, quantity=quantity)
        args['success'] = 1
        return HttpResponse(json.dumps(args))