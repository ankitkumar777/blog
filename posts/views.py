from django.shortcuts import render
from .models import Post
# Create your views here.
from django.views.generic import ListView
from django.views import View
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name="posts/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

    
def post(request ,pk):
    posts = Post.objects.get(id=pk)
    context= {'posts': posts}
    return render(request, 'posts/post-detail.html',context )