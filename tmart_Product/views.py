from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import SingleProduct , singleProductGallery ,IPs ,Set,Review , Category
from .forms import ReviewForm

# Create your views here.

class AllProducts(ListView):
    template_name = 'Products_templates/shop.html'
    paginate_by = 8
    def get_queryset(self):
        return SingleProduct.objects.filter(available = True)

class SelectedSet(ListView):
    template_name = 'Products_templates/shop.html'
    paginate_by = 8

    def get_queryset(self):
        return SingleProduct.objects.filter(set_id = self.kwargs['id'])

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

        
# def product_detail(request , slug):
#     qs = SingleProduct.objects.get(slug = slug)
#     category = Category.objects.get(subcategory__set__singleproduct = qs)
#     gallery = singleProductGallery.objects.filter(product=qs)
#     related = SingleProduct.objects.filter(tags__singleproduct = qs).exclude(id = qs.id).distinct()[:10]
#     ip = request.user.ip_address
#     if qs.features:
#         features = qs.features.split(',')
#     features = None

#     if ip not in qs.hits.all():
#         qs.hits.add(ip)

#     review_form = False
#     if request.user.is_authenticated:
#         if not Review.objects.filter(product = qs , user = request.user).exists():
#             review_form = ReviewForm(request.POST or None)
#             if review_form.is_valid():
#                 comment = review_form.cleaned_data.get('comment')
#                 user = request.user
#                 Review.objects.create(product = qs , user = user , comment = comment)

#     all_reviews = Review.objects.filter(product = qs)

#     context = {
#     'object' : qs , 
#     'gallery' : gallery , 
#     'features':features , 
#     'review_form':review_form ,
#     'all_reviews':all_reviews,
#     'related':related,
#     'category':category,
#     }
#     return render(request , 'Products_templates/product_details.html' , context)

class ProductDetail(DetailView):

    model = SingleProduct
    template_name = 'Products_templates/ProductDetail.html'

    def get_context_data(self, **kwargs):

        if self.object.features:
            features = self.object.features.split(',')
        features = None

        review_form = False
        if self.request.user.is_authenticated:
            if not Review.objects.filter(product = self.object , user = self.request.user).exists():
                review_form = ReviewForm(self.request.POST or None)
                if review_form.is_valid():
                    comment = review_form.cleaned_data.get('comment')
                    user = self.request.user
                    Review.objects.create(product = self.object , user = user , comment = comment)

        context = super().get_context_data(**kwargs)
        context['gallery'] = singleProductGallery.objects.filter(product=self.object)
        context['features']= features
        context['review_form'] = review_form
        context['all_reviews'] = Review.objects.filter(product = self.object)
        context['related'] = SingleProduct.objects.filter(tags__singleproduct = self.object).exclude(id = self.object.id).distinct()[:10]
        context['category']=Category.objects.get(subcategory__set__singleproduct = self.object)
        return context