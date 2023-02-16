from django.urls import path
from . import views

urlpatterns = [
    path("", views.forum, name="forum"),
    path("compose/", views.compose, name="compose"),
    
]