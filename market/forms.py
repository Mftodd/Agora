from django import forms
from .models import Asset, Offer

class NewListingForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ("title", "price", "image", "description")

   
class OrderForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ("value","quantity")

    
# buy button
# create a marketplace form 
# token designation
# select price type
# enter amount to pay/accept
# enter desired quantity
# send to buy button 

# sell button
