from rest_framework import serializers
from tmart_Product.models import SingleProduct

class FullSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleProduct
        fields = '__all__'

class MinimalForAllSingleProducts(serializers.ModelSerializer):
    class Meta:
        model  = SingleProduct
        fields = ['title' , 'image' , 'price' , 'discount' , 'available' , 'hits']