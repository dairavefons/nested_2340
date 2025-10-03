from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.filter(is_claimed=False).order_by('-created_at')
    return render(request, 'products/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id, is_claimed=False)
    return render(request, 'products/post_detail.html', {'post': post})

def create_post(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'You need to sign in to add a listing.')
        return redirect('login')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Your post has been created successfully!')
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'products/create_post.html', {'form': form})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.author != request.user:
        messages.error(request, 'You do not have permission to edit this post.')
        return redirect('post_detail', post_id=post.id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your post has been updated successfully!')
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'products/edit_post.html', {'form': form, 'post': post})

@login_required
def claim_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id, is_claimed=False)

        if post.author == request.user:
            messages.error(request, 'You cannot claim your own item.')
            return redirect('post_detail', post_id=post.id)

        post.is_claimed = True
        post.claimed_by = request.user
        post.save()
        messages.success(request, f'You have successfully claimed "{post.title}"!')
    except Post.DoesNotExist:
        messages.error(request, 'This post is no longer available.')
    return redirect('post_list')
