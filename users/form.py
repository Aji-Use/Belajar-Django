from django import forms
from .models import Administrator

choise=['bos', 'staff']
class AdministratorForm(forms.ModelForm):
    class Meta:
        model = Administrator
        fields = ['picture', 'username', 'email', 'password', 'position']
        widgets = {
            'picture': forms.URLInput(attrs={'class': 'form-control',
                                             'placeholder': 'https://img-global.cpcdn.com/recipes/a838e3e7d6d9f6f8/1280x1280sq80/photo.webp',
                                             }),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'rows': 3}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'rows': 3}),
            'position': forms.Select(choices=[
                ('bos', 'Bos'),
                ('sekretaris', 'Sekretaris'),
                ('karyawan', 'Karyawan'),
            ],attrs={'class': 'form-control'}),
        }
        