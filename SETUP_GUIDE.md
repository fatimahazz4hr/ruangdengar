# 🚀 Setup Guide - Ruang Dengar PPKPT

Panduan lengkap untuk menjalankan project ini di komputer lain.

---

## 📋 Prerequisites (Yang Harus Diinstall Dulu)

1. **Python 3.11+** - [Download disini](https://www.python.org/downloads/)
2. **PostgreSQL 14+** - [Download disini](https://www.postgresql.org/download/)
3. **Git** (opsional) - Untuk clone repository

---

## 🔧 Langkah Setup

### 1. Extract Project
```bash
# Extract file zip ke folder yang diinginkan
# Contoh: C:\Projects\ruangdengar
```

### 2. Buat Virtual Environment
```bash
# Buka terminal/PowerShell di folder project
python -m venv myenv

# Aktivasi virtual environment
# Windows PowerShell:
myenv\Scripts\Activate.ps1

# Windows CMD:
myenv\Scripts\activate.bat
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

**Jika requirements.txt tidak ada, install manual:**
```bash
pip install django==5.2.7
pip install psycopg2-binary
pip install pillow
pip install django-allauth
pip install openai
```

### 4. Setup Database PostgreSQL

**A. Buat Database Baru:**
```sql
-- Login ke PostgreSQL (pgAdmin atau psql)
CREATE DATABASE ruangdengar_db;
```

**B. Buat User Database:**
```sql
CREATE USER postgres WITH PASSWORD 'yourpassword';
GRANT ALL PRIVILEGES ON DATABASE ruangdengar_db TO postgres;
```

**C. Edit File Settings:**
Buka `ruangdengar/settings.py`, cari section DATABASES:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ruangdengar_db',
        'USER': 'postgres',  # Sesuaikan
        'PASSWORD': 'yourpassword',  # Ganti dengan password kamu
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Setup Environment Variables (PENTING!)

**Buat file `.env` di root project:**
```env
# Django
SECRET_KEY=your-secret-key-here-generate-random-string
DEBUG=True

# Database
DB_NAME=ruangdengar_db
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432

# Google Gemini (untuk AI Moderation - GRATIS!)
GEMINI_API_KEY=AIzaSyD-your-gemini-api-key-here

# Microsoft OAuth (opsional)
MICROSOFT_CLIENT_ID=your-client-id
MICROSOFT_CLIENT_SECRET=your-client-secret
```

**Generate SECRET_KEY:**
```python
# Jalankan di Python shell:
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### 6. Jalankan Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Buat Superuser (Admin Pertama)
```bash
python manage.py createsuperuser
# Ikuti instruksi untuk create admin account
```

**ATAU gunakan custom command:**
```bash
python manage.py create_admin
```

### 8. Load Data Backup (Opsional)
```bash
# Jika ada file data_backup.json
python manage.py loaddata data_backup.json
```

### 9. Jalankan Server
```bash
python manage.py runserver
```

Buka browser: **http://127.0.0.1:8000/**

---

## 📁 Struktur Folder Yang Harus Ada

```
ruangdengar/
├── manage.py
├── requirements.txt
├── .env (buat sendiri)
├── db.sqlite3 (otomatis dibuat)
├── ruangdengar/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── users/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ai_moderation.py
├── templates/
├── static/
└── media/ (otomatis dibuat)
```

---

## ⚙️ Konfigurasi Microsoft OAuth (Opsional)

Jika ingin login dengan Microsoft/Telkom University:

1. Ikuti panduan di `MICROSOFT_OAUTH_SETUP.md`
2. Update `.env` dengan Client ID dan Secret
3. Tambahkan Redirect URI di Azure Portal:
   - `http://localhost:8000/accounts/microsoft/login/callback/`

---

## 🚨 Troubleshooting

### Error: "No module named 'psycopg2'"
```bash
pip install psycopg2-binary
```

### Error: Database connection failed
- Pastikan PostgreSQL service running
- Cek username/password di settings.py
- Cek database sudah dibuat

### Error: "GEMINI_API_KEY not found"
- Daftar gratis di https://aistudio.google.com/app/apikey
- Lihat panduan lengkap di `GEMINI_SETUP.md`
- AI moderation tetap jalan dengan fallback keyword-based (tanpa AI)

### Error: Static files not loading
```bash
python manage.py collectstatic
```

### Port 8000 sudah digunakan
```bash
python manage.py runserver 8080
```

---

## 📦 Files Yang TIDAK Perlu Di-Zip

Sebelum zip project, **HAPUS** folder/file ini (akan di-generate ulang):

- `myenv/` - Virtual environment (terlalu besar)
- `__pycache__/` - Python bytecode
- `*.pyc` - Compiled Python files
- `db.sqlite3` - Database lokal (kecuali mau backup)
- `.env` - Contains secrets (JANGAN DI-SHARE!)
- `media/` - User uploads (kecuali butuh data testing)

**Command untuk clean sebelum zip:**
```powershell
# PowerShell
Remove-Item -Recurse -Force myenv, __pycache__, *.pyc, db.sqlite3, .env
```

---

## 🎯 Quick Start (Ringkasan)

```bash
# 1. Extract & masuk folder
cd ruangdengar

# 2. Buat virtual env & aktivasi
python -m venv myenv
myenv\Scripts\Activate.ps1

# 3. Install dependencies
pip install -r requirements.txt

# 4. Setup database (buat di PostgreSQL dulu!)
python manage.py migrate

# 5. Buat admin
python manage.py create_admin

# 6. Run server
python manage.py runserver
```

**Done! Buka http://127.0.0.1:8000/** 🎉

---

## 📞 Support

Jika ada masalah:
1. Cek error message di terminal
2. Pastikan semua prerequisites sudah installed
3. Cek file `.env` sudah benar
4. Cek PostgreSQL service running

---

## 📝 Notes

- Default admin: Buat via `python manage.py create_admin`
- Database: PostgreSQL (production) atau SQLite (testing)
- AI Moderation: Butuh OpenAI API key
- OAuth: Butuh Microsoft Azure App registration

**Happy Coding! 🚀**
