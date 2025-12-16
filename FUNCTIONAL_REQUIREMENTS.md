# Perancangan Sistem - Tabel Functional Requirement

**Ruang Dengar Platform**  
**Version**: 1.0  
**Last Updated**: December 15, 2025

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Functional Requirements by Feature](#functional-requirements-by-feature)
3. [Data Flow Requirements](#data-flow-requirements)
4. [Non-Functional Requirements](#non-functional-requirements)
5. [Constraint & Assumptions](#constraint--assumptions)

---

## Overview

Dokumen ini mendefinisikan **Functional Requirements (FR)** untuk Ruang Dengar Platform. Setiap requirement dijelaskan dengan:
- **ID**: Unique identifier (FR-001, FR-002, etc.)
- **Feature Name**: Nama fitur
- **Description**: Deskripsi singkat
- **Actor**: Siapa yang melakukan aksi (User/Admin)
- **Precondition**: Kondisi sebelum fitur dijalankan
- **Main Flow**: Alur utama (step-by-step)
- **Postcondition**: Hasil akhir
- **Exception**: Error handling
- **Constraint**: Batasan/keterbatasan
- **Priority**: HIGH/MEDIUM/LOW

---

## Functional Requirements by Feature

### A. AUTHENTICATION & REGISTRATION

#### FR-001: User Registration dengan Email

| Attribute | Value |
|-----------|-------|
| **ID** | FR-001 |
| **Feature Name** | User Registration dengan Email |
| **Category** | Authentication |
| **Priority** | HIGH |
| **Actor** | Public User |
| **Precondition** | User belum terdaftar; dapat akses landing page |
| **Main Flow** | 1. User klik "Daftar" di landing page<br>2. Pilih role: Student/Staff<br>3. Isi form: email kampus, password, nama lengkap, nim/nidn<br>4. Sistem validasi email & format password<br>5. Send email verifikasi<br>6. User klik link verifikasi di email<br>7. Akun aktif, redirect ke login |
| **Postcondition** | User account dibuat dengan status `is_active=True`, email terverifikasi |
| **Exception** | Email sudah terdaftar → error "Email already exists"<br>Email tidak valid → error "Invalid email format"<br>Password < 8 karakter → error "Password too short" |
| **Constraint** | Email harus unik, password min 8 karakter, email verifikasi berlaku 24 jam |
| **Related Models** | CustomUser |
| **Related Views** | register_user(), send_verification_email() |

---

#### FR-002: Login dengan SSO (Microsoft OAuth)

| Attribute | Value |
|-----------|-------|
| **ID** | FR-002 |
| **Feature Name** | Login dengan SSO (Microsoft Entra ID) |
| **Category** | Authentication |
| **Priority** | HIGH |
| **Actor** | User/Admin |
| **Precondition** | User terdaftar; akses login page; terhubung ke Internet |
| **Main Flow** | 1. User klik "Login dengan Microsoft"<br>2. Redirect ke Microsoft Entra ID login page<br>3. User input credential Microsoft kampus<br>4. Microsoft return email & token<br>5. Sistem cari user dengan email tersebut<br>6. Jika ada → login; jika tidak → create auto account & login<br>7. Redirect ke dashboard sesuai role |
| **Postcondition** | User authenticated; session dibuat; redirect ke dashboard |
| **Exception** | User email tidak di whitelist → error "Email not authorized"<br>Microsoft API error → error "SSO service unavailable"<br>Token invalid/expired → error "Authentication failed" |
| **Constraint** | Harus terhubung ke Microsoft Entra ID; token valid 1 jam; auto-create user harus enable di setting |
| **Related Models** | CustomUser, SocialAccount (via django-allauth) |
| **Related Views** | oauth_callback(), microsoft_oauth() |

---

#### FR-003: Password Reset

| Attribute | Value |
|-----------|-------|
| **ID** | FR-003 |
| **Feature Name** | Reset Password via Email |
| **Category** | Authentication |
| **Priority** | MEDIUM |
| **Actor** | User/Admin |
| **Precondition** | User lupa password; akses login page |
| **Main Flow** | 1. User klik "Lupa Password"<br>2. Input email terdaftar<br>3. Sistem generate reset token & send email<br>4. User klik link di email<br>5. Input password baru 2x (konfirmasi)<br>6. Sistem validate & update password<br>7. Redirect ke login page |
| **Postcondition** | Password berhasil direset; user bisa login dengan password baru |
| **Exception** | Email tidak terdaftar → error "Email not found"<br>Token expired (> 24 jam) → error "Link expired"<br>Password tidak sesuai → error "Passwords do not match" |
| **Constraint** | Reset token berlaku 24 jam; password min 8 karakter |
| **Related Models** | CustomUser |
| **Related Views** | forgot_password(), reset_password() |

---

### B. LAPORAN (REPORT MANAGEMENT)

#### FR-004: Create Laporan (Report)

| Attribute | Value |
|-----------|-------|
| **ID** | FR-004 |
| **Feature Name** | Buat Laporan Kekerasan |
| **Category** | Laporan |
| **Priority** | HIGH |
| **Actor** | User (Pelapor) |
| **Precondition** | User sudah login; akses menu "Buat Laporan" |
| **Main Flow** | 1. User klik "Buat Laporan"<br>2. Isi form:<br>   - Jenis kekerasan (dropdown)<br>   - Apakah anonim? (checkbox)<br>   - Apakah korban langsung? (radio)<br>   - Data korban (jika bukan diri sendiri)<br>   - Data terlapor<br>   - Kronologi singkat & lengkap<br>   - Lokasi kejadian<br>3. AI moderation (Gemini) analyze teks<br>4. Generate kategori, urgency, toxicity score<br>5. Create laporan dengan status `diterima`<br>6. Generate kode laporan unik (RD-20250101-001)<br>7. Redirect ke "Upload Bukti" |
| **Postcondition** | Laporan dibuat; AI moderation completed; status=`diterima`; kode laporan generated |
| **Exception** | Form tidak lengkap → error "Required field missing"<br>AI API timeout → fallback ke keyword-based; warn user<br>Database error → error "Failed to save report" |
| **Constraint** | Max 5000 karakter untuk deskripsi; AI moderation max 2 min timeout; 1 laporan per user per hari (rate limit) |
| **Data Fields** | jenis, is_anonim, apakah_korban_langsung, nama_korban, nim_nip_korban, status_korban, fakultas_korban, prodi_korban, jenis_kelamin_korban, jumlah_terlapor, nama_terlapor, nim_nip_terlapor, asal_instansi_terlapor, cronologi_singkat, deskripsi, lokasi, link_pelaporan |
| **AI Output Fields** | ai_kategori, ai_urgency, ai_toxicity_score, ai_analyzed |
| **Related Models** | Laporan, Progress |
| **Related Views** | create_laporan() |

---

#### FR-005: View Laporan Status

| Attribute | Value |
|-----------|-------|
| **ID** | FR-005 |
| **Feature Name** | Lihat Status Laporan |
| **Category** | Laporan |
| **Priority** | HIGH |
| **Actor** | User (Pelapor) |
| **Precondition** | User sudah membuat laporan; login |
| **Main Flow** | 1. User akses "Riwayat Laporan" atau "Status Laporan"<br>2. Sistem tampilkan daftar laporan milik user<br>3. User klik laporan untuk lihat detail<br>4. Tampilkan:<br>   - Kode laporan, tanggal, kategori<br>   - Status saat ini & timeline 5-tahapan PPKPT<br>   - Progress updates (catatan dari admin)<br>   - Bukti yang sudah diupload<br>   - Estimasi waktu selesai<br>5. User bisa lihat pesan dari admin |
| **Postcondition** | Status laporan ditampilkan; user informed tentang progress |
| **Exception** | Laporan tidak ditemukan → error "Report not found"<br>User tidak punya akses → error "Access denied" |
| **Constraint** | User hanya bisa lihat laporan milik sendiri; status update real-time |
| **Related Models** | Laporan, Progress |
| **Related Views** | laporan_detail(), laporan_list() |

---

#### FR-006: Edit Laporan

| Attribute | Value |
|-----------|-------|
| **ID** | FR-006 |
| **Feature Name** | Edit Laporan (Draft Only) |
| **Category** | Laporan |
| **Priority** | MEDIUM |
| **Actor** | User (Pelapor) |
| **Precondition** | Laporan masih status `diterima` (belum diverifikasi); user owner laporan |
| **Main Flow** | 1. User klik "Edit" pada laporan<br>2. Form pre-filled dengan data existing<br>3. User ubah field yang ingin diubah<br>4. Submit perubahan<br>5. Sistem re-run AI moderation<br>6. Update laporan dengan kategori baru (jika ada)<br>7. Notifikasi admin tentang perubahan |
| **Postcondition** | Laporan diupdate; AI re-analyzed; admin notified |
| **Exception** | Laporan sudah diverifikasi → error "Cannot edit verified report"<br>Form validation error → error "Invalid input" |
| **Constraint** | Hanya bisa edit status `diterima`; maksimal 3x edit |
| **Related Models** | Laporan |
| **Related Views** | edit_laporan() |

---

#### FR-007: Delete Laporan

| Attribute | Value |
|-----------|-------|
| **ID** | FR-007 |
| **Feature Name** | Hapus Laporan (Draft Only) |
| **Category** | Laporan |
| **Priority** | MEDIUM |
| **Actor** | User (Pelapor) |
| **Precondition** | Laporan masih status `diterima`; user owner laporan |
| **Main Flow** | 1. User klik "Hapus" pada laporan<br>2. Sistem tampilkan konfirmasi dialog<br>3. User confirm<br>4. Hapus laporan & semua evidence terkait<br>5. Log deletion action (audit trail) |
| **Postcondition** | Laporan dihapus; hard delete atau soft delete; audit log recorded |
| **Exception** | Laporan sudah diverifikasi → error "Cannot delete verified report"<br>Database error → rollback & error "Failed to delete" |
| **Constraint** | Hanya bisa delete status `diterima`; deletion permanent (or soft-delete dengan audit trail) |
| **Related Models** | Laporan, Evidence |
| **Related Views** | delete_laporan() |

---

### C. BUKTI (EVIDENCE)

#### FR-008: Upload Evidence

| Attribute | Value |
|-----------|-------|
| **ID** | FR-008 |
| **Feature Name** | Upload Evidence (Foto, Dokumen, dll) |
| **Category** | Bukti |
| **Priority** | HIGH |
| **Actor** | User (Pelapor) / Admin |
| **Precondition** | Laporan sudah dibuat; user di halaman "Upload Bukti" |
| **Main Flow** | 1. User klik "Pilih File"<br>2. Select file dari device (PDF, JPG, PNG, docx, xlsx)<br>3. System validate: file type, size (max 10MB per file)<br>4. Input "Keterangan Bukti"<br>5. Click "Upload"<br>6. System simpan file di storage (encrypted)<br>7. Create Evidence record di database<br>8. Notifikasi admin tentang bukti baru |
| **Postcondition** | File tersimpan di server; Evidence object dibuat; metadata recorded (uploaded_by, uploaded_at) |
| **Exception** | File size > 10MB → error "File too large"<br>Invalid file type → error "File type not allowed"<br>Storage full → error "Storage exceeded"<br>Upload timeout → error "Upload failed, please try again" |
| **Constraint** | Max 10MB per file; max 20 files per laporan; allowed types: PDF, JPG, PNG, docx, xlsx; file encrypted at rest |
| **Related Models** | Evidence, Laporan |
| **Related Views** | upload_evidence() |

---

#### FR-009: View & Download Evidence

| Attribute | Value |
|-----------|-------|
| **ID** | FR-009 |
| **Feature Name** | Lihat & Download Evidence |
| **Category** | Bukti |
| **Priority** | HIGH |
| **Actor** | User (Pelapor) / Admin |
| **Precondition** | Evidence sudah diupload; user akses laporan detail |
| **Main Flow** | 1. User buka laporan detail<br>2. Sistem tampilkan daftar evidence files<br>3. Show: filename, upload date, size, keterangan<br>4. User klik file untuk preview/download<br>5. Browser download file (atau preview inline untuk gambar)<br>6. Log download action (untuk audit) |
| **Postcondition** | File downloaded/viewed; access log recorded |
| **Exception** | File corrupted → error "File cannot be read"<br>File deleted → error "File not found"<br>User no permission → error "Access denied" |
| **Constraint** | Download only untuk authorized users (user owner atau admin) |
| **Related Models** | Evidence |
| **Related Views** | view_evidence(), download_evidence() |

---

#### FR-010: Delete Evidence

| Attribute | Value |
|-----------|-------|
| **ID** | FR-010 |
| **Feature Name** | Hapus Evidence |
| **Category** | Bukti |
| **Priority** | MEDIUM |
| **Actor** | User (Pelapor) / Admin |
| **Precondition** | Evidence ada; user owner atau admin; laporan masih `diterima` |
| **Main Flow** | 1. User klik tombol "Hapus" pada evidence<br>2. Konfirmasi dialog<br>3. User confirm<br>4. Delete file dari storage & database record<br>5. Log deletion (audit trail) |
| **Postcondition** | Evidence deleted; file removed; audit log recorded |
| **Exception** | File already deleted → error "File not found"<br>Permission denied → error "You cannot delete this" |
| **Constraint** | User hanya bisa delete sendiri; Admin bisa delete semua; laporan harus `diterima` |
| **Related Models** | Evidence |
| **Related Views** | delete_evidence() |

---

### D. AI MODERATION

#### FR-011: AI Content Moderation

| Attribute | Value |
|-----------|-------|
| **ID** | FR-011 |
| **Feature Name** | AI Content Moderation (Gemini API) |
| **Category** | AI/ML |
| **Priority** | HIGH |
| **Actor** | System (Automated) |
| **Precondition** | Laporan dibuat; text deskripsi ada; Gemini API key configured |
| **Main Flow** | 1. Laporan created, trigger AI moderation job<br>2. Extract text: jenis + deskripsi + kronologi<br>3. Call Gemini API dengan prompt:<br>   ```<br>   Analyze violence report:<br>   Type: [jenis]<br>   Description: [deskripsi]<br>   <br>   Return JSON:<br>   {<br>     "urgency": "darurat|tinggi|sedang|rendah",<br>     "toxicity_score": 0.0-1.0,<br>     "needs_blur": true|false,<br>     "reasoning": "..."<br>   }<br>   ```<br>4. Parse JSON response<br>5. Update Laporan fields: ai_kategori, ai_urgency, ai_toxicity_score, ai_analyzed<br>6. If urgency=`darurat` → trigger escalation alert<br>7. Log AI result untuk audit |
| **Postcondition** | Laporan with AI moderation results; ai_analyzed=True; urgent cases escalated |
| **Exception** | API timeout (> 2 min) → fallback ke keyword-based<br>Invalid JSON response → use default (urgency=sedang)<br>API error (rate limit) → queue untuk retry later<br>API key invalid → disable AI, log error |
| **Constraint** | Max 2 min timeout; fallback to keyword-based classification; cache hasil selama 1 jam; rate limit 100 req/day |
| **Fallback** | Keyword-based classification: count violence keywords untuk determine kategori & urgency |
| **Related Models** | Laporan |
| **Related Views** | moderate_laporan() |
| **External Service** | Google Gemini API |

---

#### FR-012: Manual Category Override

| Attribute | Value |
|-----------|-------|
| **ID** | FR-012 |
| **Feature Name** | Admin Manual Override Kategori |
| **Category** | AI/ML |
| **Priority** | MEDIUM |
| **Actor** | Admin |
| **Precondition** | Laporan sudah di-analyze AI; admin buka laporan |
| **Main Flow** | 1. Admin buka laporan detail<br>2. Lihat AI kategori & rekomendasi<br>3. Jika tidak setuju, klik "Change Category"<br>4. Select kategori yang benar dari dropdown<br>5. Tambah catatan (optional)<br>6. Submit<br>7. Update Laporan.ai_kategori & log action<br>8. Notifikasi audit trail |
| **Postcondition** | Kategori diubah; old & new value logged |
| **Exception** | Invalid kategori selected → error "Invalid category"<br>Laporan locked → error "Cannot change locked report" |
| **Constraint** | Hanya admin; kategori harus dari enum JENIS_KEKERASAN_CHOICES |
| **Related Models** | Laporan, Progress (untuk log) |
| **Related Views** | override_kategori() |

---

### E. CASE MANAGEMENT (5-TAHAPAN PPKPT)

#### FR-013: Update Status Laporan (5-Tahapan)

| Attribute | Value |
|-----------|-------|
| **ID** | FR-013 |
| **Feature Name** | Update Status Laporan (5-Tahapan PPKPT) |
| **Category** | Case Management |
| **Priority** | HIGH |
| **Actor** | Admin |
| **Precondition** | Laporan approved; admin akses laporan detail |
| **Main Flow** | 1. Admin buka laporan<br>2. Status saat ini tampil di timeline<br>3. Admin klik "Update Status"<br>4. Select status baru dari dropdown (valid transitions only)<br>5. Input catatan (wajib untuk status tertentu)<br>6. Optional: assign person handling tahapan berikutnya<br>7. Click "Save"<br>8. Create Progress entry dengan status, catatan, oleh, tanggal<br>9. Notif pelapor tentang status change<br>10. Log audit trail |
| **Postcondition** | Laporan.status updated; Progress entry created; pelapor notified; audit logged |
| **Status Transitions** | diterima → verifikasi_awal → wawancara_pelapor → pengumpulan_bukti → wawancara_terlapor → analisis_kronologi → rapat_pemutusan → rekomendasi → pelaksanaan → ditutup |
| **Exception** | Invalid status transition → error "Invalid status change"<br>Required catatan missing → error "Please add notes"<br>Laporan locked → error "Cannot update locked report" |
| **Constraint** | Status must follow PPKPT workflow; some status require catatan; timeline tracked |
| **Related Models** | Laporan, Progress |
| **Related Views** | update_laporan_status() |

---

#### FR-014: View Progress Timeline

| Attribute | Value |
|-----------|-------|
| **ID** | FR-014 |
| **Feature Name** | Lihat Timeline Progress (Visual) |
| **Category** | Case Management |
| **Priority** | HIGH |
| **Actor** | User (Pelapor) / Admin |
| **Precondition** | Laporan ada; user akses laporan detail |
| **Main Flow** | 1. User buka laporan<br>2. Sistem tampilkan timeline visual:<br>   - 5 tahapan PPKPT (boxes)<br>   - Current tahapan highlight<br>   - Status di setiap tahapan<br>   - Tanggal masuk/selesai tahapan<br>   - Catatan admin (jika ada)<br>3. User lihat progress dari awal hingga saat ini<br>4. Optional: expand setiap tahapan untuk detail |
| **Postcondition** | Timeline displayed; user informed about progress |
| **Exception** | No progress data → show "Report just created"<br>Timeline data corrupted → show error message |
| **Constraint** | Timeline read-only untuk user (pelapor); timeline editable untuk admin |
| **Related Models** | Laporan, Progress |
| **Related Views** | laporan_detail() |

---

### F. KOMUNIKASI (COMMUNICATION)

#### FR-015: Send Message dari Admin ke Pelapor

| Attribute | Value |
|-----------|-------|
| **ID** | FR-015 |
| **Feature Name** | Admin Kirim Pesan ke Pelapor |
| **Category** | Komunikasi |
| **Priority** | HIGH |
| **Actor** | Admin |
| **Precondition** | Laporan ada; admin akses laporan detail |
| **Main Flow** | 1. Admin klik "Send Message"<br>2. Optional: select template message (for common messages)<br>3. Input/edit pesan<br>4. Click "Send"<br>5. Create PelaporResponse entry (atau Message model)<br>6. Send email notif ke pelapor<br>7. Log message (audit trail)<br>8. Update laporan.updated_at |
| **Postcondition** | Message sent; pelapor notified via email; message logged |
| **Exception** | Pelapor no email → warning "Email not available"<br>Email service down → queue untuk retry<br>Message empty → error "Message cannot be empty" |
| **Constraint** | Max 1000 karakter per message; template messages for common cases |
| **Related Models** | PelaporResponse, Laporan |
| **Related Views** | send_message() |

---

#### FR-016: Pelapor Reply Message

| Attribute | Value |
|-----------|-------|
| **ID** | FR-016 |
| **Feature Name** | Pelapor Balas Pesan Admin |
| **Category** | Komunikasi |
| **Priority** | MEDIUM |
| **Actor** | User (Pelapor) |
| **Precondition** | Ada pesan dari admin; pelapor login; akses laporan detail |
| **Main Flow** | 1. Pelapor lihat pesan dari admin<br>2. Klik "Reply"<br>3. Input pesan balasan<br>4. Click "Send"<br>5. Create PelaporResponse entry<br>6. Notif admin tentang reply<br>7. Log message |
| **Postcondition** | Reply sent; admin notified; message logged |
| **Exception** | Message empty → error "Message cannot be empty"<br>Laporan closed → warning "Report closed, reply may not be seen" |
| **Constraint** | Max 1000 karakter; reply only boleh sampai laporan closed |
| **Related Models** | PelaporResponse |
| **Related Views** | send_response() |

---

### G. KONSELING (COUNSELING)

#### FR-017: View Jadwal Konselor

| Attribute | Value |
|-----------|-------|
| **ID** | FR-017 |
| **Feature Name** | Lihat Jadwal Konselor |
| **Category** | Konseling |
| **Priority** | HIGH |
| **Actor** | User (Pelapor) / Admin |
| **Precondition** | User login; akses menu "Booking Konseling" |
| **Main Flow** | 1. User klik "Booking Konseling"<br>2. Sistem tampilkan daftar konselor tersedia<br>3. For each konselor, tampilkan:<br>   - Nama, spesialisasi (future)<br>   - Jadwal tersedia (calendar view)<br>   - Green = tersedia, Red = penuh, Gray = off<br>4. User pilih konselor & lihat detail jadwal<br>5. Bisa filter by: hari, jam, tipe sesi (online/offline) |
| **Postcondition** | Jadwal displayed; user dapat membuat booking |
| **Exception** | No konselor available → show "No counselors available"<br>Jadwal data missing → error "Schedule not found" |
| **Constraint** | Calendar real-time; update setiap ada booking baru |
| **Related Models** | Counselor, Booking |
| **Related Views** | view_konselor_schedule() |

---

#### FR-018: Booking Sesi Konseling

| Attribute | Value |
|-----------|-------|
| **ID** | FR-018 |
| **Feature Name** | Booking Sesi Konseling |
| **Category** | Konseling |
| **Priority** | HIGH |
| **Actor** | User (Pelapor) |
| **Precondition** | User login; akses jadwal konselor; ada slot tersedia |
| **Main Flow** | 1. User klik slot konselor yang mau<br>2. Form booking muncul:<br>   - Tanggal & waktu (pre-filled)<br>   - Konselor (pre-filled)<br>   - Nama sesi (e.g., "Trauma Counseling")<br>   - Topik (optional)<br>   - Tipe sesi (Online/Offline)<br>   - Lokasi (jika offline)<br>3. User review & submit<br>4. Create Booking record dengan status `terjadwal`<br>5. Notif konselor & admin<br>6. Konfirmasi email ke pelapor |
| **Postcondition** | Booking created; status=`terjadwal`; all parties notified |
| **Exception** | Slot already taken → error "Slot no longer available"<br>User already have booking same time → error "You have conflicting booking"<br>Booking deadline passed → error "Cannot book past date" |
| **Constraint** | Min 24h advance booking; max 3 concurrent bookings per user |
| **Related Models** | Booking |
| **Related Views** | create_booking() |

---

#### FR-019: Manage Booking (Reschedule/Cancel)

| Attribute | Value |
|-----------|-------|
| **ID** | FR-019 |
| **Feature Name** | Reschedule / Cancel Booking |
| **Category** | Konseling |
| **Priority** | MEDIUM |
| **Actor** | User (Pelapor) / Admin |
| **Precondition** | Booking ada; status=`terjadwal`; at least 24h sebelum sesi |
| **Main Flow** | **Reschedule:**<br>1. User klik "Reschedule" pada booking<br>2. Pilih slot baru dari jadwal<br>3. Konfirmasi<br>4. Update Booking.tanggal & waktu<br>5. Notif konselor & pelapor<br><br>**Cancel:**<br>1. User klik "Cancel"<br>2. Input alasan (optional)<br>3. Konfirmasi<br>4. Update status=`dibatalkan`<br>5. Alasan_pembatalan recorded<br>6. Notif semua pihak |
| **Postcondition** | Booking updated atau dibatalkan; parties notified; audit logged |
| **Exception** | < 24h before booking → error "Cannot reschedule within 24 hours"<br>Booking already completed → error "Cannot modify completed booking"<br>Selected slot taken → error "Slot not available" |
| **Constraint** | Min 24h notice; max 2x reschedule per booking |
| **Related Models** | Booking |
| **Related Views** | reschedule_booking(), cancel_booking() |

---

#### FR-020: Create Rekam Medis Konseling

| Attribute | Value |
|-----------|-------|
| **ID** | FR-020 |
| **Feature Name** | Buat Rekam Medis Konseling |
| **Category** | Konseling |
| **Priority** | HIGH |
| **Actor** | Admin (Konselor) |
| **Precondition** | Booking selesai; konselor akses booking detail |
| **Main Flow** | 1. Konselor klik "Add Clinical Notes"<br>2. Form muncul:<br>   - Sesi ke- (auto-filled)<br>   - Tanggal sesi (auto-filled)<br>   - Diagnosis awal (optional)<br>   - Mood klien (1-10 scale)<br>   - Risk assessment: bunuh diri (enum), self-harm (enum)<br>   - Catatan konselor (text area, wajib)<br>   - Intervensi diberikan (e.g., CBT, mindfulness)<br>   - Progress notes (optional)<br>   - Rencana tindak lanjut (text area)<br>   - Sesi selanjutnya (date picker)<br>   - File lampiran (optional)<br>3. Submit<br>4. Create RekamMedisKonseling record<br>5. If risk = HIGH → trigger alert (admin & management)<br>6. Log creation (audit trail) |
| **Postcondition** | RekamMedisKonseling created; risk assessment triggered if needed; audit logged |
| **Exception** | Required fields missing → error "Please fill all required fields"<br>Invalid risk value → error "Invalid risk assessment"<br>Booking not found → error "Booking not found" |
| **Constraint** | Catatan CONFIDENTIAL (only konselor & admin); akses terbatas; hanya 1 rekam medis per booking |
| **Related Models** | RekamMedisKonseling, Booking |
| **Related Views** | create_rekam_medis() |

---

### H. ANALYTICS & REPORTING

#### FR-021: View Admin Dashboard

| Attribute | Value |
|-----------|-------|
| **ID** | FR-021 |
| **Feature Name** | Admin Dashboard (Analytics) |
| **Category** | Analytics |
| **Priority** | HIGH |
| **Actor** | Admin |
| **Precondition** | Admin login; akses "/admin/dashboard" |
| **Main Flow** | 1. Admin akses dashboard<br>2. Sistem tampilkan widgets:<br>   - Total laporan (all time & this month)<br>   - Laporan pending (by status)<br>   - Laporan by kategori (chart)<br>   - Laporan by urgency (chart)<br>   - Average response time<br>   - Case resolution rate<br>   - Konselor workload (bar chart)<br>   - Recent reports (list)<br>3. Dashboard real-time; update setiap 5 menit<br>4. Admin bisa filter: date range, kategori, status<br>5. Admin bisa export ke CSV/PDF |
| **Postcondition** | Dashboard rendered; data displayed; export available |
| **Exception** | Database error → show "Data unavailable"<br>Slow query → show "Loading..." dengan timeout |
| **Constraint** | Real-time; data updated every 5 min; require database optimization (indexing) |
| **Related Models** | Laporan, Progress, Booking, RekamMedisKonseling |
| **Related Views** | admin_dashboard() |

---

### I. EDUKASI & KONTEN

#### FR-022: View Educational Content

| Attribute | Value |
|-----------|-------|
| **ID** | FR-022 |
| **Feature Name** | Lihat Artikel & Video Edukasi |
| **Category** | Edukasi |
| **Priority** | MEDIUM |
| **Actor** | User (Pelapor) / Admin / Public |
| **Precondition** | Akses landing page atau menu "Pelajari" |
| **Main Flow** | 1. User akses halaman edukasi<br>2. Sistem tampilkan daftar artikel & video:<br>   - By kategori: kekerasan seksual, fisik, cyberbullying, dll<br>   - Search bar untuk cari<br>   - Filter by: kategori, tipe (artikel/video), publish date<br>3. User klik artikel/video<br>4. Display full content (artikel) atau embed video (YouTube)<br>5. User bisa share (social media)<br>6. Log view (untuk analytics) |
| **Postcondition** | Content displayed; view logged |
| **Exception** | Content not found → error "Article not found"<br>Video embed fail → show "Video unavailable" |
| **Constraint** | Content published only (is_published=True); video via YouTube embed |
| **Related Models** | Artikel (future model) |
| **Related Views** | artikel_list(), artikel_detail() |

---

### J. EMERGENCY HOTLINE & RESOURCES

#### FR-023: View Emergency Contacts

| Attribute | Value |
|-----------|lantai|
| **ID** | FR-023 |
| **Feature Name** | Lihat Kontak Darurat |
| **Category** | Edukasi |
| **Priority** | HIGH |
| **Actor** | Public / User |
| **Precondition** | Akses landing page footer atau menu |
| **Main Flow** | 1. User/Public buka halaman landing<br>2. Scroll ke footer atau klik "Emergency"<br>3. Tampilkan kontak darurat:<br>   - Hotline Ruang Dengar (phone)<br>   - WhatsApp number<br>   - Email<br>   - Lokasi kantor PPKPT<br>   - Jam operasional<br>   - External resources (RAINN, local orgs)<br>4. One-click actions: Call, WhatsApp, Email |
| **Postcondition** | Contacts displayed; clickable actions |
| **Exception** | Data not configured → show "Contact info not available" |
| **Constraint** | Visible to everyone (public); editable by admin |
| **Related Models** | Settings (future) |
| **Related Views** | landing_page() |

---

## Data Flow Requirements

### DF-001: Laporan Creation to Notification

```
User submits Laporan
    ↓
Validate form input
    ↓
Save Laporan (status=diterima)
    ↓
Trigger AI Moderation (async)
    ↓ (parallel)
├─ Analyze text with Gemini
├─ Generate kategori, urgency, toxicity
└─ Update Laporan fields
    ↓
Notif admin: new report received
    ↓
Upload Bukti page shown
```

### DF-002: Case Management Status Update

```
Admin clicks "Update Status"
    ↓
Select new status (validate transition)
    ↓
Input catatan
    ↓
Assign person (optional)
    ↓
Save & Create Progress entry
    ↓
Notif pelapor: status changed
    ↓
Notif konselor (if assigned)
    ↓
Log audit trail
```

### DF-003: Booking & Rekam Medis Flow

```
User books konseling slot
    ↓
Create Booking (status=terjadwal)
    ↓
Notif konselor & admin
    ↓
Sesi berlangsung
    ↓
Konselor create Rekam Medis
    ↓
Risk assessment (if HIGH risk → alert)
    ↓
User notified: rekam medis created
    ↓
Update Booking (status=selesai)
```

---

## Non-Functional Requirements

### NFR-001: Performance

| Requirement | Specification |
|------------|---------------|
| Page Load Time | < 2 seconds (90th percentile) |
| API Response Time | < 500ms (95th percentile) |
| Dashboard Load | < 3 seconds |
| Search Response | < 1 second |
| Concurrent Users | Support 100+ concurrent users |
| Database Query | < 100ms average |

### NFR-002: Availability & Reliability

| Requirement | Specification |
|------------|---------------|
| Uptime | 99.5% monthly |
| Mean Time to Recovery | < 30 minutes |
| Data Backup | Daily automated, tested monthly |
| Disaster Recovery | RTO < 4 hours, RPO < 1 hour |

### NFR-003: Security

| Requirement | Specification |
|------------|---------------|
| Authentication | 2FA (optional), SSO via OAuth 2.0 |
| Encryption | TLS 1.2+ for transit; AES-256 at rest |
| Password Policy | Min 8 chars, complexity required |
| Session Timeout | 30 min inactivity |
| Audit Logging | All user actions logged (immutable) |
| Penetration Testing | Quarterly security audit |

### NFR-004: Usability

| Requirement | Specification |
|------------|---------------|
| Accessibility | WCAG 2.1 Level AA |
| Mobile Responsive | Works on iOS 12+, Android 8+ |
| Language | Indonesian primary, English secondary |
| Error Messages | Clear, actionable, in user language |
| Help & Support | In-app help, FAQ, email support |

### NFR-005: Scalability

| Requirement | Specification |
|------------|---------------|
| Horizontal Scaling | Support multiple app servers |
| Database Scaling | PostgreSQL with read replicas |
| Caching | Redis for sessions & API responses |
| File Storage | S3 or equivalent for files |
| CDN | CloudFlare or equivalent for static content |

---

## Constraint & Assumptions

### Technical Constraints

1. **Framework**: Django 5.2+ (Python)
2. **Database**: PostgreSQL 12+
3. **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
4. **External APIs**: Gemini API (Google)
5. **Hosting**: Heroku, DigitalOcean, AWS, atau self-hosted

### Assumption

1. Users have internet connection
2. Email service available (SMTP)
3. Microsoft Entra ID available untuk SSO
4. Gemini API key available (or fallback to keyword-based)
5. File storage available (local atau cloud)
6. Database backup service available

### Timeline Constraints

- **MVP (Phase 1)**: Jan 15, 2025
- **Phase 2**: Apr 1, 2025
- **Phase 3**: Jul 1, 2025
- **Phase 4**: Oct 1, 2025+

### Regulatory Constraints

- GDPR compliance for data protection
- Indonesia Personal Data Protection Law (UU PDP)
- University internal policies & procedures
- PPKPT standard operational procedures

---

## Priority Classification

| Priority | Meaning | Example |
|----------|---------|---------|
| **HIGH** | Must-have for MVP launch | FR-001, FR-004, FR-013 |
| **MEDIUM** | Should-have; enhance UX | FR-003, FR-006, FR-018 |
| **LOW** | Nice-to-have; future phase | FR-022, advanced analytics |

---

**Document Version**: 1.0  
**Last Updated**: December 15, 2025  
**Next Review**: January 2025 (after MVP launch)  
**Maintainer**: Ruang Dengar Development Team
