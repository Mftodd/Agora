from rest_framework import serializers
from market.models import Offer

class OrderBookSerializer(serializers.Serializer):
    buy_offers = serializers.ListField(child=serializers.DictField())
    sell_offers = serializers.ListField(child=serializers.DictField())
    