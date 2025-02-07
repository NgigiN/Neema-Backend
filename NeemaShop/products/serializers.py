from rest_framework import serializers
from .models import MilkProduct, Soda, Booking


class MilkSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilkProduct
        fields = ['id', 'name', 'price_per_litre', 'stock', 'description']


class SodaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soda
        fields = ['id', 'name', 'price', 'stock']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'customer_name',
                  'total_price', 'items', 'created_at']
