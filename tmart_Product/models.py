from enum import unique
from django.db import models
from django.db.models import Q
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save
from tmart.utils import unique_slug_generator
from django.utils.html import format_html

from tmart_settings.models import IPs
# Create your models here.

class ProductManager(models.Manager):
    def search(self,query):
            lookup = (
            Q(title__icontains=query) | 
            Q(set__title__icontains=query) |
            Q(tags__name__icontains=query)
            )
            return self.get_queryset().filter(lookup).distinct()

class Category(models.Model):
    name = models.CharField(max_length=100 , verbose_name='نام دسته بندی')
    description = RichTextField(default = 'Description')
    hot_subcategory_banner = models.ImageField(default = 'empty',upload_to = 'hot_suggestions',null = True , blank = True)
    def __str__(self) :
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category , on_delete=models.CASCADE , null=True , blank=True, related_name="subcategory")
    title = models.CharField(max_length=100)

    def __str__(self) :
        return self.title

class Set(models.Model):
    subcategory = models.ForeignKey(SubCategory , on_delete=models.CASCADE , null=True , blank=True, related_name="set")
    title = models.CharField(max_length=100)

    def __str__(self) :
        return self.title

class Tags(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Colors(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    def color_tag(self):
        if self.code is not None:
            return format_html('<p style="background-color:{};color:white;padding:10px;border-radius:25%;width:20px"></p>'.format(self.code))
        else:
            return ""

    def __str__(self):
        return self.name

class SingleProduct(models.Model):
    set = models.ForeignKey(Set , on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = RichTextField()
    features = models.TextField(blank = True , null = True)
    image = models.ImageField(null = True,blank = True,upload_to = 'SingleProducts_Cover/')
    slug = models.SlugField(max_length=100,unique=True,blank=True,allow_unicode=True)
    price = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tags)
    colors = models.ManyToManyField(Colors , blank=True)
    discount = models.IntegerField(default='0')
    count = models.IntegerField(default=0)
    available = models.BooleanField()
    hits = models.ManyToManyField(IPs , blank=True)
    objects = ProductManager()


    def image_tag(self):
        return format_html('<img src="{}" / style="width:70px;">'.format(self.image.url))

    image_tag.short_description = 'Image'

    def price_with_discount(self):
        return self.price - self.discount

def product_presave_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(product_presave_receiver,sender=SingleProduct)

class singleProductGallery(models.Model):
    name    = models.CharField(max_length=200)
    image   = models.ImageField()
    product = models.ForeignKey(SingleProduct,on_delete=models.CASCADE,related_name='aaa')

    def __str__(self) :
        return self.name