from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from market.models import Offer, Asset
from .serializers import OrderBookSerializer

# Create your views here.
class OrderBookAPIView(APIView):
    def get(self, request, asset_id, format=None):
        buy_offers = Offer.objects.filter(asset=asset_id, type='BUY', fulfilled=False).reverse()
        sell_offers = Offer.objects.filter(asset=asset_id, type='SELL', fulfilled=False).reverse()
        order_book_data = {
            'buy_offers':[{
                'amount': offer.value, 
                'quantity':offer.quantity, 
                'type': offer.type, 
                'user':offer.user.username, 
                'created':offer.created_date
                } for offer in buy_offers],
            
            'sell_offers':[
                {'amount': offer.value, 
                 'quantity':offer.quantity, 
                 'type': offer.type, 
                 'user':offer.user.username, 
                 'created':offer.created_date} 
                for offer in sell_offers],
        }
        serializer = OrderBookSerializer(order_book_data)
        return Response(serializer.data)

