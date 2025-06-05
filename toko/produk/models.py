# produk/models.py
from django.db import models

class Produk(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField(blank=True)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    stok = models.IntegerField(default=0)
    gambar = models.ImageField(upload_to='produk/', blank=True, null=True)
    dibuat_pada = models.DateTimeField(auto_now_add=True)
    diperbarui_pada = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nama} (Rp{self.harga})"