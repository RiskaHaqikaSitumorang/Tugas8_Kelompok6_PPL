# produk/forms.py
from django import forms
from .models import Produk

class ProdukForm(forms.ModelForm):
    class Meta:
        model = Produk
        fields = ['nama', 'deskripsi', 'harga', 'stok', 'gambar']
        widgets = {
            'deskripsi': forms.Textarea(attrs={'rows': 3}),
        }