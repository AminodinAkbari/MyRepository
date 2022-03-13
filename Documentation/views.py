from django.shortcuts import render
from django.views.generic import ListView
from .models import DocLinks , Docs
# Create your views here.
class DocsList(ListView):
    template_name = 'Docs.html'

    def get_queryset(self):
        request=self.request
        all = DocLinks.objects.all()
        our_query = request.GET.get('q')
        if our_query is not None:
            return Docs.objects.search(our_query)
        return all