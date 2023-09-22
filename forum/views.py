from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Post, Comment
from .forms import PostForm, EditForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from accounts.models import CustomUser
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def home(request):
    """The home page ."""
    return render(request, 'forum/home.html')


def post_list(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get('page')
    try:   
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            posts = posts.filter(category=category)
    return render(request, 'forum/post/list.html', {'category': category, 'categories': categories, 'posts': posts})

def post_detail(request, year, month, day,post):
    post = get_object_or_404(Post,status=Post.Status.PUBLISHED, slug=post, publish__year=year, publish__month=month, publish__day=day)
    comments = post.comments.filter(active=True)
    form = CommentForm()
    return render(request, 'forum/post/detail.html', {'post': post, 'comments': comments, 'form': form})


@login_required
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

@login_required
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = EditForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            post.author = request.user
            return HttpResponseRedirect(reverse('forum:post_detail', args=(post.publish.year, post.publish.month, post.publish.day, post.slug)))
    else:
        form = EditForm(instance=post)
    return render(request, 'forum/post/post_edit.html', {'form': form, 'post':post})
@login_required
def post_delete(request, slug):
    post = get_object_or_404(Post,slug=slug)
    if request.method == 'POST' and request.POST:
        post.delete()
        return HttpResponseRedirect(reverse('forum:post_list', args=None))
    return render(request, 'forum/post/post_delete.html', {'post':post})
    


@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.author = request.user
        comment.save()
    return render(request, 'forum/post/comment.html',
                           {'post': post,
                            'form':form,
                            'comment':comment})
                            

@login_required
@require_POST
def post_like(request):
    post_id = request.POST.get('id')
    action = request.POST.get('action')
    if post_id and action:
        try:
            post = Post.objects.get(id=post_id)
            if action == 'like':
                post.users_like.add(request.user)
            else:
                post.users_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except Post.DoesNotExist:
            pass
        return JsonResponse({'status': 'error'})
            
