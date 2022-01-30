from rest_framework import serializers

from users.serializers import ContactSerializer
from .models import Order, OrderItem


class OrderItemAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('product_name', 'external_id', 'quantity', 'price',
                  'total_amount', 'order', 'category', 'shop')


class OrderItemSerializer(serializers.ModelSerializer):
    shop = serializers.StringRelatedField()
    category = serializers.StringRelatedField()

    class Meta:
        model = OrderItem
        fields = ('id', 'product_name', 'external_id', 'quantity',
                  'price', 'total_amount', 'order', 'category', 'shop')
        read_only_fields = ('id',)
        extra_kwargs = {
            'order': {'write_only': True}
        }


class OrderModifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'status', 'contact')
        read_only_fields = ('id',)


class OrderSerializer(serializers.ModelSerializer):
    ordered_items = OrderItemSerializer(read_only=True, many=True)

    total_sum = serializers.IntegerField()
    total_quantity = serializers.IntegerField()
    contact = ContactSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'status', 'total_quantity',
                  'total_sum', 'contact', 'ordered_items')
        read_only_fields = ('id',)
