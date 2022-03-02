import django_filters
from tmart_Product.models import SingleProduct

class ProductPriceFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter()
    class Meta:
        model = SingleProduct
        fields = ['price']