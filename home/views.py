from django.shortcuts import render
from django.views import View
from product import models as product_models
from django.contrib.auth.mixins import LoginRequiredMixin
from decimal import Decimal

from product.models import UserAddress
from home.forms import UserAddressForm

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
                args['cart_items'] = product_models.EntryCart.objects.filter(cart=args['cart']).select_related()
        return render(request,'home/cart.html',args)

class Checkout(LoginRequiredMixin, View):
    def get(self, request):
        args = {}
        args['form'] = UserAddressForm()

        cart_user = product_models.Cart.objects.filter(user = request.user).first()
        args['cart'] = cart_user
        products = product_models.EntryCart.objects.filter(cart = cart_user).select_related('product')
        args["products"] = []
        for product in products:
            total = product.quantity*product.product.price
            args["products"].append({'entry':product,'total':total})
        return render(request,'home/checkout.html',args)
    
    def post(self,request):
        args = {}
        address_form = UserAddressForm(request.POST)
        if address_form.is_valid():
            user_address = UserAddress()
            user_address.user = request.user
            user_address.country = address_form.cleaned_data['country']
            user_address.name = address_form.cleaned_data['name']
            user_address.surname = address_form.cleaned_data['surname']
            user_address.address = address_form.cleaned_data['address']
            user_address.city = address_form.cleaned_data['city']
            user_address.zip_address = address_form.cleaned_data['zip_address']
            user_address.telephone = address_form.cleaned_data['telephone']
            user_address.save()
            if(request.POST['same_address']=="on"):
                user_address_billing = UserAddress()
                user_address_billing.user = request.user
                user_address_billing.country = address_form.cleaned_data['country']
                user_address_billing.name = address_form.cleaned_data['name']
                user_address_billing.surname = address_form.cleaned_data['surname']
                user_address_billing.address = address_form.cleaned_data['address']
                user_address_billing.city = address_form.cleaned_data['city']
                user_address_billing.zip_address = address_form.cleaned_data['zip_address']
                user_address_billing.telephone = address_form.cleaned_data['telephone']
                user_address_billing.type="billing"
                user_address_billing.save()
            args['success'] = 1
        else:
            args['success'] = 2

        return render(request,'home/checkout.html', args)