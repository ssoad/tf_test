from django import template
from Academy import models

register = template.Library()


@register.filter
def times(count):
    return range(int(count))


@register.filter
def sub(count):
    return range(int(5 - int(count)))


@register.filter
def replacespace(value):
    return str(value).replace(" ", "_").lower()


@register.filter
def capitalize(value):
    return str(value).replace("_", " ").title()


@register.filter
def classCount(value):
    current_course = models.Course.objects.get(id=value)
    classes = 0
    for section in current_course.section_course.all():
        classes += section.content_section.count()

    return classes
