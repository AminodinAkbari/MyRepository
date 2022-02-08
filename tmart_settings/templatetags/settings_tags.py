from django import template
register = template.Library()

@register.inclusion_tag('settings/header.html')
def navbar():
	# item = Navbar.objects.all()[:6]
	return {}

@register.inclusion_tag('settings/footer.html')
def footer():
	# item = Navbar.objects.all()[:6]
	return {}