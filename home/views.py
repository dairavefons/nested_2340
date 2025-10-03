from django.shortcuts import render
from products.models import Post

def home(request):
    recent_listings = Post.objects.filter(is_claimed=False)[:3]  # Get 3 most recent unclaimed listings
    return render(request, 'home/index.html', {'recent_listings': recent_listings})

def about(request):
    return render(request, 'home/about.html')
