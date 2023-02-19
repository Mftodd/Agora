from django.db import models
from django.contrib.auth.models import User

# Listing
class Asset(models.Model):
    title = models.CharField(max_length=64)
    # todo: image
    image = models.ImageField(upload_to="market/", blank=True) 
    description = models.CharField(max_length=640)
    creator = models.CharField(max_length=128, blank=True)
    # todo: price should automatically update to the last transaction price
    value = models.CharField(max_length=12, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title + self.user.username
    
class Slide(models.Model):
    image = models.ImageField(upload_to="market_slideshow/")
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=100)
    featured = models.BooleanField(default=False)
    welcome = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
class Order(models.Model):
    ORDER_TYPE = (
        ("BUY",'buy'),
        ("SELL",'Sell'),
    )
    price = models.IntegerField(default=0)
    volume = models.IntegerField(default=1)
    fulfilled = models.IntegerField(default=0)
    type = models.CharField(max_length=4, choices = ORDER_TYPE, default="BUY")
    asset = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    match = None
    open = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.asset} - {self.type} ${self.price} x{self.volume}/{self.fulfilled} {self.open}"
    

    
# Market
# Make Listings
#  
# View Listings
#  
# Buy/sell terminal