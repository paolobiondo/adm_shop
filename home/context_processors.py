from product import tools as tools_products
from admin_panel import models as admin_panel_models
def home_data(request):
    args = {}
    args['menu_categories']=tools_products.getCategories()
    args['currency'] = admin_panel_models.Setting.objects.get(setting='currency')
    return args