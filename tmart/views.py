from tmart_Product.models import Category, Set
from tmart_sliders.models import MainBigSlider
from django.views.generic import ListView , DetailView

class Home(ListView):
    model = Category
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request
        context['category']= Category.objects.all()
        context['set']= Set.objects.all()
        return context