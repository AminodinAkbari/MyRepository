from django.test import TestCase , Client
from django.urls import reverse , resolve
from tmart_Product.views import *  
from tmart_Product.models import *

# Create your tests here.

def setUp(self):
    self.client = Client()

class TestUrls(TestCase):


    def test_allproducts(self):
        url = reverse('AllProducts')
        self.assertEquals(resolve(url).func.view_class , AllProducts)

    def test_set(self):
        url = reverse('set_with_id')
        self.assertEquals(resolve(url).func.view_class , SelectedSet)

    def test_search(self):
        url = reverse('search')
        self.assertEquals(resolve(url).func.view_class , ProductSearch)

    def test_set(self):
        url = reverse('product_details' , args=['slug'])
        self.assertEquals(resolve(url).func , product_detail)

class TestViews(TestCase):

    def test_detail_view(self):
        qs = SingleProduct.objects.create(slug = 'This is a test product')
        test_category = Category.objects.create(name = 'test_category')
        test_subcategory = SubCategory.objects.create(category = test_category , title = "test_subcategory")
        test_set = Set.objects.create(subcategory = test_subcategory , title_fa = 'test_set')
        response = self.client.get(reverse('product_details' , args = [qs.slug]))
        self.assertEquals(response.status_code , 200)


    def test_AllProduct(self):
        qs = SingleProduct.objects.create(slug = 'This is a test product')
        response = self.client.get(reverse('all'))
        self.assertEquals(response.status_code , 200)


    def test_SelectedSet(self):
        qs = SingleProduct.objects.create(slug = 'This is a test product')
        response = self.client.get(reverse('set_with_id' , args=[1]))
        self.assertEquals(response.status_code , 200)

    def test_ProductSearch(self):
        response = self.client.get(reverse('search'))
        self.assertEquals(response.status_code , 200)