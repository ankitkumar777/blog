from django.shortcuts import render
from .models import Post
# Create your views here.
from django.views.generic import ListView
from django.views import View

class BlogIndexView(ListView):
    model=Post
    template_name="posts/index.html"

    
def post(request ,pk):
    posts = Post.objects.get(id=pk)
    context= {'posts': posts}
    return render(request, 'posts/posts.html',context )