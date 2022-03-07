"""tmart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings

from .views import  Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view() , name = 'Home'),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('', include('tmart_Product.urls')),
    path('', include('tmart_account.urls')),
    path('', include('tmart_Cart_and_Favorite.urls')),
    path('api-auth/', include('rest_framework.urls')),
]

from .API_views import (
    SingleProductPriceRangeAPI,
    AllSingleProducts,
    SpecificSingleProducts,
    SingleProductsBySet,
    SingleProductsByColors,
    MostViewedSingleProducts
)
# REST-APIS
urlpatterns+=[
    path('product_price_range' , SingleProductPriceRangeAPI.as_view()),
    path('all_products' , AllSingleProducts.as_view()),
    path('all_products/<int:pk>' , SpecificSingleProducts.as_view()),
    path('single_products_by_set/<int:set_id>' , SingleProductsBySet.as_view()),
    path('single_products_by_colors/<color>' , SingleProductsByColors.as_view()),
    path('most_viewed_products' , MostViewedSingleProducts.as_view()),
]

if settings.DEBUG:
    urlpatterns=urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns=urlpatterns +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)