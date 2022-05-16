from django import forms
from .models import Post, Category


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'header_image', 'title_tag', 'category', 'body')
        labels = {
            'title': 'Título',
            'header_image': 'Imagem',
            'title_tag': 'Tag',
            'category': 'Categoria',
            'body': 'Publicação',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título da postagem'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tipo de assunto'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escreva aqui...'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'category', 'body']
        labels = {
            'title': 'Título',
            'title_tag': 'Tag',
            'category': 'Categoria',
            'body': 'Publicação',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título da postagem'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tipo de ssunto'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escreva aqui...'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']
        labels = {
            'category_name': 'Nome da categoria',
        }

        widgets = {
            'category_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
