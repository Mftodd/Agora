from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from market.models import Order, Asset
from .serializers import OrderBookSerializer

# Create your views here.
class OrderBookAPIView(APIView):
    def get(self, request, asset_id, format=None):
        buy_orders = Order.objects.filter(asset=asset_id, type='BUY', fulfilled=False).reverse()
        sell_orders = Order.objects.filter(asset=asset_id, type='SELL', fulfilled=False).reverse()
        order_book_data = {
            'buy_orders':[{
                'price': order.price, 
                'volume':order.volume, 
                'type': order.type, 
                'user':order.user.username, 
                'created':order.created
                } for order in buy_orders],
            
            'sell_orders':[
                {'price': order.price, 
                 'volume':order.volume, 
                 'type': order.type, 
                 'user':order.user.username, 
                 'created':order.created} 
                for order in sell_orders],
        }
        serializer = OrderBookSerializer(order_book_data)
        return Response(serializer.data)

# class AllObjectsAPIView(APIView):
#     def get(self, request, asset_id, format=None):
#         all_assets = 
