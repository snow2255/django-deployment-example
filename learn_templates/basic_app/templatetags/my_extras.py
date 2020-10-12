from django import template

register = template.library()
# creating a decorator
@register.filter(name='cut')

def cut(value,arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')

    # register.filtter('cut',cut)
