# produk/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Produk
from .forms import ProdukForm
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST

def daftar_produk(request):
    produk_list = Produk.objects.all().order_by('-dibuat_pada')
    return render(request, 'produk/daftar.html', {'produk_list': produk_list})

def tambah_produk(request):
    if request.method == 'POST':
        form = ProdukForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produk berhasil ditambahkan!')
            return redirect('produk:daftar_produk')
    else:
        form = ProdukForm()
    return render(request, 'produk/form.html', {'form': form, 'action': 'Tambah'})

def edit_produk(request, id):
    produk = get_object_or_404(Produk, pk=id)
    if request.method == 'POST':
        form = ProdukForm(request.POST, request.FILES, instance=produk)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produk berhasil diperbarui!')
            return redirect('produk:daftar_produk')  # Gunakan namespace
    else:
        form = ProdukForm(instance=produk)
    return render(request, 'produk/form.html', {
        'form': form,
        'action': 'Edit'
    })
@require_POST
def hapus_produk(request, id):
    produk = get_object_or_404(Produk, pk=id)
    nama_produk = produk.nama
    produk.delete()
    messages.success(request, f'Produk "{nama_produk}" berhasil dihapus!')
    return redirect('produk:daftar_produk')

