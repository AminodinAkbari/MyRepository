from django import template
from tmart_sliders.models import MainBigSlider

register = template.Library()

@register.inclusion_tag('MainBigSlider.html')
def Main_slider():
	qs = MainBigSlider.objects.filter(activate = True)
	return {'MainSlider':qs}