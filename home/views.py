from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from decimal import Decimal
from django.db.models import Q
import stripe
from django.http.response import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.urls import reverse

from admin_panel.models import UserAddress
from home.forms import UserAddressForm, UserAddressShippingForm
from product import models as product_models
from admin_panel.models import Setting

class Index(View):
    def get(self, request):
        args = {}
        args['products'] = product_models.Product.objects.all()
        return render(request,'home/index.html',args)

class Profile(LoginRequiredMixin, View):
    def get(self, request):
        args = {}
        return render(request,'home/profile.html',args)

class Orders(LoginRequiredMixin, View):
    def get(self, request):
        args = {}
        args['orders'] = product_models.Order.objects.filter(user=request.user).order_by('-timestamp')
        return render(request,'home/orders.html',args)

class Order(LoginRequiredMixin, View):
    def get(self, request, id):
        args = {}
        order = product_models.Order.objects.filter(id=id).first()
        args['order'] = order
        args['orderProducts'] = product_models.EntryOrder.objects.filter(order=order.id).select_related('product')
        return render(request,'home/order.html',args)

class Settings(LoginRequiredMixin, View):
    def get(self, request):
        args = {}

        return render(request,'home/settings.html',args)

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
        args['form_shipping'] = UserAddressShippingForm()

        args['shippingAddress'] = UserAddress.objects.filter(Q(user=request.user,type="shipping")).first()
        args['billingAddress'] = UserAddress.objects.filter(Q(user=request.user,type="billing")).first()
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
        args['form'] = UserAddressForm(request.POST)
        args['form_shipping'] = UserAddressShippingForm(request.POST)

        cart_user = product_models.Cart.objects.filter(user = request.user).first()
        products = product_models.EntryCart.objects.filter(cart = cart_user).select_related('product')
        args["products"] = []
        for product in products:
            total = product.quantity*product.product.price
            args["products"].append({'entry':product,'total':total})

        if args['form'].is_valid() and args['form_shipping'].is_valid():
            #check if billing shipping address exists
            if(UserAddress.objects.filter(Q(user=request.user, type="billing")).exists()):
                user_address = UserAddress.objects.filter(Q(user=request.user, type="billing")).first()
            else:
                user_address = UserAddress()
                user_address.user = request.user

            user_address.country = args['form'].cleaned_data['country']
            user_address.name = args['form'].cleaned_data['name']
            user_address.surname = args['form'].cleaned_data['surname']
            user_address.address = args['form'].cleaned_data['address']
            user_address.city = args['form'].cleaned_data['city']
            user_address.zip_address = args['form'].cleaned_data['zip_address']
            user_address.telephone = args['form'].cleaned_data['telephone']
            user_address.instruction = args['form'].cleaned_data['instruction']
            user_address.type="billing"
            user_address.save()

            if(request.POST.get('same_address')=="on"):
                if(UserAddress.objects.filter(Q(user=request.user, type="shipping")).exists()):
                    user_address_shipping = UserAddress.objects.filter(Q(user=request.user, type="shipping")).first()
                else:
                    user_address_shipping = UserAddress()
                    user_address_shipping.user = request.user

                user_address_shipping.country = args['form'].cleaned_data['country']
                user_address_shipping.name = args['form'].cleaned_data['name']
                user_address_shipping.surname = args['form'].cleaned_data['surname']
                user_address_shipping.address = args['form'].cleaned_data['address']
                user_address_shipping.city = args['form'].cleaned_data['city']
                user_address_shipping.zip_address = args['form'].cleaned_data['zip_address']
                user_address_shipping.telephone = args['form'].cleaned_data['telephone']
                user_address_shipping.instruction = args['form'].cleaned_data['instruction']
                user_address_shipping.save()
            else:
                if(UserAddress.objects.filter(Q(user=request.user, type="shipping")).exists()):
                    user_address_shipping = UserAddress.objects.filter(Q(user=request.user, type="shipping")).first()
                else:
                    user_address_shipping = UserAddress()
                    user_address_shipping.user = request.user

                user_address_shipping.country = args['form_shipping'].cleaned_data['country_shipping']
                user_address_shipping.name = args['form_shipping'].cleaned_data['name_shipping']
                user_address_shipping.surname = args['form_shipping'].cleaned_data['surname_shipping']
                user_address_shipping.address = args['form_shipping'].cleaned_data['address_shipping']
                user_address_shipping.city = args['form_shipping'].cleaned_data['city_shipping']
                user_address_shipping.zip_address = args['form_shipping'].cleaned_data['zip_address_shipping']
                user_address_shipping.telephone = args['form'].cleaned_data['telephone']
                user_address_shipping.instruction = args['form'].cleaned_data['instruction']
                user_address_shipping.save()

            cart_user = product_models.Cart.objects.filter(user = request.user).first()
            entriesCart = product_models.EntryCart.objects.filter(cart=cart_user)
       
            newOrder = product_models.Order.objects.create(user=request.user,billing_address=user_address,shipping_address=user_address_shipping,units=0,total=0,status="payment")
            totalOrder = 0
            totalUnits = 0
            for entryCart in entriesCart:
                if(entryCart.product.discount_price != 0):
                    totalOrder += entryCart.product.discount_price*entryCart.quantity
                else:
                    totalOrder += entryCart.product.price*entryCart.quantity
                totalUnits += entryCart.quantity
                product_models.EntryOrder.objects.create(order=newOrder,product=entryCart.product,quantity=entryCart.quantity)
                product_models.EntryCart.objects.filter(Q(cart=cart_user,product=entryCart.product)).delete()
            
            newOrder.units = totalUnits
            newOrder.total = totalOrder
            newOrder.save()
            
            return HttpResponseRedirect(reverse('home:payment', kwargs={'id':newOrder.id}))

        return render(request,'home/checkout.html', args)

class Payment(LoginRequiredMixin, View):
    def get(self, request, id):
        args = {}
        args['order'] = get_object_or_404(product_models.Order, Q(id=id, status="payment"))
        return render(request,'home/payment.html', args)

class Success(LoginRequiredMixin, View):
    def get(self, request, id):
        args = {}
        args['order'] = product_models.Order.objects.filter(Q(id=id, status="paid")).first()
        if args['order']:
            return render(request,'home/success.html', args)
        else:
            return HttpResponseRedirect(reverse('home:cancelled'))

class Cancelled(LoginRequiredMixin, View):
    def get(self, request):
        args = {}
        return render(request,'home/cancelled.html', args)

class Category(View):
    def get(self, request, slug):
        args = {}
        args['cat'] = get_object_or_404(product_models.Category, slug=slug)
        args['cat_items'] =  product_models.Product.objects.filter(category = slug, publish=True)
        return render(request,'home/category.html', args)

@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = Setting.objects.filter(setting="STRIPE_PUBLISHABLE_KEY").first().value
        return JsonResponse(stripe_config, safe=False)

@csrf_exempt
def create_checkout_session(request, id):
    if request.method == 'GET':
        domain_url = 'https://admshop.pythonanywhere.com/'
        order = product_models.Order.objects.filter(Q(id=id, status="payment")).first()
        stripe.api_key = Setting.objects.filter(setting="STRIPE_SECRET_KEY").first().value
        try:
            # Create new Checkout Session for the order
            # Other optional params include:
            # [billing_address_collection] - to display billing address details on the page
            # [customer] - if you have an existing Stripe Customer ID
            # [payment_intent_data] - capture the payment later
            # [customer_email] - prefill the email input in the form
            # For full details see https://stripe.com/docs/api/checkout/sessions/create

            # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
            amount = str(order.total).split('.')[0]+str(order.total).split('.')[1]
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=order.id,
                success_url=domain_url + 'success/'+str(order.id)+'?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                customer_email=request.user.email,
                mode='payment',
                line_items=[
                    {
                        'name': 'Order #'+str(order.id),
                        'quantity': 1,
                        'currency': 'eur',
                        'amount': amount,
                    }
                ]
                
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = Setting.objects.filter(setting="STRIPE_SECRET_KEY").first().value
    endpoint_secret = Setting.objects.filter(setting="STRIPE_ENDPOINT_SECRET").first().value
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        client_reference_id=event['data']['object']['client_reference_id']
        order = product_models.Order.objects.filter(Q(id=client_reference_id, status="payment")).first()
        order.status = "paid"
        order.save()


    return HttpResponse(status=200)