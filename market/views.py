import requests, random, re
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Asset, Slide, Order
from .forms import NewListingForm, OrderForm
from forum.forms import NewPostForm
from forum.models import ForumPost
from django.contrib.auth.decorators import login_required
from .market_functions import execute_trade, find_match, clean_price
from django.contrib.auth.models import User
from django.core.files.base import ContentFile


# market home
def market(request):
    
    listings = Asset.objects.all()
    slides = Slide.objects.filter(featured=True)
    
    
    context = {
        'listings': listings,
        'slides': slides
    }
    
    return render(request, 'market/index.html', context)


# create a new listing
@login_required
def new_listing(request):
    
    if request.method == "GET":
        form = NewListingForm()
        
    else:
        form = NewListingForm(request.POST, request.FILES)
        
        
        if form.is_valid():
            print(form.cleaned_data)
            title = form.cleaned_data['title']
            value = form.cleaned_data['value']
            image = form.cleaned_data['image']
            print(image)
            
            asset = Asset()
            asset.title = title
            asset.value = value
            asset.image = image
            asset.user = request.user
            asset.save()
            
            order = Order()
            order.price = value
            order.volume = 1
            order.type = "SELL"
            order.asset = asset.id
            order.user = request.user
            order.save()
            
            return redirect('profile')
            
    context = {
        'form': form,
        'listings': Asset.objects.all(),
        
    }
            
    return render(request, 'market/new_listing.html', context)
            
            
            
            
# asset page
def asset(request, asset_id):
    
    asset = get_object_or_404(Asset, id=asset_id)
    try:
        reviews = ForumPost.objects.filter(asset=asset_id).reverse()
        order_book = Order.objects.filter(asset=asset_id, open=True).order_by('price', 'created').reverse()
        order_history = Order.objects.filter(asset=asset_id, open=False).order_by('price', 'created').reverse()
    except:
        reviews = "There are no reviews for this item yet."
        order_book = "There are no orders for this item yet."
        order_history = ""
        
    order_form = OrderForm()
    review_form = NewPostForm()
    
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        
        
        if order_form.is_valid():

            order = Order()
            order.price = order_form.cleaned_data['price']
            order.volume = order_form.cleaned_data['volume']
            order.type = order_form.cleaned_data['type']
            order.asset = asset_id
            order.user = request.user
            order.save()
            
            while order.fulfilled < order.volume:
                match = find_match(asset_id, order)
                if match:
                    
                        print("Match: True")
                        execute_trade(order, match)
                        
                else:
                    print("Match: False")
                    break
                
            
            context = {
                'order_form': order_form,
                'review_form': review_form,
                'asset': asset,
                'reviews': reviews,
                'order_book': order_book,
                'match': order.match,

            }
            
            return render(request, 'market/asset.html', context)
        
        review_form = NewPostForm(request.POST)

        if review_form.is_valid():
            
            review = ForumPost()
            review.review = True
            review.user = request.user
            review.body = review_form.cleaned_data['body']
            review.image = review_form.cleaned_data['image']   
            review.asset = asset_id
            review.save()
            
            context = {
                'order_form': order_form,
                'review_form': review_form,
                'asset': asset,
                'reviews': reviews,
                'order_book': order_book
            }
            
            return render(request, 'market/asset.html', context)
        
    context = {
        'order_form': order_form,
        'review_form': review_form,
        'asset': asset,
        'reviews': reviews,
        'order_book': order_book
    }
        
    return render(request, 'market/asset.html', context)

    
def make_rs_asset(request):
    category_id = random.randint(0,41)
    alpha_id = random.choice('abcdefghijklmnopqrstuvwxyz')
     
    url = f'https://secure.runescape.com/m=itemdb_rs/api/catalogue/items.json?category={category_id}&alpha={alpha_id}&page=1'
    print(url)
    
    response = requests.get(url)
    data = response.json()
    items = (i for i in data['items'])
    for item in items:
        asset = Asset()
        asset.title = item['name']
        asset.description = item['description']
        asset.user = User.objects.get(username='Jagex')
        
        image_url = item['icon_large']
        image_response = requests.get(image_url)
        asset.image.save(f"{item['id']}.png", ContentFile(image_response.content))
        
        asset.save()
        print(f"{asset.id} - {asset}")
        
        
        order = Order()
        order.price = clean_price(item['current']['price'])
        order.volume = item['id']
        order.type = "SELL"
        order.asset = asset.id
        order.user = User.objects.get(username='Jagex')
        order.save()
        print(order)
    
    return HttpResponse('Asset created successfully')
