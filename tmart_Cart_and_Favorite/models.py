from django.db import models
from django.contrib.auth.models import User
from tmart_Product.models import SingleProduct

# Create your models here.
class Order(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    paymant_date=models.DateTimeField(blank=True,null=True)	

    def get_total_price(self):
        amount = 0
        for detail in self.orderdetail_set.all():
            amount += detail.price * detail.count
        return amount


class OrderDetail(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(SingleProduct,on_delete=models.CASCADE)
    price = models.IntegerField()
    count = models.IntegerField()
    color = models.CharField(max_length=50,default='Here Can Be Your Selected Color')


    def get_total_price(self):
        return self.price * self.count