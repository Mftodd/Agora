from django.db import models
from django.contrib.auth.models import User
# from web3 import Web3

# w3 = Web3(())

# Create your models here.
# User model
# E-mail
# Password
# Create an ETH account


class Wallet(models.Model):
    user = models.ForeignKey(User, verbose_name=(""), on_delete=models.CASCADE)
    account = '0x123456'
    