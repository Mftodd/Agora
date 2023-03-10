from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.new_listing, name="new-listing"),
    path("", views.market, name="market"),
    path("asset/<int:asset_id>/", views.asset, name="asset"),
    path('create/make_rs_asset/', views.make_rs_asset, name="make_rs_asset"),
]