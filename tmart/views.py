from django.shortcuts import render
from tmart_Product.models import Category
from tmart_sliders.models import MainBigSlider

def home(request):
    category = Category.objects.all()
    context = {
        'category' : category,
    }
    return render(request,'index.html', context)