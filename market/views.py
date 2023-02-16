from django.shortcuts import render, redirect, get_object_or_404
from .models import Asset, Slide, Offer
from .forms import NewListingForm, OrderForm
from forum.forms import NewPostForm
from forum.models import ForumPost
from django.contrib.auth.decorators import login_required


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
            price = form.cleaned_data['price']
            image = form.cleaned_data['image']
            print(image)
            
            asset = Asset()
            asset.title = title
            asset.price = price
            asset.image = image
            asset.user = request.user
            asset.save()
            
            return redirect('profile')
            
    context = {
        'form': form,
        'listings': Asset.objects.all()
    }
            
    return render(request, 'market/new_listing.html', context)
            
            
            
            
# asset page
def asset(request, asset_id):
    
    asset = get_object_or_404(Asset, id=asset_id)
    try:
        reviews = ForumPost.objects.filter(asset=asset_id).reverse()
        order_book = Offer.objects.filter(asset=asset_id, fulfilled=False).order_by('value').reverse()
    except:
        reviews = "There are no reviews for this item yet."
        order_book = "There are no orders for this item yet."
        
    order_form = OrderForm()
    review_form = NewPostForm()
        
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        
        if order_form.is_valid():
            order = Offer()
            order.value = order_form.cleaned_data['value']
            order.quantity = order_form.cleaned_data['quantity']
            order.type = "BUY"
            order.asset = asset_id
            order.user = request.user
            order.fulfilled = False
            order.save()
            
            context = {
                'order_form': order_form,
                'review_form': review_form,
                'asset': asset,
                'reviews': reviews,
                'order_book': order_book
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
