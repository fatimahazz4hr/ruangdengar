# Email Integration Testing Guide

## ✅ Integration Complete!

Email notifications telah berhasil diintegrasikan ke 4 views utama:

### 1. **Laporan Creation** (`buat_laporan_view`)
- ✅ Email ke admin saat laporan baru dibuat
- ✅ Email alert urgent ke management jika `ai_urgency='darurat'`

### 2. **Status Update** (`edit_laporan_view`)
- ✅ Email ke pelapor saat status laporan berubah
- ✅ Include catatan admin dalam email

### 3. **Booking Creation** (`booking_konseling_view`)
- ✅ Email konfirmasi ke pelapor
- ✅ Email notifikasi ke counselor

### 4. **Rekam Medis Creation** (`rekam_medis_add_view`)
- ✅ Email high risk alert ke management jika `risiko_bunuh_diri='tinggi'` atau `risiko_self_harm='tinggi'`

---

## 🧪 Testing Steps (Development Mode)

Email backend sudah dikonfigurasi ke `console.EmailBackend`, jadi semua email akan **print ke terminal** untuk testing.

### Test 1: Laporan Creation Email

1. **Start server:**
   ```bash
   python manage.py runserver
   ```

2. **Login sebagai USER**

3. **Buat laporan baru:**
   - Akses: http://localhost:8000/buat-laporan/
   - Isi form lengkap (jenis, deskripsi, lokasi, dll)
   - Upload bukti atau isi link
   - Submit

4. **Check terminal output:**
   ```
   ----------------------------------------------------------------------
   Content-Type: text/plain; charset="utf-8"
   MIME-Version: 1.0
   Content-Transfer-Encoding: 7bit
   Subject: [Ruang Dengar] Laporan Baru Masuk - RPT-20251215-0001
   From: noreply@ruangdengar.telkomuniversity.ac.id
   To: admin@example.com
   Date: Sun, 15 Dec 2025 10:30:00 +0700
   Message-ID: <...>
   
   Laporan baru telah masuk ke sistem Ruang Dengar...
   (isi email HTML akan tampil di console)
   ----------------------------------------------------------------------
   ```

5. **Verify:**
   - ✅ Email muncul di console
   - ✅ Kode laporan correct (RPT-YYYYMMDD-NNNN)
   - ✅ Link detail laporan correct
   - ✅ Urgency badge correct (DARURAT/TINGGI/SEDANG/RENDAH)

---

### Test 2: Status Update Email

1. **Login sebagai ADMIN**

2. **Update status laporan:**
   - Akses: http://localhost:8000/dashboard/kelola-laporan/
   - Klik "Edit" pada laporan
   - Ubah status (misal: diterima → sedang_diproses)
   - Tambahkan catatan
   - Submit

3. **Check terminal output:**
   ```
   Subject: [Ruang Dengar] Status Laporan Anda Telah Diperbarui
   To: user@example.com
   ```

4. **Verify:**
   - ✅ Email dikirim ke pelapor
   - ✅ Old status dan new status correct
   - ✅ Catatan admin included
   - ✅ Link ke laporan correct

---

### Test 3: Booking Email

1. **Login sebagai USER**

2. **Buat booking konseling:**
   - Akses: http://localhost:8000/booking-konseling/
   - Pilih konselor, tanggal, waktu
   - Isi jenis sesi (online/offline)
   - Submit

3. **Check terminal output (2 emails):**
   ```
   Email 1:
   Subject: [Ruang Dengar] Konfirmasi Booking Konseling
   To: user@example.com (pelapor)
   
   Email 2:
   Subject: [Ruang Dengar] Booking Konseling Baru
   To: counselor@example.com (konselor)
   ```

4. **Verify:**
   - ✅ 2 emails sent (pelapor + counselor)
   - ✅ Session details correct (tanggal, waktu, tipe)
   - ✅ Preparation checklist included
   - ✅ Links correct

---

### Test 4: High Risk Alert Email

1. **Login sebagai ADMIN**

2. **Create rekam medis dengan risk tinggi:**
   - Akses booking detail
   - Klik "Add Clinical Notes"
   - Set `risiko_bunuh_diri` = **tinggi** atau `risiko_self_harm` = **tinggi**
   - Isi form lengkap
   - Submit

3. **Check terminal output:**
   ```
   Subject: 🚨 [URGENT] High Risk Client Alert - [Client Name]
   To: superadmin@example.com, management@example.com
   ```

4. **Verify:**
   - ✅ Email sent to management (superusers)
   - ✅ Risk assessment details correct
   - ✅ Recommended actions list included
   - ✅ Urgent styling (red alert)

---

## 📧 Email Templates Created

All HTML email templates tersimpan di `templates/emails/`:

| Template | Purpose |
|----------|---------|
| `laporan_created_admin.html` | Admin notification for new laporan |
| `laporan_status_updated.html` | Pelapor notification for status change |
| `booking_created_pelapor.html` | Pelapor booking confirmation |
| `booking_created_counselor.html` | Counselor booking notification |
| `high_risk_alert.html` | Management high risk alert |

---

## 🎨 Email Design Features

- ✅ **Responsive design** (mobile-friendly)
- ✅ **Gradient headers** (#667eea → #764ba2)
- ✅ **Color-coded urgency badges**:
  - 🔴 DARURAT (red)
  - 🟠 TINGGI (orange)
  - 🟡 SEDANG (yellow)
  - 🟢 RENDAH (green)
- ✅ **CTA buttons** (view laporan, booking, rekam medis)
- ✅ **Plain text fallback** (untuk email clients yang tidak support HTML)

---

## 🔧 Configuration

### Current Settings (Development)

```python
# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'noreply@ruangdengar.telkomuniversity.ac.id'
SITE_URL = 'http://localhost:8000'
TIME_ZONE = 'Asia/Jakarta'
```

### Production Settings

For production deployment, update `settings_production.py`:

```python
# Email configuration (sudah ada)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST', default='smtp.gmail.com')
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')  # your-email@gmail.com
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')  # Gmail App Password
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='noreply@ruangdengar.telkomuniversity.ac.id')
SITE_URL = config('SITE_URL', default='https://ruangdengar.telkomuniversity.ac.id')
```

### Environment Variables (.env)

```bash
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-16-char-app-password
SITE_URL=https://ruangdengar.telkomuniversity.ac.id
```

---

## 📝 Function Reference

All email utility functions dalam `users/email_utils.py`:

### 1. `send_laporan_created_notification(laporan, admin_emails)`
Send email ke admin saat laporan baru dibuat.

### 2. `send_laporan_status_updated_notification(laporan, old_status, new_status, catatan="")`
Send email ke pelapor saat status berubah.

### 3. `send_urgent_laporan_alert(laporan, management_emails)`
Send URGENT alert ke management untuk laporan DARURAT.

### 4. `send_booking_created_notification(booking)`
Send dual email: confirmation ke pelapor + notification ke counselor.

### 5. `send_high_risk_alert(rekam_medis, management_emails)`
Send HIGH RISK alert ke management untuk client dengan risk tinggi.

### 6. `get_admin_emails()`
Get all admin email addresses (untuk laporan notifications).

### 7. `get_management_emails()`
Get superuser/management email addresses (untuk urgent alerts).

---

## 🐛 Troubleshooting

### Email tidak muncul di console?

**Check:**
1. ✅ Server running? `python manage.py runserver`
2. ✅ EMAIL_BACKEND correct? `console.EmailBackend` (dev mode)
3. ✅ Admin email exists? Check `CustomUser.objects.filter(role='ADMIN')`
4. ✅ Import error? Check terminal for import errors

### Email template error?

**Check:**
1. ✅ Template files exist di `templates/emails/`?
2. ✅ Template variables correct ({{ laporan.kode }}, {{ booking.tanggal }}, dll)?
3. ✅ Model fields correct (check Laporan, Booking, RekamMedisKonseling models)?

### Production: Email tidak terkirim?

**Check:**
1. ✅ Gmail App Password generated? (bukan password biasa)
2. ✅ Environment variables set? (`EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`)
3. ✅ SMTP settings correct? (port 587, TLS enabled)
4. ✅ Firewall allow outbound port 587?
5. ✅ Check Django logs: `/var/log/ruangdengar/django.log`

---

## ✨ Next Steps (Optional Enhancements)

### 1. Async Email Delivery (Celery)
Untuk non-blocking email sending:

```bash
pip install celery redis
```

Create `users/tasks.py`:
```python
from celery import shared_task
from .email_utils import send_laporan_created_notification

@shared_task
def send_laporan_email_async(laporan_id, admin_emails):
    from .models import Laporan
    laporan = Laporan.objects.get(pk=laporan_id)
    send_laporan_created_notification(laporan, admin_emails)
```

### 2. Email Templates Customization
Edit HTML templates di `templates/emails/` untuk customize:
- Logo/branding
- Color scheme
- Text content
- Footer links

### 3. Email Analytics
Add tracking:
- Open rate (pixel tracking)
- Click rate (link tracking)
- Bounce rate (webhook from email provider)

---

## 📚 References

- Email Integration Guide: `EMAIL_INTEGRATION_GUIDE.md`
- Django Email Documentation: https://docs.djangoproject.com/en/5.2/topics/email/
- Gmail SMTP Setup: https://support.google.com/mail/answer/7126229

---

**Testing Complete!** ✅  
All email notifications working dalam development mode (console backend).  
Ready untuk production deployment setelah configure Gmail SMTP credentials.
