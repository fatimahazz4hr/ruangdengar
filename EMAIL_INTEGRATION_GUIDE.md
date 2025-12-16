# Email Notification Integration Guide

## 📧 Implementasi Email Notification - Ruang Dengar

File ini berisi contoh integrasi email notification ke dalam views yang ada.

---

## 1. LAPORAN: Notifikasi Saat Laporan Dibuat

### File: `users/views.py`

```python
# Import di bagian atas file
from users.email_utils import (
    send_laporan_created_notification,
    send_urgent_laporan_alert,
    get_admin_emails
)

# Di dalam function create_laporan (setelah laporan.save())
@login_required
def create_laporan(request):
    # ... existing code ...
    
    if form.is_valid():
        laporan = form.save(commit=False)
        laporan.pelapor = request.user
        laporan.kode_laporan = generate_kode_laporan()  # existing function
        laporan.save()
        
        # ✅ TAMBAHKAN INI: Send email notification ke admin
        admin_emails = get_admin_emails()
        if admin_emails:
            send_laporan_created_notification(laporan, admin_emails)
        
        # ✅ TAMBAHKAN INI: Jika urgent, send alert ke management
        if laporan.ai_urgency == 'DARURAT':
            from users.email_utils import send_urgent_laporan_alert, get_management_emails
            management_emails = get_management_emails()
            if management_emails:
                send_urgent_laporan_alert(laporan, management_emails)
        
        messages.success(request, 'Laporan berhasil dibuat!')
        return redirect('upload_bukti', laporan_id=laporan.id)
    
    # ... rest of code ...
```

---

## 2. LAPORAN: Notifikasi Saat Status Diupdate

### File: `users/views.py`

```python
# Import
from users.email_utils import send_laporan_status_updated_notification

# Di dalam function update_laporan_status
@login_required
def update_laporan_status(request, laporan_id):
    # ... existing code ...
    
    if form.is_valid():
        laporan = get_object_or_404(Laporan, id=laporan_id)
        old_status = laporan.status  # ✅ Simpan old status
        
        # Update status
        laporan.status = form.cleaned_data['status']
        laporan.save()
        
        # Create Progress entry (existing)
        Progress.objects.create(
            laporan=laporan,
            status_saat_ini=laporan.status,
            tahapan_sebelumnya=old_status,
            catatan=form.cleaned_data['catatan'],
            oleh=request.user
        )
        
        # ✅ TAMBAHKAN INI: Send email notification ke pelapor
        send_laporan_status_updated_notification(laporan, old_status, laporan.status)
        
        messages.success(request, 'Status laporan berhasil diupdate!')
        return redirect('laporan_detail', laporan_id=laporan.id)
    
    # ... rest of code ...
```

---

## 3. BOOKING: Notifikasi Saat Booking Dibuat

### File: `users/views.py`

```python
# Import
from users.email_utils import send_booking_created_notification

# Di dalam function create_booking
@login_required
def create_booking(request):
    # ... existing code ...
    
    if form.is_valid():
        booking = form.save(commit=False)
        booking.pelapor = request.user
        booking.status = 'TERJADWAL'
        booking.save()
        
        # ✅ TAMBAHKAN INI: Send email ke konselor dan pelapor
        send_booking_created_notification(booking)
        
        messages.success(request, 'Booking konseling berhasil!')
        return redirect('booking_detail', booking_id=booking.id)
    
    # ... rest of code ...
```

---

## 4. REKAM MEDIS: High Risk Alert

### File: `users/views.py`

```python
# Import
from users.email_utils import (
    send_high_risk_alert,
    send_rekam_medis_created_notification,
    get_management_emails
)

# Di dalam function create_rekam_medis
@login_required
def create_rekam_medis(request, booking_id):
    # ... existing code ...
    
    if form.is_valid():
        rekam_medis = form.save(commit=False)
        rekam_medis.booking = booking
        rekam_medis.pelapor = booking.pelapor
        rekam_medis.konselor = request.user
        rekam_medis.save()
        
        # Update booking status
        booking.status = 'SELESAI'
        booking.save()
        
        # ✅ TAMBAHKAN INI: Check for high risk and send alert
        if rekam_medis.risk_bunuh_diri == 'TINGGI' or rekam_medis.risk_self_harm == 'TINGGI':
            management_emails = get_management_emails()
            if management_emails:
                send_high_risk_alert(rekam_medis, management_emails)
        
        # ✅ TAMBAHKAN INI: Optional - notify pelapor
        send_rekam_medis_created_notification(rekam_medis)
        
        messages.success(request, 'Rekam medis berhasil disimpan!')
        return redirect('rekam_medis_detail', rekam_medis_id=rekam_medis.id)
    
    # ... rest of code ...
```

---

## 5. Testing Email (Development Mode)

Email akan muncul di **console/terminal** karena menggunakan `console.EmailBackend`.

### Test Email Function:

Buat file `test_email.py` di root project:

```python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ruangdengar.settings')
django.setup()

from users.email_utils import (
    send_notification_email,
    get_admin_emails
)

# Test simple email
def test_email():
    result = send_notification_email(
        subject="Test Email Notification",
        recipient_list=['admin@test.com'],
        template_name='emails/laporan_created_admin.html',
        context={
            'kode_laporan': 'RD-20250101-001',
            'jenis': 'Kekerasan Seksual',
            'urgency': 'TINGGI',
            'is_anonim': False,
            'pelapor_nama': 'John Doe',
            'created_at': '2025-01-15 10:00:00',
            'laporan_url': 'http://localhost:8000/admin/laporan/1/'
        }
    )
    print(f"Email sent: {result}")

if __name__ == '__main__':
    test_email()
```

Run dengan:
```bash
python test_email.py
```

---

## 6. Production Setup (SMTP Gmail)

### Update `ruangdengar/settings_production.py`:

```python
# Email Configuration (Production)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')  # Set di environment variable
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')  # Gmail App Password
DEFAULT_FROM_EMAIL = 'noreply@ruangdengar.telkomuniversity.ac.id'
SITE_URL = os.environ.get('SITE_URL', 'https://ruangdengar.telkomuniversity.ac.id')
```

### Set Environment Variables:

```bash
# .env file
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-16-char-app-password
SITE_URL=https://ruangdengar.telkomuniversity.ac.id
```

---

## 7. Async Email (Optional - Celery)

Untuk production, sebaiknya pakai Celery untuk async email:

```python
# tasks.py (create new file)
from celery import shared_task
from users.email_utils import send_notification_email

@shared_task
def send_email_async(subject, recipient_list, template_name, context):
    return send_notification_email(subject, recipient_list, template_name, context)
```

Usage:
```python
# Instead of direct call
send_laporan_created_notification(laporan, admin_emails)

# Use async
from users.tasks import send_email_async
send_email_async.delay(subject, recipients, template, context)
```

---

## 8. Additional Templates Needed

Buat template lainnya jika diperlukan:
- `booking_reminder.html` (untuk reminder H-1)
- `laporan_urgent_alert.html` (untuk laporan darurat)
- `rekam_medis_created.html` (konfirmasi ke pelapor)

---

## ✅ Checklist Implementasi:

- [x] Email utility functions created (`email_utils.py`)
- [x] Email templates created (4 templates)
- [x] Settings.py updated (EMAIL config)
- [ ] Integrate to `create_laporan()` view
- [ ] Integrate to `update_laporan_status()` view
- [ ] Integrate to `create_booking()` view
- [ ] Integrate to `create_rekam_medis()` view
- [ ] Test in development (console backend)
- [ ] Setup SMTP for production
- [ ] (Optional) Setup Celery for async emails

---

**Next Steps:**
1. Test email di development (akan muncul di terminal/console)
2. Integrate email calls ke views yang relevan
3. Deploy ke production dengan SMTP credentials
