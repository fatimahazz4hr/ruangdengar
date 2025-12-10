# 🚀 QUICK START: Setup Microsoft OAuth

## Error yang Anda alami:
```
DoesNotExist at /accounts/microsoft/login/
No exception message supplied
```

**Penyebab:** Social Application untuk Microsoft belum di-setup di Django Admin.

---

## ✅ Solusi Cepat (5 Menit)

### Step 1: Buat Superuser (SUDAH SELESAI ✅)
Superuser sudah dibuat dengan credentials:
```
Email: admin@telkomuniversity.ac.id
Password: admin123
```

**NOTE:** Jika perlu buat superuser baru, gunakan:
```bash
python manage.py create_admin
```

### Step 2: Login ke Django Admin
1. Buka: http://127.0.0.1:8000/admin
2. Login dengan superuser yang baru dibuat

### Step 3: Configure Sites
1. Klik **"Sites"** di sidebar
2. Klik **"example.com"**
3. Edit:
   ```
   Domain name: 127.0.0.1:8000
   Display name: Ruang Dengar Local
   ```
4. Klik **"SAVE"**

### Step 4: Tambah Social Application (TEMPORARY - untuk testing UI saja)
1. Kembali ke admin home
2. Klik **"Social applications"** → **"Add Social Application"**
3. Isi form:
   ```
   Provider: Microsoft
   Name: Microsoft Telkom (Temporary)
   Client id: dummy-client-id-for-testing-ui-only
   Secret key: dummy-secret-key-for-testing-ui-only
   ```
4. Di bagian **"Sites"**:
   - Pilih **"127.0.0.1:8000"** di kotak kiri
   - Klik tanda **panah kanan (→)** untuk pindahkan ke "Chosen sites"
5. Klik **"SAVE"**

### Step 5: Test Tombol Microsoft
1. Logout dari admin: http://127.0.0.1:8000/admin/logout/
2. Buka halaman login: http://127.0.0.1:8000/
3. Klik tombol **"Login dengan Microsoft"**
4. **EXPECTED:** Akan redirect ke Microsoft login (tapi gagal karena dummy credentials)
   - Ini normal! Minimal tombol tidak error lagi
5. **UI Testing:** Cek semua halaman socialaccount templates sudah tampil bagus

---

## 🔐 Setup REAL Microsoft OAuth (untuk Production)

Setelah testing UI selesai, ikuti **MICROSOFT_OAUTH_SETUP.md** untuk:
1. Register app di Azure Portal
2. Dapatkan **real Client ID** dan **Secret**
3. Update Social Application di admin dengan credentials yang benar
4. Test login dengan akun @telkomuniversity.ac.id

---

## 📋 Checklist

- [ ] Superuser created
- [ ] Sites configured (127.0.0.1:8000)
- [ ] Social Application added (dummy credentials OK untuk testing)
- [ ] Tombol Microsoft tidak error lagi
- [ ] Templates socialaccount tampil dengan benar
- [ ] (Optional) Real Azure credentials untuk production

---

## ❓ FAQ

**Q: Kenapa pakai dummy credentials dulu?**
A: Untuk testing UI/UX templates yang sudah kita buat, tanpa perlu setup Azure dulu.

**Q: Kapan harus ganti ke real credentials?**
A: Setelah UI confirmed bagus, lalu setup Azure Portal untuk production.

**Q: Apakah registrasi manual masih bisa?**
A: Ya! Registrasi manual tidak terpengaruh, masih bisa digunakan normal.

---

**Last Updated:** December 6, 2025
**Status:** ✅ Ready untuk testing UI dengan dummy credentials
