from django.db import models
from django.contrib.auth.models import User
# from web3 import Web3

# w3 = Web3(())

# Create your models here.
# User model
# E-mail
# Password
# Create an ETH account

  
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=f"{user}/profile", default="/users/default_img.png", blank=True)
    shop_bg_photo = models.ImageField(upload_to=f"{user}/profile", blank=True)
    about_me = models.CharField(max_length=640, blank=True)
    featured = models.BooleanField(default=False)
    featured_slide = models.ImageField(upload_to=f"{user}/profile", blank=True)
    assets = []
    balance = models.IntegerField(default=0)
    web3_address = models.CharField(max_length=64, default=0)
    
    def __str__(self):
        return self.user.username