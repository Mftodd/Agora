from django.urls import path
from .views import OrderBookAPIView

urlpatterns = [
    path("order-book/<int:asset_id>/", OrderBookAPIView.as_view(), name="order_book")
]