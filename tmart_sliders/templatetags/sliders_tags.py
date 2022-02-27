from django import template
from tmart_sliders.models import MainBigSlider
from tmart_Product.models import SingleProduct , Set , Category
import random
from django.db.models import Count

register = template.Library()

#---this function made side categories (you can see it in left sliders in index.html)
def side_sets(qs):
		query = random.choice(qs)
		sets = Category.objects.get(subcategory__set__singleproduct = query)
		if sets is not None:
			return sets
		return None


@register.inclusion_tag('MainBigSlider.html')
def Main_slider():
	qs = MainBigSlider.objects.filter(activate = True)
	return {'MainSlider':qs}

@register.inclusion_tag('common_slider.html')
def related_products(related,category):
	return{"qs":related , "title":'محصولات مرتبط' , 'category':category}

@register.inclusion_tag('common_slider.html')
def popular_products():
	qs = SingleProduct.objects.annotate(hits_count = Count('hits')).filter(hits_count__gt = 3)[:10]
	category=side_sets(qs)
	return {'qs':qs , 'title':'محصولات پر بازدید' , 'category':category}

@register.inclusion_tag('common_slider.html')
def high_sales():
	qs = SingleProduct.objects.filter(discount__gt = 100000)[:10]
	category=side_sets(qs)
	if qs.count() > 1:
		return {'qs':qs , 'title':'محصئلات دارای بیشترین تخفیف' , 'category':category}
	
@register.inclusion_tag('common_slider.html')
def base_on_your_visits():
	pass