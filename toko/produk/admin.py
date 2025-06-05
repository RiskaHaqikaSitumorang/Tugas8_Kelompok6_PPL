# produk/admin.py
from django.contrib import admin
from .models import Produk

@admin.register(Produk)
class ProdukAdmin(admin.ModelAdmin):
    list_display = ('nama', 'harga', 'stok')
    search_fields = ('nama',)