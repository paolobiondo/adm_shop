from django import forms
from product.models import UserAddress

class UserAddressForm(forms.Form):
    country = forms.CharField(label='country', max_length=100, required=True)
    name = forms.CharField(label='first name', max_length=100, required=True)
    surname = forms.CharField(label='last name', max_length=100, required=True)
    address =  forms.CharField(widget=forms.Textarea, required=True)
    city = forms.CharField(label='city', max_length=100, required=True)
    zip_address = forms.CharField(label='zipaddress', max_length=100, required=True)
    telephone = forms.CharField(label='telephone', max_length=100, required=False)
    instruction =  forms.CharField(widget=forms.Textarea, required=False)

class UserAddressShippingForm(forms.Form):
    country_shipping = forms.CharField(label='country', max_length=100, required=False)
    name_shipping = forms.CharField(label='first name', max_length=100, required=False)
    surname_shipping = forms.CharField(label='last name', max_length=100, required=False)
    address_shipping =  forms.CharField(widget=forms.Textarea, required=False)
    city_shipping = forms.CharField(label='city', max_length=100, required=False)
    zip_address_shipping = forms.CharField(label='zip address', max_length=100, required=False)
