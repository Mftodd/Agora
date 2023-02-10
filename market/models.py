from django.db import models
from django.contrib.auth.models import User

# Listing
class Listings(models.Model):
    title = models.CharField(max_length=64)
    # todo: image
    image = models.ImageField(upload_to="market/", blank=True) 
    description = models.CharField(max_length=640)
    key = models.CharField(max_length=128, blank=True)
    # todo: price should automatically update to the last transaction price
    price = models.CharField(max_length=12, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title + self.user.username
    
# Market
# Make Listings
#  
# View Listings
#  
# Buy/sell terminal