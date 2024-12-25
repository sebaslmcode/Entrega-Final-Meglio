# blog/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Post, Profile
from .forms import UserRegistrationForm, PostForm, ProfileForm

def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)  # Crear un perfil para el nuevo usuario
            login(request, user)
            return redirect('profile')  # Redirige al perfil después de registrarse
    else:
        form = UserRegistrationForm()
    return render(request, 'blog/register.html', {'form': form})

def posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/posts.html', {'posts': posts})

@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts')
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'post_form': form})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('posts')
    return render(request, 'blog/delete_post.html', {'post': post})

def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')  # Redirige al perfil después de iniciar sesión
        else:
            return render(request, 'blog/login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'blog/login.html')

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'post_form': form, 'post': post})

@login_required
def profile(request):
    return render(request, 'blog/profile.html')  # Asegúrate de que esta plantilla exista

@login_required
def edit_profile(request):
    try:
        profile = request.user.profile  # Intenta obtener el perfil del usuario
    except Profile.DoesNotExist:
        # Si no existe, redirige a la página de perfil o crea uno nuevo
        return redirect('profile')  # O puedes redirigir a una vista para crear un perfil

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirige al perfil después de editar
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'blog/edit_profile.html', {'form': form})