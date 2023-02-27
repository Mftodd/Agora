from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("profile/<int:profile_id>", views.profile, name="profile"),
    path("logout/", views.logout, name="logout"),  
    path("settings/", views.settings, name="settings"),  
]