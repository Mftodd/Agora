from django.shortcuts import render
from market.models import Slide

# Create your views here.
def welcome(request):
    slides = Slide.objects.filter(welcome=True)
    
    context = {
        'slides': slides
    }
    
    return render(request, 'welcome/index.html', context)
