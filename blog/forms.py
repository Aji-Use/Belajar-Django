from django import forms
from .models import Post

# class CreatePost(forms.Form):
#     title = forms.CharField(max_length=255)
#     linkImg = forms.URLField()
#     body = forms.CharField()
#     receipes = forms.CharField()
#     category = forms.CharField(max_length=255)
    

# Bisa auto create slug, karena mengambil fungsi save pada models
class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'linkImg', 'body', 'receipes', 'category']
        labels = {
            'title': 'Judul Postingan',
            'linkImg': 'URL Gambar',
            'body': 'Deskripsi',
            'receipes': 'Resep Masakan',
            'category': 'Kategori',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'linkImg': forms.URLInput(attrs={'class': 'form-control',
                                             'placeholder': 'https://img-global.cpcdn.com/recipes/a838e3e7d6d9f6f8/1280x1280sq80/photo.webp',
                                             }),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'receipes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
        }