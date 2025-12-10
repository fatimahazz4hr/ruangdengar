# Panduan Setup Google OAuth untuk Ruang Dengar

## Langkah 1: Install Dependencies

```bash
pip install django-allauth
```

## Langkah 2: Migrasi Database

```bash
python manage.py migrate
```

## Langkah 3: Setup Google Cloud Console

1. **Buka Google Cloud Console**
   - Pergi ke: https://console.cloud.google.com/

2. **Buat Project Baru** (atau gunakan yang sudah ada)
   - Klik "Select a project" di bagian atas
   - Klik "NEW PROJECT"
   - Nama project: "Ruang Dengar OAuth"
   - Klik "CREATE"

3. **Enable Google+ API**
   - Di dashboard, cari "APIs & Services"
   - Klik "Enable APIs and Services"
   - Cari "Google+ API"
   - Klik "ENABLE"

4. **Buat OAuth 2.0 Credentials**
   - Di sidebar, pilih "Credentials"
   - Klik "CREATE CREDENTIALS" → "OAuth client ID"
   - Jika diminta, konfigurasi OAuth consent screen terlebih dahulu:
     - User Type: External
     - App name: Ruang Dengar
     - User support email: email Anda
     - Developer contact email: email Anda
     - Klik "SAVE AND CONTINUE"
   
5. **Configure OAuth Client**
   - Application type: Web application
   - Name: Ruang Dengar Web Client
   - Authorized JavaScript origins:
     - http://localhost:8000
     - http://127.0.0.1:8000
   - Authorized redirect URIs:
     - http://localhost:8000/accounts/google/login/callback/
     - http://127.0.0.1:8000/accounts/google/login/callback/
   - Klik "CREATE"

6. **Simpan Credentials**
   - Akan muncul popup dengan:
     - Client ID: `xxx.apps.googleusercontent.com`
     - Client Secret: `xxx`
   - **JANGAN TUTUP** popup ini dulu, atau copy kedua nilai tersebut

## Langkah 4: Konfigurasi Django Admin

1. **Jalankan Server**
   ```bash
   python manage.py runserver
   ```

2. **Login ke Admin**
   - Buka: http://localhost:8000/admin/
   - Login dengan akun superuser

3. **Tambah Social Application**
   - Di sidebar, cari "Sites" → klik "Sites"
   - Pastikan ada entry dengan domain "example.com" (ID biasanya 1)
   - Jika belum, edit menjadi "localhost:8000"
   
4. **Konfigurasi Google Provider**
   - Kembali ke home admin
   - Cari "Social applications" → klik "Add"
   - Provider: Google
   - Name: Google OAuth
   - Client id: [paste Client ID dari Google Console]
   - Secret key: [paste Client Secret dari Google Console]
   - Sites: Pilih "localhost:8000" atau "example.com" (pindahkan ke "Chosen sites")
   - Klik "SAVE"

## Langkah 5: Testing

1. Logout dari admin
2. Buka halaman login: http://localhost:8000/login/
3. Klik tombol Google (yang sudah ada logo Google berwarna)
4. Pilih akun Google
5. Seharusnya redirect ke dashboard setelah login berhasil

## Langkah 6: Production Setup (Untuk Deployment)

Ketika deploy ke production (misalnya di Heroku, Railway, atau server lain):

1. **Update Google Console**
   - Tambahkan production URL ke Authorized origins:
     - https://yourdomain.com
   - Tambahkan production callback:
     - https://yourdomain.com/accounts/google/login/callback/

2. **Update Django Sites**
   - Di admin production, update Site domain menjadi domain production Anda

3. **Environment Variables**
   - Simpan Client ID dan Secret di environment variables
   - Update `settings.py`:
   ```python
   SOCIALACCOUNT_PROVIDERS = {
       'google': {
           'APP': {
               'client_id': os.environ.get('GOOGLE_CLIENT_ID'),
               'secret': os.environ.get('GOOGLE_CLIENT_SECRET'),
           }
       }
   }
   ```

## Troubleshooting

### Error: "redirect_uri_mismatch"
- Pastikan URL callback di Google Console sama persis dengan yang digunakan
- Format harus: `http://localhost:8000/accounts/google/login/callback/`
- Jangan lupa trailing slash `/` di akhir

### Error: "Site matching query does not exist"
- Jalankan: `python manage.py migrate`
- Atau manual create site di admin

### Error: "SocialApp matching query does not exist"
- Pastikan sudah tambah Social Application di Django admin
- Provider harus "Google" (bukan "google")

### Tombol Google tidak muncul
- Clear browser cache
- Hard refresh: Ctrl+Shift+R

### Login berhasil tapi tidak redirect
- Cek `LOGIN_REDIRECT_URL` di `settings.py`
- Pastikan URL 'dashboard' sudah terdaftar di `urls.py`

## File yang Sudah Dimodifikasi

1. `requirements.txt` - Tambah django-allauth
2. `ruangdengar/settings.py` - Konfigurasi allauth
3. `ruangdengar/urls.py` - Tambah allauth URLs
4. `templates/users/login.html` - Update tombol Google dengan logo proper

## Catatan Penting

- Client Secret harus dijaga kerahasiaannya
- Jangan commit Client ID dan Secret ke Git
- Untuk production, gunakan HTTPS
- Email dari Google akan otomatis tersimpan di user profile
