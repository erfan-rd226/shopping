from .models import Category , Product 
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'
        # ['id','title','description','is_enable']


class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'
        # ['id','title','categories','description','is_enable']