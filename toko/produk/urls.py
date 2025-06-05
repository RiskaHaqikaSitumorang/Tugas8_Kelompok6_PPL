from django.urls import path
from . import views

app_name = 'produk'

urlpatterns = [
    path('', views.daftar_produk, name='daftar_produk'),
    path('tambah/', views.tambah_produk, name='tambah_produk'),
    path('<int:id>/edit/', views.edit_produk, name='edit_produk'),
    path('<int:id>/hapus/', views.hapus_produk, name='hapus_produk'),
]
