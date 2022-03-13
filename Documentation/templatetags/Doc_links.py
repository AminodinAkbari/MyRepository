from django import template
register = template.Library()
from Documentation.models import DocLinks

@register.inclusion_tag('links.html')
def link():
    qs = DocLinks.objects.all() or None
    return {"item":qs}