from django import forms
from .models import Asset, Order

class NewListingForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ("title", "value", "image", "description")

   
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("type","price","volume",)

    
# buy button
# create a marketplace form 
# token designation
# select price type
# enter amount to pay/accept
# enter desired quantity
# send to buy button 

# sell button
