from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import SingleProduct , singleProductGallery ,IPs ,Set,Review , Category
from .forms import ReviewForm
from django.contrib.auth.models import User
from tmart_account.signals import user_product_view
# Create your views here.

class AllProducts(ListView):
    template_name = 'Products_templates/shop.html'
    paginate_by = 8
    def get_queryset(self):
        return SingleProduct.objects.filter(available = True)

class AllProductsBy_SubCategory(ListView):
    template_name = 'Products_templates/shop.html'
    paginate_by = 8
    def get_queryset(self):
        return SingleProduct.objects.filter(set__subcategory_id = self.kwargs['id'])

class SelectedSet(ListView):
    template_name = 'Products_templates/shop.html'
    paginate_by = 8

    def get_queryset(self):
        return SingleProduct.objects.filter(set_id = self.kwargs['id'])

class SelectedCategory(ListView):
    template_name = 'Products_templates/shop_ByCategory.html'
    paginate_by = 8

    def get_queryset(self):
        return SingleProduct.objects.filter(set__subcategory__category_id = self.kwargs['id'])



class ProductSearch(ListView):
    template_name =  'Products_templates/shop.html'
    paginate_by = 8

    def get_queryset(self):
        request = self.request
        print(request.GET)
        our_query = request.GET.get('q')
        if our_query is not None:
            return SingleProduct.objects.search(our_query)
        return SingleProduct.objects.all()


def ProductDetail(request, slug):
    try:
        object = SingleProduct.objects.get(slug = slug)
    except:
        object = None

    if request.user.is_authenticated:
        user_product_view(object.id , request.user)
    if object.features:
        features = object.features.split(',')
    features = None

    try:
        category = Category.objects.get(subcategory__set__singleproduct = object)
    except Category.DoesNotExist:
        category = None

    review_form = None
    if request.user.is_authenticated:
        if not Review.objects.filter(product = object , user = request.user).exists():
            review_form = ReviewForm(request.POST or None)
            if review_form.is_valid():
                comment = review_form.cleaned_data.get('comment')
                user = request.user
                Review.objects.create(product = object , user = user , comment = comment)
                review_form = None


    context = {
    'gallery'    : singleProductGallery.objects.filter(product=object),
    'features'   :features,
    'review_form':review_form,
    'all_reviews':Review.objects.filter(product = object),
    'related'    :SingleProduct.objects.filter(tags__singleproduct = object).exclude(id = object.id).distinct()[:10],
    'category'   :category,
    'object':object
    }
    return render(request , 'Products_templates/ProductDetail.html' , context)
