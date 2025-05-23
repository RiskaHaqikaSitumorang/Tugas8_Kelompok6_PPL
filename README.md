# Tugas9_Kelompok6_PPL
# Manajemen Produk Django - Dokumentasi

## 📋 Deskripsi Proyek
Sistem manajemen produk berbasis web dengan fitur CRUD (Create, Read, Update, Delete) menggunakan Django.

## ✨ Fitur Utama
- ✅ Tambah produk baru dengan gambar
- ✅ Daftar semua produk
- ✅ Edit informasi produk
- ✅ Hapus produk 
- ✅ Notifikasi aksi sukses/gagal

## 🛠️ Teknologi Digunakan
- Python 3.x
- Django 4.x
- Bootstrap 5
- Font Awesome 6
- Pillow (untuk pengolahan gambar)

## 🚀 Cara Instalasi

### 1. Clone Repository
```bash
git clone https://github.com/RiskaHaqikaSitumorang/Tugas9_Kelompok6_PPL.git
cd repo-manajemen-produk
```

### 2. Buat Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies
```bash
pip install django
```

### 4. Migrasi Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Buat Superuser
```bash
python manage.py createsuperuser
```

### 6. Jalankan Server
```bash
python manage.py runserver
```

Buka http://localhost:8000 di browser Anda.

## 📂 Struktur Direktori
```
manajemen-produk/
├── produk/
│   ├── migrations/
│   ├── templates/
│   │   ├── produk/
│   │   │   ├── base.html
│   │   │   ├── daftar.html
│   │   │   ├── form.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── manajemen_produk/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── media/
├── static/
├── manage.py
└── requirements.txt
```

## 🖼️ Screenshots

### Halaman Daftar Produk
![image](https://github.com/user-attachments/assets/0255e8f2-3fff-4e14-8a5f-1f76a152faed)


### Form Tambah Produk
![image](https://github.com/user-attachments/assets/2c4f1d0c-bc54-4279-9fa0-a88169994d77)

### Form Edit Produk
![image](https://github.com/user-attachments/assets/4b70ac6f-1c1e-4386-a5b7-b7b4a16a84e1)


## 👥 Kontributor

| Nama | NPM | 
|------|-----|
| Berliani Utami | 2208107010082 |
| Raihan Firyal | 2208107010084 |
| Riska Haqika Situmorang | 2208107010086 | 

## 📝 Lisensi
Proyek ini dilisensikan di bawah MIT License - lihat file [LICENSE](LICENSE) untuk detail lebih lanjut.

