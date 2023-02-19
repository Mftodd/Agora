from rest_framework import serializers
from market.models import Order

class OrderBookSerializer(serializers.Serializer):
    buy_orders = serializers.ListField(child=serializers.DictField())
    sell_orders = serializers.ListField(child=serializers.DictField())
    