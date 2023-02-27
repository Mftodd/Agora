from django import forms
from .models import Profile

class LoginForm(forms.Form):
    
    username = forms.CharField(
        min_length=3, 
        max_length=32,
        )
    
    password = forms.CharField(
        widget=forms.PasswordInput(), 
        min_length=6,
        max_length=32
        )
    
class SignUpForm(LoginForm):
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(),
        min_length=6,
        max_length= 32,
        )
    email = forms.EmailField()
    
class SettingsForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("avatar", "shop_bg_photo", "about_me", "web3_address")