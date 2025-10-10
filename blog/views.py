from django.shortcuts import render
from django.http import Http404
from .models import Post
from django.core.paginator import Paginator

def home(request):
    # MongoEngine QuerySet
    posts = Post.objects.order_by('-created_at')  # .all() is optional
    paginator = Paginator(list(posts), 6)  # Convert QuerySet to list for Django Paginator
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'page_obj': page_obj})

def detail(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        raise Http404("Post not found")
    return render(request, 'detail.html', {'post': post})

def search(request):
    query = request.GET.get('q', '')
    posts = []
    if query:
        # Case-insensitive search in MongoEngine
        posts = Post.objects(title__icontains=query)
    return render(request, 'posts.html', {'posts': posts})
