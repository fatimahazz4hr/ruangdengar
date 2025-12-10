# Setup Microsoft OAuth (Azure AD) untuk Ruang Dengar

## 📋 Overview
Panduan ini akan membantu Anda setup **Microsoft OAuth** (Azure Active Directory) untuk login menggunakan akun **@telkomuniversity.ac.id** atau **@student.telkomuniversity.ac.id**.

---

## 🚀 Langkah 1: Registrasi Aplikasi di Azure Portal

### 1.1. Buka Azure Portal
1. Kunjungi: https://portal.azure.com
2. Login dengan akun Microsoft (gunakan akun admin IT Telkom University jika memungkinkan)
3. Di search bar, ketik **"Azure Active Directory"** atau **"App registrations"**

### 1.2. Buat App Registration Baru
1. Klik **"App registrations"** di sidebar kiri
2. Klik **"New registration"** di toolbar atas
3. Isi form pendaftaran:
   ```
   Name: Ruang Dengar - PPKS Telkom University
   Supported account types: 
     - Pilih "Accounts in any organizational directory (Any Azure AD directory - Multitenant)"
     - ATAU "Accounts in this organizational directory only (Telkom University only)" jika ada
   
   Redirect URI:
     - Platform: Web
     - URL Development: http://localhost:8000/accounts/microsoft/login/callback/
     - URL Production: https://yourdomain.com/accounts/microsoft/login/callback/
   ```
4. Klik **"Register"**

### 1.3. Copy Application (client) ID
Setelah registrasi, Anda akan melihat:
- **Application (client) ID** → Copy ini (contoh: `12345678-1234-1234-1234-123456789012`)
- **Directory (tenant) ID** → Copy juga (atau gunakan `common` untuk multitenant)

---

## 🔑 Langkah 2: Generate Client Secret

### 2.1. Buat Client Secret
1. Di halaman app registration Anda, klik **"Certificates & secrets"** di sidebar
2. Klik tab **"Client secrets"**
3. Klik **"New client secret"**
4. Isi:
   ```
   Description: Ruang Dengar Production Secret
   Expires: 24 months (atau sesuai kebijakan)
   ```
5. Klik **"Add"**
6. **PENTING**: Copy **Value** (secret) segera! Ini hanya ditampilkan sekali
   - Contoh: `abc123~XyZ789.AbCdEfGhIjKlMnOpQrStUvWxYz`

---

## 🌐 Langkah 3: Konfigurasi Redirect URIs

### 3.1. Tambah Redirect URIs
1. Klik **"Authentication"** di sidebar
2. Di bagian **"Platform configurations" → "Web"**, pastikan ada:
   ```
   Development:
   http://localhost:8000/accounts/microsoft/login/callback/
   http://127.0.0.1:8000/accounts/microsoft/login/callback/
   
   Production:
   https://yourdomain.com/accounts/microsoft/login/callback/
   ```
3. Scroll ke bawah, di **"Implicit grant and hybrid flows"**, TIDAK perlu centang apapun
4. Klik **"Save"**

### 3.2. API Permissions (Optional tapi Recommended)
1. Klik **"API permissions"** di sidebar
2. Pastikan ada permissions berikut (seharusnya sudah auto-added):
   ```
   Microsoft Graph:
   - User.Read (Delegated)
   - email (Delegated)
   - openid (Delegated)
   - profile (Delegated)
   ```
3. Jika belum ada, klik **"Add a permission"** → **Microsoft Graph** → **Delegated permissions**
4. Centang: `User.Read`, `email`, `openid`, `profile`
5. Klik **"Add permissions"**
6. Klik **"Grant admin consent for [Tenant]"** (jika Anda admin)

---

## ⚙️ Langkah 4: Konfigurasi Django

### 4.1. Update settings.py (Sudah Done!)
File `ruangdengar/settings.py` sudah dikonfigurasi:
```python
SOCIALACCOUNT_PROVIDERS = {
    'microsoft': {
        'APPS': [
            {
                'client_id': '',  # Isi dari Azure Portal
                'secret': '',  # Isi dari Azure Portal
                'tenant': 'common',  # atau tenant ID Telkom University
            }
        ],
        # ...
    }
}
```

### 4.2. Tambahkan Credentials via Django Admin
1. Jalankan server: `python manage.py runserver`
2. Buka: http://127.0.0.1:8000/admin
3. Login sebagai superuser
4. Cari **"Sites"** → Klik **"example.com"**
5. Edit:
   ```
   Domain name: localhost:8000
   Display name: Ruang Dengar
   ```
6. Save

7. Kembali ke admin, cari **"Social applications"**
8. Klik **"Add Social Application"**
9. Isi form:
   ```
   Provider: Microsoft
   Name: Microsoft Telkom University
   Client id: [Paste Application (client) ID dari Azure]
   Secret key: [Paste Client Secret dari Azure]
   Sites: Pilih "localhost:8000" (pindahkan ke "Chosen sites")
   ```
10. Klik **"Save"**

---

## 🧪 Langkah 5: Testing

### 5.1. Test Login Flow
1. Buka: http://127.0.0.1:8000
2. Klik tombol **"Login dengan Microsoft"**
3. Akan redirect ke halaman login Microsoft
4. Login dengan akun **@telkomuniversity.ac.id** atau **@student.telkomuniversity.ac.id**
5. Setelah berhasil, akan redirect ke halaman **"Lengkapi Profil"**
6. Isi form profil (NIM/NIDN, Fakultas, Prodi, dll)
7. Redirect ke dashboard

### 5.2. Troubleshooting

#### Error: "AADSTS50011: The redirect URI specified in the request does not match..."
**Solusi**: 
- Cek Redirect URI di Azure Portal harus **EXACT MATCH** dengan URL callback
- Pastikan ada slash `/` di akhir: `http://localhost:8000/accounts/microsoft/login/callback/`

#### Error: "invalid_client" atau "AADSTS7000215"
**Solusi**:
- Client Secret salah atau expired
- Generate secret baru di Azure Portal
- Update di Django Admin

#### Error: Email domain tidak diizinkan
**Solusi**:
- Pastikan `ALLOWED_EMAIL_DOMAINS` di `settings.py` sudah benar:
  ```python
  ALLOWED_EMAIL_DOMAINS = [
      'telkomuniversity.ac.id',
      'student.telkomuniversity.ac.id',
  ]
  ```

#### User diarahkan ke lengkapi profil terus-menerus
**Solusi**:
- Pastikan field `is_profile_complete` di-set `True` setelah lengkapi profil
- Cek di `users/views.py` → `lengkapi_profil_view`:
  ```python
  user.is_profile_complete = True
  user.save()
  ```

---

## 🔒 Langkah 6: Restrict ke Email Telkom University Only

### 6.1. Tenant-Specific Configuration (Recommended)
Jika Anda punya akses admin Azure AD Telkom University:
1. Di Azure Portal, copy **Directory (tenant) ID** Telkom University
2. Update `settings.py`:
   ```python
   SOCIALACCOUNT_PROVIDERS = {
       'microsoft': {
           'APPS': [{
               'tenant': '<tenant-id-telkom-university>',  # Ganti 'common'
           }],
       }
   }
   ```
3. Dengan ini, HANYA akun dari tenant Telkom University yang bisa login

### 6.2. Email Domain Validation (Already Implemented)
File `users/adapters.py` sudah ada validasi:
```python
class EmailDomainAdapter(DefaultAccountAdapter):
    def clean_email(self, email):
        allowed_domains = ['telkomuniversity.ac.id', 'student.telkomuniversity.ac.id']
        if email.split('@')[1] not in allowed_domains:
            raise ValidationError("Email harus @telkomuniversity.ac.id")
        return email
```

---

## 📝 Langkah 7: Production Deployment

### 7.1. Update Production Settings
1. Copy `settings.py` ke `settings_production.py` (jika belum ada)
2. Update:
   ```python
   ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
   
   # Site ID production (check di Django admin)
   SITE_ID = 2  # atau ID site production Anda
   ```

### 7.2. Update Azure Redirect URI Production
1. Kembali ke Azure Portal → App Registration
2. Tambah Production Redirect URI:
   ```
   https://yourdomain.com/accounts/microsoft/login/callback/
   ```
3. Save

### 7.3. Update Django Admin - Social App Production
1. Login ke Django admin production
2. Edit Social Application "Microsoft Telkom University"
3. Pastikan Sites yang dipilih adalah site production (yourdomain.com)
4. Save

---

## 🎯 Checklist Completion

- [ ] App Registration created di Azure Portal
- [ ] Client ID & Secret copied
- [ ] Redirect URIs configured (dev + prod)
- [ ] API Permissions granted
- [ ] Django Sites configured
- [ ] Social Application added via Django Admin
- [ ] Test login berhasil dengan email @telkomuniversity.ac.id
- [ ] Lengkapi profil berhasil
- [ ] User redirect ke dashboard setelah profil lengkap
- [ ] Production deployment (jika applicable)

---

## 📚 Referensi

- **Azure App Registration**: https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app
- **Django Allauth Microsoft Provider**: https://django-allauth.readthedocs.io/en/latest/providers.html#microsoft
- **Microsoft Graph API**: https://learn.microsoft.com/en-us/graph/overview

---

## 💬 Butuh Bantuan?

Jika ada error atau pertanyaan, hubungi:
- **IT Telkom University** untuk akses Azure AD tenant
- **Developer Ruang Dengar** untuk konfigurasi Django

---

**Updated**: December 6, 2025
**Status**: ✅ Microsoft OAuth configured, ready for Azure credentials
