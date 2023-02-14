from django import forms
from .models import Asset

class NewListingForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ("title", "price", "image", "description")

   
class OrderForm(forms.Form):
    order_types = ["Buy", "Sell"]
    
    type = forms.ChoiceField(choices=[order_types], required=True)
    bid = forms.DecimalField(required=True)
    quantity = forms.IntegerField(required=True)
    
# buy button
# create a marketplace form 
# token designation
# select price type
# enter amount to pay/accept
# enter desired quantity
# send to buy button 

# sell button
