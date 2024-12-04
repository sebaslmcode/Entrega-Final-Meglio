from django.urls import path
from .views import index, add_post, edit_post, delete_post, search_posts

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_post, name='add_post'),
    path('edit/<int:post_id>/', edit_post, name='edit_post'),
    path('delete/<int:post_id>/', delete_post, name='delete_post'),
    path('search/', search_posts, name='search_posts'),
]