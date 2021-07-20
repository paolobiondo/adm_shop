from django import forms
from product import models as products_models

class EditProductForm(forms.Form):
    title = forms.CharField(label='title', max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea, required=False)
    price = forms.CharField(label='price', max_length=10, required=True)
    discounted_price = forms.CharField(label='Discounted Price', max_length=100, required=False)
    units = forms.CharField(label='units', max_length=10, required=True)
    category = forms.CharField()
    
    