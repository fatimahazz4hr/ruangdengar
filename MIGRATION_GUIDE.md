# Panduan Migrasi Database ke PostgreSQL

## Langkah-langkah Migrasi

### 1. Backup Data dari SQLite (Database saat ini)

Pastikan database masih menggunakan SQLite, kemudian jalankan:

```powershell
python migrate_to_postgres.py
```

Script ini akan membuat file `data_backup.json` berisi semua data.

### 2. Install PostgreSQL

- Download PostgreSQL dari: https://www.postgresql.org/download/windows/
- Install dengan pengaturan default
- **CATAT PASSWORD** yang kamu set untuk user `postgres`
- Port default: 5432

### 3. Buat Database Baru

Buka **pgAdmin** atau **SQL Shell (psql)** dan jalankan:

```sql
CREATE DATABASE ruangdengar_db;
```

### 4. Install Package Python untuk PostgreSQL

```powershell
pip install psycopg2-binary
```

### 5. Update settings.py

Edit `ruangdengar/settings.py` dan ganti password PostgreSQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ruangdengar_db',
        'USER': 'postgres',
        'PASSWORD': 'password_kamu_disini',  # ← GANTI INI
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

**PENTING:** File `settings.py` sudah diupdate, tinggal ganti bagian `PASSWORD` saja!

### 6. Migrate Schema ke PostgreSQL

```powershell
python manage.py migrate
```

### 7. Import Data ke PostgreSQL

```powershell
python manage.py loaddata data_backup.json
```

### 8. Jalankan Server

```powershell
python manage.py runserver
```

### 9. Test

Buka browser dan akses `http://127.0.0.1:8000`
- Login dengan user yang sama seperti di SQLite
- Semua data (users, bookings, laporan) harus sudah ter-import

---

## Troubleshooting

### Error: "role postgres does not exist"
```powershell
# Buka psql sebagai superuser dan buat role
CREATE USER postgres WITH PASSWORD 'your_password' SUPERUSER;
```

### Error: "database ruangdengar_db does not exist"
```powershell
# Buat database
CREATE DATABASE ruangdengar_db;
```

### Error: "psycopg2 not installed"
```powershell
pip install psycopg2-binary
```

### Error saat loaddata
Jika ada error foreign key atau duplicate:
```powershell
# Hapus database dan buat ulang
DROP DATABASE ruangdengar_db;
CREATE DATABASE ruangdengar_db;

# Migrate ulang
python manage.py migrate
python manage.py loaddata data_backup.json
```

### Kembali ke SQLite (Rollback)

Edit `ruangdengar/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

---

## Verifikasi Migrasi Berhasil

Cek apakah data sudah masuk:

```powershell
python manage.py shell
```

```python
from users.models import CustomUser, Booking, Laporan, Counselor

# Cek jumlah data
print(f"Users: {CustomUser.objects.count()}")
print(f"Bookings: {Booking.objects.count()}")
print(f"Laporan: {Laporan.objects.count()}")
print(f"Counselors: {Counselor.objects.count()}")
```

---

## Keuntungan PostgreSQL

✅ **Performance lebih baik** untuk aplikasi production
✅ **Concurrent access** lebih stabil (multi-user)
✅ **Data integrity** lebih kuat
✅ **Full-text search** lebih powerful
✅ **JSON field support** native
✅ **Production ready** untuk deployment

---

## File Penting

- `data_backup.json` - Backup data dari SQLite (jangan dihapus!)
- `db.sqlite3` - Database SQLite lama (backup)
- `ruangdengar/settings.py` - Konfigurasi database

---

**TIPS:** Simpan file `data_backup.json` sebagai backup. Jika ada masalah, kamu bisa restore data dengan mudah.
