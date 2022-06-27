from django import template
from ..models import Category
register = template.Library()

@register.simple_tag
def get_category():
    context = Category.objects.all()
    return {'list_objects': context}