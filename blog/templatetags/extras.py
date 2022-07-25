from django import template
register=template.Library()
@register.filter(name='get_val')

def val(dict,key):
    return dict.get(key)
    