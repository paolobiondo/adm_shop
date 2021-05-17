from product import models as products_model
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