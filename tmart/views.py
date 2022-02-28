from django.shortcuts import render
from tmart_Product.models import Category, Set
from tmart_sliders.models import MainBigSlider

def home(request):
    category = Category.objects.all()
    sets = Set.objects.all()
    context = {
        'category' : category,
        'sets':sets
    }
    return render(request,'index.html', context)