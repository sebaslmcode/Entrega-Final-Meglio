# README

## MiPrimeraPagina_Meglio

Este proyecto es un blog simple desarrollado con Django. A continuación se detalla el orden en el que se pueden probar las funcionalidades y la estructura del proyecto.

### Estructura del Proyecto

- **blog/**: Carpeta que contiene la aplicación del blog.
  - **migrations/**: Migraciones de la base de datos.
  - **templates/**: Plantillas HTML para las vistas.
    - **blog/**: Plantillas específicas de la aplicación blog.
      - `base.html`: Plantilla base que incluye la estructura general del sitio.
      - `home.html`: Página de inicio del blog.
      - `posts.html`: Muestra la lista de posts.
      - `add_post.html`: Formulario para agregar un nuevo post.
      - `edit_post.html`: Formulario para editar un post existente.
      - `delete_post.html`: Confirmación para eliminar un post.
      - `login.html`: Formulario de inicio de sesión.
      - `register.html`: Formulario de registro de nuevos usuarios.
      - `profile.html`: Muestra el perfil del usuario.
      - `edit_profile.html`: Formulario para editar el perfil del usuario.
      - `about.html`: Página con información sobre el autor del blog.
  - **forms.py**: Define los formularios utilizados en la aplicación.
  - **models.py**: Define los modelos de datos (Post, Author, Category, Profile).
  - **views.py**: Contiene las vistas que manejan la lógica del negocio.
  
- **MiPrimeraPagina_Meglio/**: Carpeta principal del proyecto.
  - `urls.py`: Define las rutas de la aplicación.
  - `settings.py`: Configuración del proyecto Django.
  - `wsgi.py`: Configuración para el despliegue WSGI.

### Funcionalidades

1. **Inicio (Página de Inicio)**:
   - Accede a la página de inicio en la URL raíz (`/`).
   - Presenta un mensaje de bienvenida y enlaces a las secciones del blog.

2. **Lista de Posts**:
   - Accede a la lista de posts en `/posts/`.
   - Puedes buscar posts utilizando el formulario de búsqueda.
   - Cada post tiene enlaces para editar y eliminar.

3. **Agregar Nuevo Post**:
   - Accede a la página para agregar un nuevo post en `/add_post/`.
   - Completa el formulario con el título, contenido, nombre del autor y nombre de la categoría.
   - Al enviar el formulario, se guardará el nuevo post y se redirigirá a la lista de posts.

4. **Editar Post**:
   - Desde la lista de posts, haz clic en "Editar" junto al post que deseas modificar.
   - Accede a la página de edición en `/edit_post/<post_id>/`.
   - Realiza los cambios necesarios y guarda para actualizar el post.

5. **Eliminar Post**:
   - Desde la lista de posts, haz clic en "Eliminar" junto al post que deseas borrar.
   - Accede a la página de confirmación en `/delete_post/<post_id>/`.
   - Confirma la eliminación del post.

6. **Registro de Usuarios**:
   - Accede a la página de registro en `/register/`.
   - Completa el formulario para crear una nueva cuenta de usuario.

7. **Inicio de Sesión**:
   - Accede a la página de inicio de sesión en `/login/`.
   - Ingresa tus credenciales para acceder a tu cuenta.

8. **Perfil de Usuario**:
   - Accede a tu perfil en `/profile/`.
   - Puedes ver y editar tu información personal.

9. **Acerca de**:
   - Accede a la página "Acerca de Mí" en `/about/` para conocer más sobre el autor del blog.

### Instrucciones para Probar el Proyecto

1. **Configuración del Entorno**:
   - Asegúrate de tener Python y Django instalados.
   - Clona el repositorio y navega a la carpeta del proyecto.

2. **Instalación de Dependencias**:
   - Ejecuta `pip install -r requirements.txt` para instalar las dependencias necesarias.

3. **Migraciones de Base de Datos**:
   - Ejecuta `python manage.py migrate` para aplicar las migraciones y crear la base de datos.

4. **Ejecutar el Servidor**:
   - Ejecuta `python manage.py runserver` para iniciar el servidor de desarrollo.

5. **Acceso a la Aplicación**:
   - Abre tu navegador y ve a `http://127.0.0.1:8000/` para acceder a la aplicación.

### Notas

- Asegúrate de que el archivo `settings.py` esté configurado correctamente
