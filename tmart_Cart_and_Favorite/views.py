from django.shortcuts import render
from tmart_Cart_and_Favorite.models import *
from django.shortcuts import redirect, render
from tmart_Product.models import SingleProduct
from django.contrib.auth.decorators import login_required
from django.http.response import Http404
from .forms import CouponApplyForm
from django.utils import timezone
from django.views import generic
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

    now = timezone.now()
    form = CouponApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        coupon = Coupon.objects.get(code__iexact = code ,valid_from__lte = now ,valid_to__gte = now,active = True)
        if coupon:
            open_order.coupon = coupon
            open_order.save()
    else:
        coupon = None

    return render(request, 'UserCart.html' , {'qs':qs , 'open_order':open_order , 'form':form,'coupon':coupon})

@login_required(login_url='/login')
def remove_item_fromcart(request,**kwargs):
    detail_id = kwargs['order_id']
    if detail_id is not None:
        order_detail = OrderDetail.objects.get(id=detail_id)
        if order_detail is not None:
            order_detail.delete()
            return redirect('/Cart')
    raise Http404()


def add_to_favorite(request,slug):
    order = Order.objects.filter(owner_id=request.user.id,is_paid=False).first() or None
    print(order.owner_id)

    if order is None:
        print("order is None")
        order = Order.objects.create(owner_id=request.user.id,is_paid=False)

    all_favorites = Favorite.objects.filter(user = request.user)
    print(all_favorites)
    product = SingleProduct.objects.get(slug = slug)
    print(product)
    for i in all_favorites:
        logic = product.title == i.product.title
        if logic:
            return redirect('/')
        else:
            Favorite.objects.create(product=product,user = request.user)
            return redirect('/')
    

class FavoritePage(generic.ListView):
    template_name = 'favorites.html'
    def get_queryset(self):
        item = Favorite.objects.filter(user = self.request.user)
        return item

def remove_item_favorite(request,**kwargs):
    detail_id = kwargs['order_id']
    if detail_id is not None:
        order_detail = Favorite.objects.get_queryset().get(id=detail_id) or None
        if order_detail is not None:
            order_detail.delete()
            return redirect('/favorites')
    raise Http404()