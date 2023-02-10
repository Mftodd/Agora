from django import forms
from .models import Listings

class NewListingForm(forms.ModelForm):
    class Meta:
        model = Listings
        fields = ("title", "key", "price", "image")

   
class TradeForm():
    ...
# buy button
# create a marketplace form 
# token designation
# select price type
# enter amount to pay/accept
# enter desired quantity
# send to buy button 

# sell button
