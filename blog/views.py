from django.shortcuts import get_object_or_404, render
from .models import Post
from django.core.paginator import Paginator


def home(request):
  posts = Post.objects.all().order_by('-created_at')
  paginator = Paginator(posts, 6)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  return render(request,'home.html',{'page_obj': page_obj})



def detail(request,slug):
  post = get_object_or_404(Post,slug=slug)
  return render(request,'detail.html',{'post':post})



def search(request):
  query = request.GET.get('q','')
  if query:
    posts = Post.objects.filter(title__icontains=query)
    return render(request,'posts.html',{'posts':posts})
