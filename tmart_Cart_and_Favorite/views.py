from django.shortcuts import render
from tmart_Cart_and_Favorite.models import *
from django.shortcuts import redirect, render
from tmart_Product.models import SingleProduct
from django.contrib.auth.decorators import login_required
from django.http.response import Http404
from .forms import CouponApplyForm , CheckOutForm
from django.utils import timezone
from datetime import datetime
from django.views import generic
from django.contrib import messages
from django.utils.decorators import method_decorator
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
        
        OrderDetail.objects.create(order = order,product_id=product.id,count=count,price=product.price - product.discount,color = color)    
        return redirect('/')
    else:
        print("Form is not valid")
        return redirect('/Hichi')
        
@login_required(login_url='/login')
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
            used = Order.objects.filter(owner = request.user , is_paid = True , coupon = coupon).first()
            if used is not None:
                messages.error(request , 'شما این کد تخفیف را قبلا استفاده کرده اید')
            else:
                open_order.coupon = coupon
                open_order.save()
    else:
        coupon = None

    passed_order = Order.objects.filter(owner = request.user , is_paid=True)
    # if passed_order is not None:
    #     passed_status = CheckOut.objects.filter(order = passed_order[:1])
    # else:
    #     passed_status = None
    # print(passed_order)

    context ={
    'qs':qs ,
    'open_order':open_order ,
    'form':form,
    'coupon':coupon,
    'passed_order':passed_order,
    # 'passed_status':passed_status
    }

    return render(request, 'UserCart.html' , context)

@login_required(login_url='/login')
def remove_item_fromcart(request,**kwargs):
    detail_id = kwargs['order_id']
    if detail_id is not None:
        order_detail = OrderDetail.objects.get(id=detail_id)
        if order_detail is not None:
            order_detail.delete()
            return redirect('/Cart')
    raise Http404()

@login_required(login_url='/login')
def add_to_favorite(request,slug):
    order = Order.objects.filter(owner_id=request.user.id,is_paid=False).first() or None
    if order is None:
        print("order is None")
        order = Order.objects.create(owner_id=request.user.id,is_paid=False)
    product = SingleProduct.objects.get(slug = slug)
    try:
        Favorite.objects.get(product = product ,user = request.user)
    except:
        Favorite.objects.create(product = product , user = request.user)
    return redirect('/')

    
@method_decorator(login_required, name='dispatch')
class FavoritePage(generic.ListView):
    template_name = 'favorites.html'
    def get_queryset(self):
        item = Favorite.objects.filter(user = self.request.user)
        return item

@login_required(login_url='/login')
def remove_item_favorite(request,**kwargs):
    detail_id = kwargs['order_id']
    if detail_id is not None:
        order_detail = Favorite.objects.get_queryset().get(id=detail_id) or None
        if order_detail is not None:
            order_detail.delete()
            return redirect('/favorites')
    raise Http404()

@login_required(login_url='/login')
def checkout(request):
    open_order:Order = Order.objects.filter(owner_id=request.user.id,is_paid=False).first() or False
    if open_order:
        qs = OrderDetail.objects.filter(order_id = open_order or None)
    else:
        qs = None
    forms = CheckOutForm(request.POST or None)
    if forms.is_valid():
        address = forms.cleaned_data.get("address")
        zipcode = forms.cleaned_data.get("zipcode")
        CheckOut.objects.create(order = open_order , address = address , zipcode = zipcode , status = 'inprogress')
        open_order.is_paid = True
        open_order.save()
        messages.success(request , 'خرید شما با موفقیت انجام شد . شما می توانید وضعیت سبد خریدتان را در صفحه سبد خرید ببینید')
        return redirect("/")

    context = {
    "forms":forms ,
    "qs" : qs,
    "user":request.user,
    "open_order":open_order
    }
    return render(request , 'checkout.html' , context)