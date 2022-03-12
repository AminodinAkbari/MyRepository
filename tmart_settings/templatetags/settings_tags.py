from django import template
from tmart_Product.models import SingleProduct , Category,Set , Tags,Colors
from tmart_settings.models import OurInformation
import random
register = template.Library()


@register.inclusion_tag('settings/header.html')
def navbar(request):
	offers_products = []
	if SingleProduct.objects.all() is not None:
		for item in SingleProduct.objects.all():
			half_price = item.price / 2
			final_price = item.price - item.discount
			if half_price > final_price:
				offers_products.append(item)

	selected_set = Set.objects.all().exclude(hot_subcategory_banner = 'empty')
	if len(selected_set) > 1 :
		set_image = random.choice(selected_set)
	else:
		set_image = None
	
	context = {
	'Home':'خانه' , 
	'AllProducts':'همه محصولات' , 
	'AboutUs':'درباره ما' ,
	'ContactUs':'تماس با ما' ,
	'offers':offers_products[:2] ,
	'set_image':set_image
	}
	return {'request':request , 'context' : context}

@register.inclusion_tag('settings/footer.html')
def footer():
	information = OurInformation.objects.filter(active = True).first()
	categories = Category.objects.all()[:6]
	return {
	'information' : information,
	'categories':categories,
	
	}

@register.inclusion_tag('Products_templates/wide_banner_component.html')
def category_component(start , end):
	qs = Category.objects.all()[(start):(end)]
	if len(qs) > 1:
		final_list = random.sample(list(qs) , len(qs))
		return {'qs' : final_list}
	else:
		return {'qs' : []}

@register.inclusion_tag('Products_templates/filter_menu.html')
def filter_menu():
	filters = ['پرفروش ترین' , 'ارزانترین' , 'گرانترین' , 'تخفیف دارها']
	tags = Tags.objects.all()[:8]
	colors = Colors.objects.all()[:5]
	context = {
	"filters" : filters,
	"tags":tags,
	"colors":colors
	}
	return context