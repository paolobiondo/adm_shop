from product import models as products_model
from django.utils.datetime_safe import datetime
from decimal import Decimal

def getCategories():
    categories_array = []
    categories = products_model.Category.objects.all()
    cat_childs=[]
    for category in categories:     
        childs = products_model.Category_Parents.objects.filter(parent=category).select_related('child','parent')
        if childs:
            if(category not in cat_childs):
                childs_array=[]
                for child in childs:
                    childs_array.append(child.child)
                    cat_childs.append(child.child)
                categories_array.append({'category':category,'parents':childs_array})
                childs_array=[]
        else:
            if(category not in cat_childs):
                categories_array.append({'category':category,'parents':0})

    return categories_array

def updateCart(instance,quantity_difference):
    instance.cart.total = Decimal(instance.cart.total) + (Decimal(quantity_difference) * Decimal(instance.product.price))
    instance.cart.count = int(instance.cart.count) + int(quantity_difference)
    instance.cart.updated = datetime.now()
    instance.cart.save()