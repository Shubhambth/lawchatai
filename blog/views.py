from django.shortcuts import get_object_or_404, render
from .models import Post


def home(request):
  posts = Post.objects.all()
  
  return render(request,'home.html',{"posts":posts})



def detail(request,slug):
  post = get_object_or_404(Post,slug=slug)
  return render(request,'detail.html',{'post':post})



def search(request):
  query = request.GET.get('q','')
  if query:
    posts = Post.objects.filter(title__icontains=query)
    return render(request,'posts.html',{'posts':posts})
