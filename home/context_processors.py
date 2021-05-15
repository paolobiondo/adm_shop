from product import tools as tools_products

def home_data(request):
    args = {}
    args['menu_categories']=tools_products.getCategories()
    return args