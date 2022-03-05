from django.test import TestCase , Client

from django.urls import reverse , resolve
from django.core.files.uploadedfile import SimpleUploadedFile

from tmart_Product.views import *  
from tmart_Product.models import *

# Create your tests here.

def setUp(self):
    self.client = Client()

class TestUrls(TestCase):

    def test_allproducts(self):
        url = reverse('tmart_Product:AllProducts')
        self.assertEquals(resolve(url).func.view_class , AllProducts)

    def test_set(self):
        url = reverse('tmart_Product:set_with_id')
        self.assertEquals(resolve(url).func.view_class , SelectedSet)

    def test_search(self):
        url = reverse('tmart_Product:search')
        self.assertEquals(resolve(url).func.view_class , ProductSearch)

    def test_set(self):
        url = reverse('tmart_Product:ProductDetail' , args=['slug'])
        self.assertEquals(resolve(url).func.view_class , ProductDetail)

class TestViews(TestCase):

    def test_detail_view(self):
        qs = SingleProduct.objects.create(slug = 'This is a test product')
        response = self.client.get(reverse('tmart_Product:ProductDetail' , args = [qs.slug]))
        self.assertEquals(response.status_code , 200)

    def test_AllProduct(self):
        qs = SingleProduct.objects.create(slug = 'This is a test product')
        response = self.client.get(reverse('tmart_Product:AllProducts'))
        self.assertEquals(response.status_code , 200)

    def test_AllProduct_BySubCategory(self):
        qs = SingleProduct.objects.create(slug = 'This is a test product')
        response = self.client.get(reverse('tmart_Product:SubCategory' , args=[1]))
        self.assertEquals(response.status_code , 200)

    def test_SelectedSet(self):
        qs = SingleProduct.objects.create(slug = 'This is a test product')
        response = self.client.get(reverse('tmart_Product:set_with_id' , args=[1]))
        self.assertEquals(response.status_code , 200)

    def test_ProductSearch(self):
        response = self.client.get(reverse('tmart_Product:search'))
        self.assertEquals(response.status_code , 200)

class TestModels(TestCase):

    def setUp(self):
        category = Category.objects.create(name = 'category_test' , description = 'category_description_test')
        subcategory = SubCategory.objects.create(category = category , title_fa = 'test_title_fa')
        Set.objects.create(subcategory = subcategory , title_fa = 'test_title_fa')

        tags = Tags.objects.create(name = 'test_tag_name')
        colors = Colors.objects.create(name = 'test_colors_name' , code = '#111')

        singleproducts = SingleProduct.objects.create(title = 'singleproduct_title')

    def test_setUp(self):
        category = Category.objects.get(name = 'category_test')
        subcategory = SubCategory.objects.get(category = category)
        set = Set.objects.get(subcategory = subcategory)