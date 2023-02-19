from django.shortcuts import render, redirect, get_object_or_404
from .models import Asset, Slide, Order
from .forms import NewListingForm, OrderForm
from forum.forms import NewPostForm
from forum.models import ForumPost
from django.contrib.auth.decorators import login_required
from .market_functions import execute_trade, find_match


# market home
def market(request):
    
    listings = Asset.objects.all()
    slides = Slide.objects.all()
    
    
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
        order_book = Order.objects.filter(asset=asset_id, open=True).order_by('price').reverse()
    except:
        reviews = "There are no reviews for this item yet."
        order_book = "There are no orders for this item yet."
        
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
