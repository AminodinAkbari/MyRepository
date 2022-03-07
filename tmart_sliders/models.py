from django.db import models
from django.utils.html import format_html
from tmart_Product.models import Set
# Create your models here.

class MainBigSlider(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null= True , blank= True)
    image = models.ImageField(upload_to = 'BigSlider/')
    link_to_set = models.ForeignKey(Set , on_delete = models.CASCADE , blank=True , null = True)
    button_text = models.CharField(max_length=50)
    activate = models.BooleanField(default=False)
    def image_tag(self):
        return format_html('<img src="{}" / style="width:70px;">'.format(self.image.url))
    image_tag.short_description = 'Image'
