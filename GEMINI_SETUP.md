# 🆓 Setup Google Gemini API (100% GRATIS!)

Panduan 5 menit untuk dapetin API key Google Gemini GRATIS.

---

## 🎯 Kenapa Gemini?

✅ **100% GRATIS** - Tidak ada biaya sama sekali  
✅ **60 requests/menit** - Cukup untuk kampus  
✅ **Unlimited quota** - Gratis selamanya  
✅ **Lebih bagus dari ChatGPT-3.5** - Model terbaru Google  
✅ **No credit card needed** - Cuma perlu akun Google  

---

## 📝 Langkah Dapetin API Key (5 MENIT!)

### 1. Buka Google AI Studio
👉 **https://aistudio.google.com/app/apikey**

### 2. Login dengan Google Account
- Pakai email Telkom University atau email pribadi
- **Gratis, tidak perlu kartu kredit!**

### 3. Klik "Create API Key"
![Gemini API](https://i.imgur.com/example.png)

- Klik tombol **"Create API key in new project"**
- Atau pilih existing project (kalau udah punya)

### 4. Copy API Key
- API key akan muncul, bentuknya seperti:
  ```
  AIzaSyD-xxxxxxxxxxxxxxxxxxxxxxxxxxx
  ```
- **COPY** dan simpan baik-baik!

### 5. Paste ke `.env`
```env
# File: .env
GEMINI_API_KEY=AIzaSyD-xxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## ✅ Testing API Key

Coba test di Python:

```python
import google.generativeai as genai

# Setup
genai.configure(api_key='AIzaSyD-xxxxxxxxxxxxxxxxxxxxxxxxxxx')
model = genai.GenerativeModel('gemini-pro')

# Test
response = model.generate_content('Halo!')
print(response.text)

# Output: Halo! Ada yang bisa saya bantu?
```

Kalau keluar response → **API key berhasil!** ✅

---

## 🚀 Install Dependencies

```bash
pip install google-generativeai
```

Atau sudah otomatis terinstall kalau pakai:
```bash
pip install -r requirements.txt
```

---

## 🔧 Konfigurasi di Project

File `.env` harus ada:
```env
# Django
SECRET_KEY=your-django-secret-key
DEBUG=True

# Database
DB_NAME=ruangdengar_db
DB_USER=postgres
DB_PASSWORD=yourpassword

# Google Gemini AI (GRATIS!)
GEMINI_API_KEY=AIzaSyD-xxxxxxxxxxxxxxxxxxxxxxxxxxx

# Microsoft OAuth (opsional)
MICROSOFT_CLIENT_ID=your-client-id
MICROSOFT_CLIENT_SECRET=your-client-secret
```

---

## 📊 Quota & Limits (GRATIS SELAMANYA!)

| Feature | Free Tier |
|---------|-----------|
| **Requests per minute** | 60 RPM |
| **Requests per day** | 1,500 RPD |
| **Cost** | **$0 (GRATIS!)** |
| **Credit card** | **TIDAK PERLU** |
| **Expire** | **TIDAK PERNAH** |

**Cukup untuk:**
- Kampus dengan 500 mahasiswa
- ~3 laporan per mahasiswa per hari
- AI moderation untuk semua laporan

---

## ❓ Troubleshooting

### Error: "API key not valid"
- Pastikan copy full API key (termasuk `AIzaSy...`)
- Cek tidak ada spasi sebelum/sesudah
- Generate API key baru di dashboard

### Error: "Quota exceeded"
- Tunggu 1 menit (reset otomatis)
- Max 60 requests per menit
- Kalau habis quota harian, tunggu besok (jarang banget)

### AI tidak jalan tapi web normal
- Cek file `.env` ada `GEMINI_API_KEY=...`
- AI moderation optional, web tetap jalan tanpa AI
- Cek logs: `python manage.py runserver` (lihat warning)

---

## 🆚 Perbandingan AI

| AI | Biaya | Quota | Setup |
|----|-------|-------|-------|
| **Google Gemini** | 🆓 GRATIS | 60/min | ⭐ 5 menit |
| OpenAI GPT | 💰 $0.002/1K tokens | Unlimited (bayar) | 15 menit |
| Claude AI | 💰 $0.008/1K tokens | Unlimited (bayar) | 15 menit |

**Gemini = Paling Gampang + Gratis!** 🎉

---

## 📞 Link Penting

- **Dashboard API**: https://aistudio.google.com/app/apikey
- **Dokumentasi**: https://ai.google.dev/docs
- **Pricing (Gratis!)**: https://ai.google.dev/pricing

---

## 🎯 Kesimpulan

1. Buka: https://aistudio.google.com/app/apikey
2. Login Google → Create API key
3. Copy paste ke `.env`
4. Done! AI moderation langsung jalan 🚀

**GRATIS SELAMANYA, TIDAK BUTUH KARTU KREDIT!** 💚
