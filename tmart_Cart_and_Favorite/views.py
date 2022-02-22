from django.shortcuts import render
from tmart_Cart_and_Favorite.models import Order , OrderDetail
from django.shortcuts import redirect, render
from tmart_Product.models import SingleProduct

# Create your views here.
def add_to_order_detail(request,slug):
    count = request.POST.get('qtybutton') or None
    color = request.POST.get('color') or None
    print(color , count)

    if count and color:
        order = Order.objects.filter(owner_id=request.user.id,is_paid=False).first() or None
        print(order)
        if int(count) < 0:
            count = 1
        product = SingleProduct.objects.get_by_slug(slug) or None
        print(product)
        
        if order is None:
            print("order is None")
            order = Order.objects.create(owner_id=request.user.id,is_paid=False)
        
        order.orderdetail_set.create(product_id=product.id,count=count,price=product.price - product.discount,color = color)    
        return redirect('/')
    else:
        print("Form is not valid")
        return redirect('/Hichi')