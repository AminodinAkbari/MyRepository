from django import template
register = template.Library()

@register.inclusion_tag('settings/header.html')
def navbar(request):
	# item = Navbar.objects.all()[:6]
	return {'request':request}

@register.inclusion_tag('settings/footer.html')
def footer():
	# item = Navbar.objects.all()[:6]
	return {}