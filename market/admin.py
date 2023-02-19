from django.contrib import admin
from .models import Asset, Slide, Order

# Register your models here.
admin.site.register(Asset)
admin.site.register(Slide)
admin.site.register(Order)