from django.shortcuts import render, redirect, get_object_or_404
from .models import Asset, Slide
from .forms import NewListingForm, OrderForm
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
            if form.cleaned_data['key']:
                key = form.cleaned_data['key']
            else:
                key = "0x1231241258719"
            price = form.cleaned_data['price']
            image = form.cleaned_data['image']
            print(image)
            
            asset = Asset()
            asset.title = title
            asset.key = key
            asset.price = price
            asset.image = image
            asset.user = request.user
            asset.save()
            
            return redirect('home')
            
    context = {
        'form': form,
        'listings': Asset.objects.all()
    }
            
    return render(request, 'market/new_listing.html', context)
            
# asset page
def asset(request, asset_id):
    
    asset = get_object_or_404(Asset, id=asset_id)
    
    if request.method == "GET":
        order_form = OrderForm()
    
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        
        if order_form.is_valid():
            order = {'type':"", 
                     'bid':"",
                     'quantity':""}
            order['type'] = order_form.cleaned_data['type']
            order['bid'] = order_form.cleaned_data['bid']
            order['quantity'] = order_form.cleaned_data['quantity']
        
            asset.order_book.append(order)
            asset.save
            
            return(redirect('market'))
    
    context = {
        'order_form': order_form,
        'asset': asset,
        'order_book': asset.order_book
    }
    
    return render(request, 'market/asset.html', context)
