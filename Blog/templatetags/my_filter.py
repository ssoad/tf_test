from django import template

register = template.Library()


@register.filter
def times(count):
    return range(int(count))


@register.filter
def sub(count):
    return range(int(5 - int(count)))


@register.filter
def replacespace(value):
    return str(value).replace("#", " sharp").replace(" ", "_").lower()
