from django.shortcuts import render
from django.http import JsonResponse
from .models import Post
from .forms import CreatePost

# Create your views here.
def index(request):
    '''index, home blog app'''
    posts = Post.objects.all() # pylint: disable=no-member
    context = {
        'posts' : posts,
    }
    return render(request, 'blog/index.html', context)

def category_post(request, categoryInput):
    '''category post'''
    posts = Post.objects.filter(category__iexact=categoryInput) # pylint: disable=no-member 
    return render(request, 'blog/categoryposts.html', {
        'posts': posts,
        'active_category': categoryInput,    
    })

def detail_post(request, categoryInput, slugInput):
    '''detail post'''
    posts = Post.objects.get(slug=slugInput) # pylint: disable=no-member 
    context = {
        'post' : posts
    }
    return render(request, 'blog/detailPost.html', context)


def create_post(request):
    '''create post'''
    createpost = CreatePost()
    context = {
        'create_post' : createpost,
    }
    
    if request.method == 'POST':
        data_post = CreatePost(request.POST)
        
        if data_post.is_valid():
            # cd = data_post.cleaned_data
            # cd['category'] = cd['category'.lower()]
            # Post.objects.create(**cd) # pylint: disable=no-member
            data_post.save()
            return JsonResponse({'message': 'Post berhasil dibuat'})
        else:
            return JsonResponse({'message' : data_post.errors}, status=400)
            
    return render(request, 'blog/kontributor.html', context)







# def create_post(request):
#     createpost = CreatePost()
#     context = {
#         'create_post':createpost
#     }
    
#     if request.method == "POST":
#         createpost = CreatePost(request.POST)
        
#         if createpost.is_valid():
#             cd = createpost.cleaned_data
#             context.update(cd)
#             context['create_post'] = createpost

#     return render(request, 'blog/create_post.html', context)



    
