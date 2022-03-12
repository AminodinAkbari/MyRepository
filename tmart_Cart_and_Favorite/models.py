from django.db import models
from django.contrib.auth.models import User
from tmart_Product.models import SingleProduct
from django.core.validators import MinValueValidator , MaxValueValidator
from django.utils import timezone

# Create your models here.
class Order(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE , null=True)
    is_paid = models.BooleanField(default=False)
    paymant_date=models.DateTimeField(default=timezone.now)	
    shipping = models.IntegerField(default = 20000)
    coupon = models.ForeignKey('Coupon' , on_delete=models.SET_NULL, blank=True, null=True)

    def get_total_price(self):
        amount = 0
        for detail in self.orderdetail.all():
            amount += detail.price * detail.count
        if self.coupon:
            discount = self.coupon.discount / 100 * amount
            amount -= discount
        if amount > 199000 :
            return amount
        elif amount == 0:
            return amount
        else:
            return amount+self.shipping

    def save(self, *args, **kwargs):
        self.paymant_date = timezone.now()
        super(Order, self).save(*args, **kwargs)
        
        


class OrderDetail(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="orderdetail")
    product = models.ForeignKey(SingleProduct,on_delete=models.CASCADE,related_name="product")
    price = models.IntegerField()
    count = models.IntegerField()
    color = models.CharField(max_length=50,default='Here Can Be Your Selected Color')


    def get_total_price(self):
        return self.price * self.count


class Coupon(models.Model):
    code = models.CharField(max_length = 50 , unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    active = models.BooleanField(default = False)


class Favorite(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    product = models.ForeignKey(SingleProduct,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self) -> str:
        return super().__str__()

class CheckOut(models.Model):
    order = models.ForeignKey(Order , on_delete=models.SET_NULL , null=True , related_name = "checkout")
    address = models.TextField()
    zipcode = models.CharField(max_length=10)
    send_info = [
    ('not_send_yet' , 'هنوز ارسال نشده'),
    ('recive' , 'دریافت شده'),
    ('inprogress' , 'در راه'),
    ('feild' , 'بازگشت خورده')
    ]
    status = models.CharField(choices=send_info , max_length=20 , default = 'not_send_yet')
