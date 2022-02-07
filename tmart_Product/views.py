from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import SingleProduct , singleProductGallery ,IPs
# Create your views here.

class AllProducts(ListView):
    template_name = 'Products_templates/shop.html'
    paginate_by = 8
    def get_queryset(self):
        return SingleProduct.objects.filter(available = True) 

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

        
def product_detail(request , pk):
    qs = SingleProduct.objects.get(id = pk)
    gallery = singleProductGallery.objects.filter(product=qs)
    ip = request.user.ip_address

    features = qs.features.split(',')

    if ip not in qs.hits.all():
        qs.hits.add(ip)

    context = {'object' : qs , 'gallery' : gallery , 'features':features}
    return render(request , 'Products_templates/product_details.html' , context)