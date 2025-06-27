from django.shortcuts import render

from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all() # pylint: disable=no-member
    context = {
        'posts' : posts,
    }
    return render(request, 'blog/index.html', context)

def category_post(request, categoryInput):
    posts = Post.objects.filter(category__iexact=categoryInput) # pylint: disable=no-member 
    return render(request, 'blog/categoryposts.html', {
        'posts': posts,
        'active_category': categoryInput,    
    })

def detail_post(request, categoryInput, slugInput):
    posts = Post.objects.get(slug=slugInput) # pylint: disable=no-member 
    context = {
        'post' : posts
    }
    return render(request, 'blog/detailPost.html', context)












def cemilan(request):
    cemilans = Post.objects.filter(category="Cemilan") # pylint: disable=no-member
    context = {
    'cemilan' : cemilans
    }
    return render(request, 'blog/cemilan.html', context)

def minuman(request):
    minumans = Post.objects.filter(category="Minuman") # pylint: disable=no-member
    context = {
    'minuman' : minumans
    }
    return render(request, 'blog/minuman.html', context)

def kuliner_lokal(request):
    kuliner_lokals = Post.objects.filter(category='Kuliner Lokal') # pylint: disable=no-member 
    context = {
        'kuliner_lokal' : kuliner_lokals
    }  
    return render(request, 'blog/kuliner_lokal.html', context)
        
def street_food(request):
    street_foods = Post.objects.filter(category='Street Food') # pylint: disable=no-member 
    context = {
        'street_food' : street_foods
    }
    return render(request, 'blog/street_food.html', context)

def kuliner_barat(request):
    kuliner_barats = Post.objects.filter(category='Kuliner Barat') # pylint: disable=no-member 
    context = {
        'kuliner_barat' : kuliner_barats
    }
    
    return render(request, 'blog/kuliner_barat.html', context)

# def category_post(request, categoryInput):
#     posts = Post.objects.filter(category = categoryInput) # pylint: disable=no-member 
#     context = {
#         'posts' : posts
#     }
#     return render(request, 'blog/categoryposts.html', context)


