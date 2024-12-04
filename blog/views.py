from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})

def add_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('index')  # Redirige a la lista de posts después de guardar
    else:
        post_form = PostForm()
    
    return render(request, 'blog/add_post.html', {'post_form': post_form})

def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('index')
    else:
        post_form = PostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'post_form': post_form, 'post': post})

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    return render(request, 'blog/delete_post.html', {'post': post})

def search_posts(request):
    query = request.GET.get('q')
    posts = Post.objects.filter(title__icontains=query)
    return render(request, 'blog/index.html', {'posts': posts})