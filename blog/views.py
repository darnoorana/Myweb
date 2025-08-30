
# Create your views here.

# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import BlogPost, Comment
from .forms import BlogPostForm, CommentForm

def blog_list(request):
    """قائمة المقالات"""
    posts = BlogPost.objects.filter(is_published=True)
    search_query = request.GET.get('search')
    
    if search_query:
        posts = posts.filter(
            Q(title__icontains=search_query) | 
            Q(content__icontains=search_query)
        )
    
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    return render(request, 'blog/blog_list.html', {
        'posts': posts,
        'search_query': search_query
    })

def post_detail(request, slug):
    """تفاصيل المقالة"""
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    post.views_count += 1
    post.save()
    
    comments = post.comments.filter(is_approved=True)
    
    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'تم إضافة تعليقك بنجاح!')
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = CommentForm()
    
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })

@login_required
def create_post(request):
    """إنشاء مقالة جديدة"""
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'تم إنشاء المقالة بنجاح!')
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = BlogPostForm()
    
    return render(request, 'blog/create_post.html', {'form': form})

@login_required
def edit_post(request, slug):
    """تعديل المقالة"""
    post = get_object_or_404(BlogPost, slug=slug, author=request.user)
    
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم تحديث المقالة بنجاح!')
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = BlogPostForm(instance=post)
    
    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})

@login_required
def delete_post(request, slug):
    """حذف المقالة"""
    post = get_object_or_404(BlogPost, slug=slug, author=request.user)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'تم حذف المقالة بنجاح!')
        return redirect('blog:blog_list')
    
    return render(request, 'blog/delete_post.html', {'post': post})

@login_required
def my_posts(request):
    """مقالاتي"""
    posts = BlogPost.objects.filter(author=request.user)
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    return render(request, 'blog/my_posts.html', {'posts': posts})

