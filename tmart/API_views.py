from tmart.custom_APIFilters import ProductPriceFilter
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .serializers import *

from tmart_Product.models import SingleProduct , Set


class SingleProductPriceRangeAPI(generics.ListAPIView):
    queryset = SingleProduct.objects.all()
    serializer_class = FullSerializer
    filter_class = ProductPriceFilter

class AllSingleProducts(generics.ListAPIView):
    queryset = SingleProduct.objects.all()
    serializer_class = MinimalForAllSingleProducts

class SpecificSingleProducts(generics.RetrieveUpdateDestroyAPIView):
    queryset = SingleProduct.objects.all()
    serializer_class = MinimalForAllSingleProducts

class SingleProductsBySet(generics.ListAPIView):
    def get_queryset(self):
        return SingleProduct.objects.filter(set__id = self.kwargs['set_id'])
    
    serializer_class = MinimalForAllSingleProducts

class SingleProductsByColors(generics.ListAPIView):
    def get_queryset(self):
        return SingleProduct.objects.filter(colors__name = self.kwargs['color'])
    
    serializer_class = MinimalForAllSingleProducts

class MostViewedSingleProducts(generics.ListAPIView):
    def get_queryset(self):
        return SingleProduct.objects.all().order_by('-hits')
    serializer_class = MinimalForAllSingleProducts