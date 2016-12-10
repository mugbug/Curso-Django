from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='replace')
@stringfilter
def replace(value, arg):
    if value:
        value = value.upper()
    return value


@register.filter(name='add_label')
def add_label(value, arg):
    new_value = '{0}: {1}'.format(arg, value)
    return new_value
