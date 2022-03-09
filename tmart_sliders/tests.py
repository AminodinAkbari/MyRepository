from django.test import TestCase
from django.template import Context, Template
from tmart_sliders.models import MainBigSlider 
from tmart_Product.models import SingleProduct
# Create your tests here.


class TestTemplateTags(TestCase):

	def setUp(self):
		qs = MainBigSlider.objects.create(title = 'test' , image = 'test' , button_text = 'test')
		SingleProduct.objects.create(slug = 'This is a test product')
		
	def test_main_slider(self):
		qs = MainBigSlider.objects.all().first()
		context = Context({
			'MainBigSlider' : 'main_big_slider_test',
		})
		template = Template(
			"{% load sliders_tags %}"
			"{% Main_slider %}"
			"{{MainBigSlider}}"
		)
		rendered = template.render(context)
		self.assertInHTML('main_big_slider_test' , rendered)

	def test_related_products(self):
		qs = SingleProduct.objects.get(slug = 'This is a test product')
		context = Context({'popular_products':'popular_products'})
		template = Template(
		"{% load sliders_tags %}"
		"{% related_products qs 'arg_2' %}"
		"{{popular_products}}"
		)
		rendered = template.render(context)
		self.assertInHTML('popular_products' , rendered)

	def test_popular_products(self):
		context = Context({'popular_products':'1'})
		template = Template(
		"{% load sliders_tags %}"
		"{% popular_products %}"
		"{{popular_products}}"
		)
		rendered = template.render(context)
		self.assertInHTML('1' , rendered)

	def test_high_sales(self):
		context = Context({
			'high_test':'1'
		})
		template = Template(
		"{% load sliders_tags %}"
		"{% high_sales %}"
		"{{high_test}}"
		)
		rendered = template.render(context)
		self.assertInHTML('1' , rendered)

	def test_singleproducts_base_on_user_visits(self):
		context = Context({
			'high_test':'1'
		})
		template = Template(
		"{% load sliders_tags %}"
		"{% high_sales %}"
		"{{high_test}}"
		)
		rendered = template.render(context)
		self.assertInHTML('1' , rendered)