from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, SignUpForm, SettingsForm
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.contrib.auth.decorators import login_required
from .models import Profile
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
                    user.set_password(password)
                    user.save()
                    
                    profile = Profile()
                    profile.user = user
                    profile.save()
                    
                    user_login(request, user)
                    return redirect(f'/users/profile/{user.id}')
    
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
                return redirect(f'/users/profile/{user.id}')
    
    return render(request, "users/login.html", {'form':form})


# Logout 

def logout(request):
    user_logout(request)
    return redirect('welcome')

# Profile
def profile(request, profile_id):
    
    account = User.objects.get(id=profile_id)
    
    profile = Profile.objects.get(user=account)
    assets = Asset.objects.filter(user=profile.user)
    featured = assets.filter(featured=True)
    posts = ForumPost.objects.filter(user=profile.user)
    orders = Order.objects.filter(user=profile.user)
    
    # todo: need to save these to the user profile somehow.
    # address = Wallet.account.address
    # key = Wallet.account.key 
    # balance = w3.eth.get_balance(address)
    context = {
        'profile': profile,
        'assets': assets,
        'featured': featured,
        'posts': posts,
        'orders': orders,
        # 'key': key,   
        # 'balance': balance
    }
    # print(Wallet.account.key)

    return render(request, "users/profile.html", context)

@login_required
def settings(request):
    user = request.user
    profile = get_object_or_404(Profile.objects.filter(user=user))
    
    if request.method == "GET":
        form = SettingsForm()
        
    else: 
        form = SettingsForm(request.POST, request.FILES)
        
        if form.is_valid():
            avatar = form.cleaned_data['avatar']
            shop_bg_photo = form.cleaned_data['shop_bg_photo']
            about_me = form.cleaned_data['about_me']
            web3_address = form.cleaned_data['web3_address']
            
            if avatar:
                profile.avatar = avatar
            if shop_bg_photo:
                profile.shop_bg_photo = shop_bg_photo 
            if about_me: 
                profile.about_me = about_me
            if web3_address: 
                profile.web3_address = web3_address
            profile.save()
            
        return redirect(f'/users/profile/{user.id}')
    
 
    context = {
        'user': user,
        'profile': profile,
        'form': form,
    }
    
    return render(request, "users/settings.html", context)