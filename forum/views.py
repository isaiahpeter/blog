from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Post, Comment
from .forms import PostForm, EditForm
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def post_list(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    posts = Post.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category=category)
    return render(request, 'forum/post/list.html', {'category': category, 'categories': categories, 'posts': posts})

def post_detail(request, year, month, day,post):
    post = get_object_or_404(Post,status=Post.Status.PUBLISHED, slug=post, publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'forum/post/detail.html', {'post': post})



def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            category_slug = post.category.slug
            categories = Category.objects.all()
            category = get_object_or_404(Category, slug=category_slug)
            return HttpResponseRedirect(reverse('forum:post_list', args=None))
    else:
        form = PostForm()        
    return render(request, 'forum/post/post_new.html', {'form':form })


def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('post_detail', args=(post.publish.year, post.publish.month, post.publish.day, post.slug)))
    else:
        form = PostForm(instance=post)
    return render(request, 'forum/post/post_edit.html', {'form': form, 'post':post})
