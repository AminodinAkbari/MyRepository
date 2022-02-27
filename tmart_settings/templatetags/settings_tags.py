from django import template
from tmart_Product.models import SingleProduct , Category
import random
register = template.Library()


@register.inclusion_tag('settings/header.html')
def navbar(request):
	offers_products = []
	for item in SingleProduct.objects.all():
		half_price = item.price / 2
		final_price = item.price - item.discount
		if half_price > final_price:
			offers_products.append(item)

	if len(offers_products) > 2:
		selected_product_for_category_image = random.choice(offers_products)
	else:
		selected_product_for_category_image = None
	
	context = {
	'Home':'خانه' , 
	'AllProducts':'همه محصولات' , 
	'AboutUs':'درباره ما' ,
	'ContactUs':'تماس با ما' ,
	'offers':offers_products[:2] ,
	'category_image':selected_product_for_category_image
	}
	return {'request':request , 'context' : context}

@register.inclusion_tag('settings/footer.html')
def footer():
	# item = Navbar.objects.all()[:6]
	return {}