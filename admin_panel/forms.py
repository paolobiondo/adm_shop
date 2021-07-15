from django import forms
from product import models as products_models

class EditProductForm(forms.Form):
    title = forms.CharField(label='title', max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea, required=False)
    price = forms.CharField(label='price', max_length=10, required=True)
    discounted_price = forms.CharField(label='Discounted Price', max_length=100, required=False)
    units = forms.CharField(label='units', max_length=10, required=True)
    
    categories = products_models.Category.objects.all()
    CHOICES = [('0', 'select category')]
    for category in categories:
        single_tuple = ((category.slug,category.name))
        CHOICES.append(single_tuple)

    category = forms.ChoiceField(choices = CHOICES,widget=forms.Select(attrs={'class':'form-control'}))
    
    