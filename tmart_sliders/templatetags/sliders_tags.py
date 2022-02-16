from django import template
from tmart_sliders.models import MainBigSlider
from tmart_Product.models import SingleProduct , Set

register = template.Library()

@register.inclusion_tag('MainBigSlider.html')
def Main_slider():
	qs = MainBigSlider.objects.filter(activate = True)
	return {'MainSlider':qs}

@register.inclusion_tag('common_slider.html')
def common_slider(title_en):
	qs = SingleProduct.objects.filter(set__title_en = title_en)
	print(qs)
	return {'qs':qs}