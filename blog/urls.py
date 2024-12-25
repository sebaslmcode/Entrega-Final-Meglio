# blog/urls.py

from django.urls import path
from .views import register, posts, add_post, delete_post, logout_view, login_view, edit_post, about, profile, edit_profile

urlpatterns = [
    path('register/', register, name='register'),
    path('posts/', posts, name='posts'),
    path('add_post/', add_post, name='add_post'),
    path('edit_post/<int:post_id>/', edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', delete_post, name='delete_post'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('about/', about, name='about'),
    path('profile/', profile, name='profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),  # Asegúrate de que esta línea esté presente
]