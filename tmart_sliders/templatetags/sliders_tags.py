from django import template
from tmart_sliders.models import MainBigSlider
from tmart_Product.models import SingleProduct , Set , Category, SubCategory
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

def random_sets():
	random_sets = Set.objects.all()
	if len(random_sets) > 4:
		random_four_set = random.sample(list(random_sets) , 4) 
		return random_four_set
	else:
		random_four_set = None
		return random_sets
	

def random_subcategories():
	random_subcategories = SubCategory.objects.all()
	if len(random_subcategories) > 4:
		random_four_subcategory = random.sample(list(random_subcategories) , 4) 
		return random_four_subcategory
	else:
		random_four_subcategory = None
		return random_subcategories
	


@register.inclusion_tag('MainBigSlider.html')
def Main_slider():
	qs = MainBigSlider.objects.filter(activate = True)
	return {'MainSlider':qs}

@register.inclusion_tag('common_slider.html')
def related_products(related,category):
	return{"qs":related , "title":'محصولات مرتبط' , 'category':category}

@register.inclusion_tag('common_slider.html')
def popular_products():
	random_four_set = random_sets()
	qs = SingleProduct.objects.annotate(hits_count = Count('hits')).filter(hits_count__gt = 3)[:10]
	category=side_sets(qs)

	return {
	'qs':qs ,
	'title':'محصولات پر بازدید' ,
	'category':category ,
	'random_four_set':random_four_set ,
	'random_sets':random_sets
	}

@register.inclusion_tag('common_slider.html')
def high_sales():
	random_four_subcategory = random_subcategories()
	qs = SingleProduct.objects.filter(discount__gt = 100000)[:10]
	category=side_sets(qs)
	if qs.count() > 1:
		return {
		'qs':qs ,
		'title':'محصولات دارای بیشترین تخفیف' ,
		'category':category ,
		'random_four_subcategory':random_four_subcategory
		}
	
@register.inclusion_tag('common_slider.html')
def base_on_your_visits():
	pass