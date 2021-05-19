from django.shortcuts import render
from django.views import View
from product import models as product_models
from django.contrib.auth.mixins import LoginRequiredMixin
from decimal import Decimal

class Index(View):
    def get(self, request):
        args = {}
        args['products'] = product_models.Product.objects.all()
        return render(request,'home/index.html',args)

class Profile(LoginRequiredMixin, View):
    def get(self, request):
        args = {}
        return render(request,'home/profile.html',args)

class Cart(View):
    def get(self, request):
        args = {}
        if request.user.is_authenticated:
            args['cart'] = product_models.Cart.objects.filter(user=request.user).first()
            if(args['cart']):
                args['cart_items'] = product_models.Entry.objects.filter(cart=args['cart']).select_related()
        return render(request,'home/cart.html',args)
