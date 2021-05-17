from django import template

register = template.Library() 

@register.filter(name='is_admin_panel') 
def is_admin_panel(user):
    return user.groups.filter(name='admin_panel').exists() 