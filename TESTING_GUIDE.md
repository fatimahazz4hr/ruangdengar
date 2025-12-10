# 🧪 Panduan Testing Multiple Role

## ⚠️ MASALAH: Session Tercampur

Django menggunakan **session per browser**, bukan per tab. Jadi kalau login USER dan ADMIN di browser yang sama (walaupun beda tab), session akan **saling timpa/tercampur**.

---

## ✅ SOLUSI 1: Gunakan Browser Berbeda (RECOMMENDED)

**Untuk testing USER dan ADMIN bersamaan:**

1. **Browser 1 (Chrome)** → Login sebagai **USER**
   - URL: http://127.0.0.1:8000/
   - Email: `iqna@gmail.com` atau `auliya@gmail.com`
   - Test: Dashboard User, Buat Laporan, Booking Konseling, dll

2. **Browser 2 (Firefox/Edge)** → Login sebagai **ADMIN**
   - URL: http://127.0.0.1:8000/
   - Email: `fatimahazz4hr@gmail.com`
   - Test: Dashboard Admin, Kelola Jadwal, Kelola Laporan, dll

**Keuntungan:**
- ✅ Session tidak tercampur
- ✅ Bisa test USER dan ADMIN bersamaan
- ✅ Tidak perlu logout berkali-kali

---

## ✅ SOLUSI 2: Incognito/Private Mode

**Untuk testing tanpa install browser lain:**

1. **Window Normal** → Login sebagai **USER**
   - Chrome biasa
   
2. **Window Incognito/Private** → Login sebagai **ADMIN**
   - Chrome → Klik menu (⋮) → New Incognito Window
   - Edge → Ctrl + Shift + N
   - Firefox → Ctrl + Shift + P

**Keuntungan:**
- ✅ Session terpisah
- ✅ Tidak perlu browser lain
- ✅ Bisa test bersamaan

---

## ✅ SOLUSI 3: Logout Sebelum Switch Role

**Kalau hanya punya 1 browser:**

1. **Login sebagai USER**
   - Test semua fitur user
   
2. **LOGOUT** (penting!)
   - Klik tombol "Keluar"
   
3. **Login sebagai ADMIN**
   - Test semua fitur admin
   
4. **LOGOUT lagi** sebelum balik ke USER

**Keuntungan:**
- ✅ Session bersih
- ✅ Tidak tercampur

**Kekurangan:**
- ❌ Harus logout berkali-kali
- ❌ Tidak bisa test bersamaan

---

## 🚫 JANGAN LAKUKAN INI

❌ **Login USER dan ADMIN di tab berbeda, browser yang sama**
- Session akan tercampur
- Role bisa berubah-ubah
- Data bisa kacau

❌ **Switch role tanpa logout**
- Session lama masih aktif
- Django bingung mau pakai session yang mana

---

## 📋 Daftar Akun untuk Testing

### USER Accounts
- Email: `iqna@gmail.com` | Nama: Anggi | NIM: 2211102288
- Email: `auliya@gmail.com` | Nama: Auliya | NIM: 2211102293
- Email: `fatimahazz@student.telkomuniversity.ac.id` | Nama: Fatimah | NIM: 2211102160

### ADMIN Account
- Email: `fatimahazz4hr@gmail.com` | Nama: Fatimah Az Zahra | NIDN: 2211102160

---

## 🎯 Workflow Testing yang Benar

### Scenario 1: Test USER dan ADMIN Bersamaan

```
Chrome (Normal):
├─ Login: iqna@gmail.com (USER)
├─ Test: Dashboard User
├─ Test: Buat Laporan
├─ Test: Booking Konseling
└─ Test: Riwayat Laporan

Firefox (atau Chrome Incognito):
├─ Login: fatimahazz4hr@gmail.com (ADMIN)
├─ Test: Dashboard Admin
├─ Test: Kelola Jadwal
├─ Test: Kelola Laporan
└─ Test: Kelola Pengguna
```

### Scenario 2: Test Satu Role Saja

```
Browser apapun:
1. Login sebagai USER
2. Test semua fitur user
3. LOGOUT
4. Login sebagai ADMIN
5. Test semua fitur admin
6. LOGOUT
```

---

## 🔍 Debug: Cek Role Saat Ini

Buka browser console (F12) dan ketik:

```javascript
// Lihat cookies
document.cookie

// Reload dengan clear cache
location.reload(true)
```

Atau cek di Django admin:
- Login ke: http://127.0.0.1:8000/admin
- Menu: SESSIONS → Sessions
- Lihat session data

---

## 💡 Tips

1. **Gunakan Browser Berbeda** = Paling mudah dan aman
2. **Incognito Mode** = Alternatif kalau tidak punya browser lain
3. **Selalu Logout** = Kalau test di browser yang sama
4. **Clear Cache** = Kalau masih bermasalah (Ctrl + Shift + Del)
5. **Close All Tabs** = Sebelum login ulang

---

## 🆘 Troubleshooting

### "Role berubah-ubah sendiri"
→ Session tercampur. Logout, close browser, buka lagi.

### "Redirect ke admin padahal login user"
→ Masih ada session admin. Logout dan clear cookies.

### "CSRF error"
→ Session lama tidak valid. Logout, clear cache, login ulang.

### "Data tidak muncul"
→ Login dengan role yang salah. Cek email saat login (USER atau ADMIN).

---

**Last Updated:** December 5, 2025
