from django.shortcuts import render, redirect, get_object_or_404
from .models import ForumPost
from .forms import NewPostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def forum(request):
    
    feed = ForumPost.objects.all()
    form = NewPostForm()
    
    context = {
        "feed":feed,
        "form":form
    }
    
    return render(request, 'forum/index.html', context)

@login_required
def compose(request):
    
    if request.method == "GET":
        form = NewPostForm()
        
    else:
        
        form = NewPostForm(request.POST)
        
        if form.is_valid():
            body = form.cleaned_data['body']
            image = form.cleaned_data['image']
            
            
            new_post = ForumPost()
            new_post.body = body
            new_post.image = image
            new_post.user = request.user
            new_post.save()
            
            return redirect('forum')
        
    return render(request, 'forum/compose.html', {"form": form})
            