from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponseRedirect
from .models import Post
from .forms import SignUpForm, LoginForm, PostForm
from django.views import View
from django.views.generic import ListView, TemplateView
from django.contrib import messages
from django.contrib.auth.models import Group
# Create your views here.

def index(request):
    post= Post.objects.all()
    return render(request, "posts/index.html", {'post': post})

class AboutView(TemplateView):
    template_name="posts/about.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class ContactView(TemplateView):
    template_name="posts/contact.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

def dashboard(request):
    if request.user.is_authenticated:
        post= Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        context = {
            'post':post,
            'full_name': full_name,
            'groups': gps
        }
        return render(request, "posts/dashboard.html", context)
    else:
        return HttpResponseRedirect('/login/')

def user_signup(request):
    if request.method =="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
            messages.success(request, 'Registration Successful as Author')
            return HttpResponseRedirect('/login/')
    else:
        form = SignUpForm()
    context = {'form':form}
    return render(request, 'posts/signup.html', context )


def user_login(request):
    if not request.user.is_authenticated:
        if request.method =="POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Login Successful")
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        context = {'form': form}
        return render(request, 'posts/login.html',context)
    else:
        return HttpResponseRedirect('/dashboard/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def add_post(request):
    if request.user.is_authenticated:
        if request.method =="POST":
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                body = form.cleaned_data['body']
                p = Post(title=title, body=body)
                p.save()
                messages.success(request, "Post Successful")
                form=PostForm()
        else:
            form = PostForm()
        context = {'form': form}
        return render(request, 'posts/addpost.html',context)
    else:
        return HttpResponseRedirect('/login/')


def update_post(request,pk):
    if request.user.is_authenticated:
        if request.method =="POST":
            pi= Post.objects.get(id=pk)
            form = PostForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
                messages.success(request, "Post Update Successful")
                return HttpResponseRedirect('/dashboard/')
        else:
            pi= Post.objects.get(id=pk)
            form = PostForm(instance=pi)
        context = {'form': form}
        return render(request, 'posts/updatepost.html', context)
    else:
        return HttpResponseRedirect('/login/')


def delete_post(request,pk):
    if request.user.is_authenticated:
        if request.method =="POST":
            pi= Post.objects.get(id=pk)
            pi.delete()
            messages.success(request, "Post Deleted Successful")
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')