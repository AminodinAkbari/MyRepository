from enum import unique
from django.db import models
from django.db.models import Q
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save
from tmart.utils import unique_slug_generator
from django.utils.html import format_html
from django.contrib.auth.models import User

from tmart_settings.models import IPs
# Create your models here.

class ProductManager(models.Manager):
    def search(self,query):
            lookup = (
            Q(title__icontains=query) | 
            Q(set__title_fa__icontains=query) |
            Q(tags__name__icontains=query)
            )
            return self.get_queryset().filter(lookup).distinct()
            
    def get_by_slug(self,slug):
        qs = SingleProduct.objects.get_queryset().filter(slug=slug)
        if qs.count()==1:
            return qs.first()

class Category(models.Model):
    name = models.CharField(max_length=100 , verbose_name='نام دسته بندی')
    description = RichTextField(default = 'Description')
    hot_subcategory_banner = models.ImageField(default = 'empty',upload_to = 'hot_suggestions',null = True , blank = True)
    def __str__(self) :
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category , on_delete=models.CASCADE , null=True , blank=True, related_name="subcategory")
    title_fa = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100 , blank = True , null = True)

    def __str__(self) :
        return self.title_fa

    def get_absolute_url(self):
        return f"subcategory/{self.id}"

class Set(models.Model):
    subcategory = models.ForeignKey(SubCategory , on_delete=models.CASCADE , null=True , blank=True, related_name="set")
    title_fa = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100 , blank = True , null = True)
    hot_subcategory_banner = models.ImageField(default = 'empty',upload_to = 'hot_suggestions',null = True , blank = True)

    def get_absolute_url(self):
        return f"set/{self.id}"

    def __str__(self) :
        return self.title_fa

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
    set = models.ForeignKey(Set , on_delete=models.CASCADE,blank = True , null = True)
    title = models.CharField(max_length=250 , blank = True , null = True)
    description = RichTextField(blank = True , null = True)
    features = models.TextField(blank = True , null = True)
    image = models.ImageField(null = True,blank = True,upload_to = 'SingleProducts_Cover/' , default = 'static/product_images/category_1.jpg')
    slug = models.SlugField(max_length=100,unique=True,blank=True,allow_unicode=True , null=True)
    price = models.IntegerField(default=0,blank = True , null = True)
    tags = models.ManyToManyField(Tags,blank = True)
    colors = models.ManyToManyField(Colors , blank=True)
    discount = models.IntegerField(default='0',blank = True , null = True)
    count = models.IntegerField(default=0)
    available = models.BooleanField(default = False)
    hits = models.ManyToManyField(IPs , blank=True )
    hot_offer = models.BooleanField(default = False)
    objects = ProductManager()


    def image_tag(self):
        return format_html('<img src="{}" / style="width:70px;">'.format(self.image.url))

    image_tag.short_description = 'Image'

    def price_with_discount(self):
        return self.price - self.discount

    def get_absolute_url(self):
        return f"ProductDetail/{self.slug}"


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

class Review(models.Model):
    STATUS= (
    ('wating_for_published','در انتظار تایید'),
    ('True' , 'تایید شده'),
    ('False', 'تایید نشده')
    )
    product = models.ForeignKey(SingleProduct,on_delete = models.CASCADE)
    user    = models.ForeignKey(User,on_delete = models.CASCADE)
    comment = models.TextField()
    status  = models.CharField(max_length=20,choices=STATUS,default='wating_for_published')
    create_at= models.DateField(auto_now_add = True)

    def __str__(self) :
        return self.user.first_name