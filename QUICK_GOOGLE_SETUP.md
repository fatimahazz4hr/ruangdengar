# Setup Google Login - Langkah Cepat

## ✅ Yang Sudah Selesai:
1. Library django-allauth terinstall
2. Database migrations sudah dijalankan
3. Tombol Google di halaman login sudah ada logo Google yang proper
4. Server Django sudah running

## 🔧 Yang Perlu Anda Lakukan:

### Step 1: Buka Google Cloud Console
1. Pergi ke: https://console.cloud.google.com/
2. Login dengan akun Google Anda

### Step 2: Buat Project Baru
1. Klik dropdown project di bagian atas (Select a project)
2. Klik "NEW PROJECT"
3. Nama project: **Ruang Dengar**
4. Klik "CREATE"

### Step 3: Enable Google+ API
1. Di menu sebelah kiri, klik "APIs & Services" → "Library"
2. Cari: **Google+ API**
3. Klik hasil pencarian, lalu klik tombol **"ENABLE"**

### Step 4: Setup OAuth Consent Screen
1. Di menu kiri, klik "OAuth consent screen"
2. Pilih **External**, klik "CREATE"
3. Isi form:
   - App name: **Ruang Dengar**
   - User support email: (pilih email Anda)
   - Developer contact email: (isi email Anda)
4. Klik "SAVE AND CONTINUE"
5. Di halaman "Scopes", klik "SAVE AND CONTINUE" (tidak perlu tambah scope)
6. Di halaman "Test users", klik "SAVE AND CONTINUE"
7. Klik "BACK TO DASHBOARD"

### Step 5: Buat OAuth Credentials
1. Di menu kiri, klik "Credentials"
2. Klik tombol "CREATE CREDENTIALS" → pilih **"OAuth client ID"**
3. Application type: **Web application**
4. Name: **Ruang Dengar Web Client**
5. Di "Authorized JavaScript origins", klik "ADD URI":
   ```
   http://localhost:8000
   ```
6. Di "Authorized redirect URIs", klik "ADD URI":
   ```
   http://localhost:8000/accounts/google/login/callback/
   ```
7. Klik **"CREATE"**

### Step 6: Copy Client ID & Secret
Akan muncul popup dengan:
- **Client ID**: xxx.apps.googleusercontent.com
- **Client secret**: xxx

**JANGAN TUTUP POPUP INI! Copy kedua nilai tersebut.**

### Step 7: Konfigurasi di Django Admin
1. Buka browser: http://localhost:8000/admin/
2. Login dengan akun superuser admin Anda
3. Cari **"Sites"** di sidebar → klik
4. Klik entry yang ada (biasanya "example.com")
5. Edit:
   - Domain name: **localhost:8000**
   - Display name: **Ruang Dengar**
6. Klik "SAVE"

### Step 8: Tambah Social Application
1. Kembali ke halaman admin utama
2. Cari **"Social applications"** → klik "Add"
3. Isi form:
   - **Provider**: Google
   - **Name**: Google OAuth
   - **Client id**: [paste Client ID dari Google Console]
   - **Secret key**: [paste Client Secret dari Google Console]
   - **Sites**: Pilih "localhost:8000" dari kotak "Available sites", klik panah → untuk pindah ke "Chosen sites"
4. Klik "SAVE"

## 🎉 Testing

1. Logout dari admin: http://localhost:8000/logout/
2. Buka halaman login: http://localhost:8000/login/
3. Klik tombol **Google** (yang sekarang sudah ada logo Google berwarna)
4. Pilih akun Google Anda
5. Izinkan akses
6. Seharusnya redirect ke dashboard!

## ⚠️ Troubleshooting

### Error: "redirect_uri_mismatch"
- Pastikan URL di Google Console persis: `http://localhost:8000/accounts/google/login/callback/`
- Perhatikan trailing slash `/` di akhir

### Error: "Site matching query does not exist"
- Sudah dikonfigurasi di Step 7

### Tombol Google tidak klik-able
- Hard refresh browser: Ctrl+Shift+R

### Login berhasil tapi tidak redirect
- Cek apakah URL `dashboard` sudah terdaftar di `users/urls.py`

## 📝 Catatan Penting

- **JANGAN** commit Client ID dan Secret ke Git
- Untuk production, ganti URL callback dengan domain production Anda
- Email dari Google akan otomatis tersimpan di user profile
