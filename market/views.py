from django.shortcuts import render, redirect, get_object_or_404
from .models import Listings, Slideshow
from .forms import NewListingForm
from django.contrib.auth.decorators import login_required

def index(request):
    
    listings = Listings.objects.all()
    
    
    context = {
        'listings': listings,
    }
    
    return render(request, 'market/index.html', context)


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
            
            new_listing = Listings()
            new_listing.title = title
            new_listing.key = key
            new_listing.price = price
            new_listing.image = image
            new_listing.user = request.user
            new_listing.save()
            
            return redirect('home')
            
    context = {
        'form': form,
        'listings': Listings.objects.all()
    }
            
    return render(request, 'market/new_listing.html', context)
            

# Create your views here.