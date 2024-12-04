from django import forms
from .models import Post, Author, Category

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'bio']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class PostForm(forms.ModelForm):
    author_name = forms.CharField(max_length=100, required=True, label="Nombre del Autor")
    category_name = forms.CharField(max_length=100, required=True, label="Nombre de la Categoría")

    class Meta:
        model = Post
        fields = ['title', 'content']  # Excluimos author y category de aquí

    def save(self, commit=True):
        post = super().save(commit=False)
        # Obtener o crear el autor
        author_name = self.cleaned_data['author_name']
        author, created = Author.objects.get_or_create(name=author_name)
        post.author = author

        # Obtener o crear la categoría
        category_name = self.cleaned_data['category_name']
        category, created = Category.objects.get_or_create(name=category_name)
        post.category = category

        if commit:
            post.save()
        return post