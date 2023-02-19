from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, SignUpForm
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.contrib.auth.decorators import login_required
from .models import Wallet
from market.models import Asset, Order
from forum.models import ForumPost
from django.contrib.auth.models import User
# from web3 import Web3

# w3 = Web3()


# Sign Up
def signup(request):
    if request.method == "GET":
        form = SignUpForm()
    else:
        form = SignUpForm(request.POST)
        if form.is_valid():
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                password_confirm = form.cleaned_data['password_confirm']
                
                if password == password_confirm:
                    
                    user = User()

                    user.username = username
                    user.email = email
                    user.wallet = Wallet.account
                    user.set_password(password)
                    user.save()
                    user_login(request, user)
                    return redirect('profile')
    
    return render(request, "users/signup.html", {'form':form})

# Login

def login(request):
    
    if request.method == "GET":
        form = LoginForm()
        
    else: 
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username_input = form.cleaned_data['username']
            password_input = form.cleaned_data['password']
            
            user = authenticate (request,
                username = username_input,
                password = password_input,
            )
            
            if user is not None:
                user_login(request, user)
                return redirect('profile')
    
    return render(request, "users/login.html", {'form':form})


# Logout 

def logout(request):
    user_logout(request)
    return redirect('welcome')

# Profile
@login_required
def profile(request):
    user = request.user
    assets = Asset.objects.filter(user=user)
    posts = ForumPost.objects.filter(user=user)
    orders = Order.objects.filter(user=user)
    
    # todo: need to save these to the user profile somehow.
    # address = Wallet.account.address
    # key = Wallet.account.key 
    # balance = w3.eth.get_balance(address)
    context = {
        'user': user,
        'assets': assets,
        'posts': posts,
        'orders': orders,
        # 'key': key,   
        # 'balance': balance
    }
    # print(Wallet.account.key)

    return render(request, "users/profile.html", context)