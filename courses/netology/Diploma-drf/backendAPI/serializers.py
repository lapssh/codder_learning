from rest_framework import serializers

from .models import Category, Product, ProductParameter, Shop


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name', 'state', 'url')
        read_only_fields = ('id',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'shops')
        read_only_fields = ('id',)


class ProductParameterSerializer(serializers.ModelSerializer):
    parameter = serializers.StringRelatedField()

    class Meta:
        model = ProductParameter
        fields = ('parameter', 'value',)


class ProductSerializer(serializers.ModelSerializer):
    shop = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    product_parameters = ProductParameterSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ('id', 'shop', 'name', 'category', 'external_id', 'model', 'quantity',
                  'price', 'price_rrc', 'product_parameters')
        read_only_fields = ('id',)
