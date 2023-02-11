from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.new_listing, name="new-listing"),
    path("", views.market, name="market"),
]