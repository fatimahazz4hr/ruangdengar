# 📧 Email Integration - Quick Reference

## ✅ Integration Complete!

Email notifications telah **berhasil diintegrasikan** ke Ruang Dengar Platform.

---

## 📊 What's Working Now

| Workflow | Email Type | Recipients | Trigger |
|----------|-----------|-----------|---------|
| **Buat Laporan** | Admin Notification | All Admins | User submit laporan |
| **Laporan DARURAT** | Urgent Alert 🚨 | Management | AI urgency = DARURAT |
| **Update Status** | Status Update | Pelapor | Admin ubah status |
| **Buat Booking** | Dual Confirmation | Counselor + Pelapor | User buat booking |
| **Rekam Medis (High Risk)** | High Risk Alert 🚨 | Management | risk_bunuh_diri/self_harm = TINGGI |

---

## 🧪 Test Now (Development Mode)

```bash
# Start server
python manage.py runserver

# Emails akan print ke terminal/console (tidak send real email)
```

### Quick Test Scenarios:

1. **Test Laporan Email:**
   - Login sebagai USER
   - Buat laporan baru
   - ✅ Check terminal → email ke admin muncul

2. **Test Status Update Email:**
   - Login sebagai ADMIN
   - Update status laporan
   - ✅ Check terminal → email ke pelapor muncul

3. **Test Booking Email:**
   - Login sebagai USER
   - Buat booking baru
   - ✅ Check terminal → 2 emails muncul (counselor + pelapor)

4. **Test High Risk Alert:**
   - Login sebagai ADMIN
   - Create rekam medis dengan `risiko_bunuh_diri=tinggi`
   - ✅ Check terminal → urgent email ke management muncul

---

## 📁 New Files Created

### Code & Templates (6 files):
- ✅ `users/email_utils.py` - Core email functions
- ✅ `templates/emails/laporan_created_admin.html`
- ✅ `templates/emails/laporan_status_updated.html`
- ✅ `templates/emails/booking_created_pelapor.html`
- ✅ `templates/emails/booking_created_counselor.html`
- ✅ `templates/emails/high_risk_alert.html`

### Documentation (3 files):
- 📚 `EMAIL_INTEGRATION_GUIDE.md` - Developer guide
- 🧪 `EMAIL_TESTING_GUIDE.md` - Testing procedures
- 📋 `EMAIL_IMPLEMENTATION_SUMMARY.md` - Implementation summary

---

## 🔧 Configuration

### Current (Development):
```python
EMAIL_BACKEND = 'console.EmailBackend'  # Print to terminal
DEFAULT_FROM_EMAIL = 'noreply@ruangdengar.telkomuniversity.ac.id'
SITE_URL = 'http://localhost:8000'
```

### For Production:
1. Generate Gmail App Password
2. Set environment variables:
   ```
   EMAIL_HOST_USER=your-email@gmail.com
   EMAIL_HOST_PASSWORD=your-app-password
   SITE_URL=https://ruangdengar.telkomuniversity.ac.id
   ```
3. Email akan send real ke Gmail recipients

---

## 🎨 Email Design

- ✅ Responsive HTML (mobile-friendly)
- ✅ Gradient purple header (#667eea → #764ba2)
- ✅ Color-coded urgency badges (🔴 🟠 🟡 🟢)
- ✅ CTA buttons (View Laporan, View Booking, dll)
- ✅ Professional styling

---

## 📝 Code Changes

### Modified: `users/views.py`

**4 views updated:**
1. `buat_laporan_view` (line ~1356) → send admin email
2. `edit_laporan_view` (line ~981) → send status update email
3. `booking_konseling_view` (line ~1606) → send booking emails
4. `rekam_medis_add_view` (line ~706) → send high risk alert

**Added imports:**
```python
from .email_utils import (
    send_laporan_created_notification,
    send_laporan_status_updated_notification,
    send_urgent_laporan_alert,
    send_booking_created_notification,
    send_high_risk_alert,
    get_admin_emails,
    get_management_emails
)
```

---

## 🚀 Next Actions

### For Testing (Now):
```bash
# 1. Start server
python manage.py runserver

# 2. Test each workflow
# 3. Check terminal output untuk email HTML
```

### For Production (Later):
1. Generate Gmail App Password
2. Update environment variables
3. Test with real email addresses
4. Monitor logs untuk delivery issues

---

## 🐛 Troubleshooting

### Email tidak muncul di console?
- ✅ Check server running?
- ✅ Check EMAIL_BACKEND = 'console.EmailBackend'?
- ✅ Check admin users exists?

### Production email tidak terkirim?
- ✅ Gmail App Password correct?
- ✅ Environment variables set?
- ✅ SMTP port 587 open?
- ✅ Check Django logs

---

## 📚 Full Documentation

| Document | Purpose |
|----------|---------|
| [EMAIL_IMPLEMENTATION_SUMMARY.md](EMAIL_IMPLEMENTATION_SUMMARY.md) | Complete implementation summary |
| [EMAIL_TESTING_GUIDE.md](EMAIL_TESTING_GUIDE.md) | Step-by-step testing guide |
| [EMAIL_INTEGRATION_GUIDE.md](EMAIL_INTEGRATION_GUIDE.md) | Developer integration guide |

---

## ✨ Summary

**Status**: ✅ **READY TO TEST**

**What's Complete:**
- ✅ Email utility functions (8 functions)
- ✅ HTML email templates (5 templates)
- ✅ View integration (4 views)
- ✅ Development configuration
- ✅ Documentation (3 guides)

**Test Command:**
```bash
python manage.py runserver
# Then test workflows → check terminal for email output
```

**Production Deployment:**
- ⏳ Pending Gmail credentials only
- ✅ Configuration ready
- ✅ Templates ready
- ✅ Code ready

---

**🎉 Email integration complete & ready to test!**

Test sekarang dengan `python manage.py runserver` → buat laporan/booking → check terminal output.
