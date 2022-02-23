from django.shortcuts import render
from tmart_Cart_and_Favorite.models import Order , OrderDetail
from django.shortcuts import redirect, render
from tmart_Product.models import SingleProduct
from django.contrib.auth.decorators import login_required
from django.http.response import Http404

# Create your views here.

@login_required(login_url='/login')
def add_to_order_detail(request,slug):
    count = request.POST.get('qtybutton') or None
    color = request.POST.get('color') or None
    print(color , count)

    if count and color:
        order = Order.objects.filter(owner_id=request.user.id,is_paid=False).first() or None
        
        if int(count) < 0:
            count = 1

        product = SingleProduct.objects.get_by_slug(slug) or None
        
        
        if order is None:
            print("order is None")
            order = Order.objects.create(owner_id=request.user.id,is_paid=False)
        
        order.orderdetail_set.create(product_id=product.id,count=count,price=product.price - product.discount,color = color)    
        return redirect('/')
    else:
        print("Form is not valid")
        return redirect('/Hichi')

def Cart_user(request):
    open_order:Order = Order.objects.filter(owner_id=request.user.id,is_paid=False).first() or False
    if open_order:
        qs = OrderDetail.objects.filter(order_id = open_order or None)
    else:
        qs = None
    return render(request, 'UserCart.html' , {'qs':qs})

@login_required(login_url='/login')
def remove_item_fromcart(request,**kwargs):
    detail_id = kwargs['order_id']
    if detail_id is not None:
        order_detail = OrderDetail.objects.get(id=detail_id)
        if order_detail is not None:
            order_detail.delete()
            return redirect('/Cart')
    raise Http404()