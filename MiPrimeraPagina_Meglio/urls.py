from django.contrib import admin
from django.urls import path, include
from blog.views import home  # Asegúrate de importar la vista home

urlpatterns = [
    path('', home, name='home'),  # Esta línea es crucial para la URL raíz
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Incluye las URLs de la aplicación blog
]