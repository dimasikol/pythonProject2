from django import template
from ..models import Category,Genre
register = template.Library()


@register.simple_tag
def category_tag():
    context=Genre.objects.all()
    return {'list_objects': context}


def ref_tag():

    pass