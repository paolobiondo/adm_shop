from product import models as products_model
def getCategories():
    categories_array = []
    categories = products_model.Category.objects.all()
    for category in categories:     
        childs = products_model.Category_Parents.objects.filter(parent=category).select_related('child','parent')
        if childs:
            childs_array=[]
            for child in childs:
                childs_array.append(child.child)
            categories_array.append({'category':category,'parents':childs_array})
        elif category not in childs_array:
            categories_array.append({'category':category,'parents':0})
    
    return categories_array