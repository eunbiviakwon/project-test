from rest_framework import serializers

from .models import Order


class OrderListSerializer(serializers.ModelSerializer):
    product_main_name =
    product_main_image =
    class Meta:
        model = Order
        fields = ['ordered_at','total_price', 'product_main_name', 'product_main_image']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['receiver', 'address', 'delivery', 'mobile', 'requirements', 'total_price', 'payment', 'ordered_at']

