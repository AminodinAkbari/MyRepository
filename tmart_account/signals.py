from itertools import product
from .models import History
from django.contrib.auth.models import User
from tmart_Product.models import SingleProduct , Tags
def user_product_view(product_id , user):
    singleproduct=SingleProduct.objects.get(id = product_id)
    tags = []
    for i in singleproduct.tags.all():
        tags.append(i.name)
    
    past_model = History.objects.filter(user = user).first()
    if past_model:
        product = past_model.product.split(",")
        for product_item in product:
            if product_item not in tags:
                tags.append(product_item)
        tags_string = ','.join(str(e) for e in tags)

        past_model.delete()

        History.objects.create(
            user = user ,
            product = tags_string ,
        )   
    
    else:
        tags_string = ','.join(str(e) for e in tags)
        History.objects.create(
        user = user ,
        product = tags_string
        )


