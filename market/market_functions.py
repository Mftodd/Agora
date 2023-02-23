
from .models import Order, Asset


def find_match(asset_id, order):
    sell_side = Order.objects.filter(asset=asset_id, type="SELL", open=True).order_by('price', 'created')
    bid_side = Order.objects.filter(asset=asset_id, type="BUY", open=True).order_by('price', 'created')

    if order.type == "BUY":
        for ask in sell_side:
            if ask.price <= order.price: 
                ask.match = order
                order.match = ask
                ask.save()
                order.save()

    elif order.type == "SELL":
        for bid in bid_side:
            if bid.price >= order.price:
                bid.match = order
                order.match = bid
                bid.save()
                order.save()

    return order.match
                
                
                
def execute_trade(order, match):
    print(order, match)
    
    remaining_match_vol = match.volume - match.fulfilled
    asset_id = order.asset_id
    asset = Asset.objects.get(id=asset_id)
    
    # adjust for volume  
    if remaining_match_vol > order.volume:
        
        order.fulfilled = order.volume # all orders are fulfilled
        order.open = False # close the order
        order.save()
        
        match.fulfilled = match.fulfilled + order.volume # the match consumes the entire order volume.
        if match.fulfilled == match.volume: # if consuming the volume fulfills the order, 
            match.open = False              # close the order.
        match.save()
        
    elif remaining_match_vol < order.volume:
        order.fulfilled = order.fulfilled + remaining_match_vol # the order consumes the remaining match vol
        if order.fulfilled == order.volume:
            order.open = False
        order.save()
        
        match.fulfilled = match.volume # the match is fulfilled                          
        match.open = False # close the match in the orderbook
        match.save()
    
    else:
        order.fulfilled = order.volume
        order.open = False
        order.save()
        
        match.fulfilled = match.volume
        match.open = False
        match.save()

        
    return order, match