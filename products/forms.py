from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'product_type', 'condition', 'price', 'is_free', 'payment_method', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describe your product'}),
            'product_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Electronics, Books, Furniture'}),
            'condition': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price', 'step': '0.01', 'id': 'id_price'}),
            'is_free': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'id_is_free'}),
            'payment_method': forms.Select(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control-file', 'accept': 'image/*'}),
        }