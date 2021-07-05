from product import tools as tools_products
from admin_panel import models as admin_panel_models
from product import models as product_models
from django.forms.models import model_to_dict
from django.contrib.auth.models import Group

def home_data(request):
    args = {}
    if(admin_panel_models.Setting.objects.filter(setting='currency').exists()):
        args['currency'] = admin_panel_models.Setting.objects.get(setting='currency')
    else:
        admin_panel_models.Setting.objects.create(setting='STRIPE_SECRET_KEY',value='0')
        admin_panel_models.Setting.objects.create(setting='STRIPE_PUBLISHABLE_KEY',value='0')
        admin_panel_models.Setting.objects.create(setting='STRIPE_ENDPOINT_SECRET', value='0')
        admin_panel_models.Setting.objects.create(setting='currency',value='€')
        args['currency'] = admin_panel_models.Setting.objects.get(setting='currency')
        admin_panel = Group.objects.get_or_create(name='admin_panel')


    if request.user.is_authenticated:
       args['cart'] =  product_models.Cart.objects.filter(user=request.user).first()

    args['menu_categories']=tools_products.getCategories()
    return args