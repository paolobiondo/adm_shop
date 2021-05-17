from product import tools as tools_products
from admin_panel import models as admin_panel_models
from product import models as product_models

def home_data(request):
    args = {}
    if(admin_panel_models.Setting.objects.filter(setting='currency').exists()):
        args['currency'] = admin_panel_models.Setting.objects.get(setting='currency')
    else:
        admin_panel_models.Setting.objects.create(setting='currency',value='€')
        args['currency'] = admin_panel_models.Setting.objects.get(setting='currency')

    if request.user.is_authenticated:
       args['cart'] =  product_models.Cart.objects.filter(user=request.user)

    args['menu_categories']=tools_products.getCategories()
    return args