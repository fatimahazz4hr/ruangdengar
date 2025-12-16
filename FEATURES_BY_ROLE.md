# Fitur Ruang Dengar - Pemisahan Peran (Role-Based Features)

**Version**: 1.0  
**Last Updated**: December 15, 2025

---

## 📋 Table of Contents

1. [Fitur untuk Pelapor/Korban](#fitur-untuk-pelapor--korban)
2. [Fitur untuk Admin/PPKPT](#fitur-untuk-admin--ppkpt)
3. [Fitur untuk Konselor](#fitur-untuk-konselor)
4. [Fitur Bersama (Cross-Role)](#fitur-bersama-cross-role)
5. [Access Control Matrix](#access-control-matrix)

---

## Fitur untuk Pelapor/Korban

**Peran**: Mahasiswa, Dosen, atau Tenaga Penunjang yang melaporkan kekerasan/pelecehan

### 1.1 Authentikasi & Registrasi
| Fitur | Deskripsi | Status |
|-------|-----------|--------|
| **Registrasi Akun** | Daftar dengan email kampus atau akun Google/Microsoft | ✅ Aktif |
| **SSO (Single Sign-On)** | Login dengan Microsoft Entra ID (Azure AD) / Google | ✅ Aktif |
| **Konfirmasi Email** | Validasi email kampus sebelum akses | ✅ Aktif |
| **Lupa Password** | Reset password melalui email | ✅ Aktif |
| **Dua Faktor Autentikasi (2FA)** | Keamanan tambahan (optional) | ⏳ Planned |

### 1.2 Profil & Data Pribadi
| Fitur | Deskripsi | Status |
|-------|-----------|--------|
| **Lengkapi Profil** | Isi data diri: nama, NIM, fakultas, prodi, no WA, dll | ✅ Aktif |
| **Edit Profil** | Ubah informasi pribadi kapan saja | ✅ Aktif |
| **Upload Foto Profil** | Pilih foto profil pengguna | ✅ Aktif |
| **Data Pribadi Terenkripsi** | Alamat, no telepon kerabat dilindungi | ✅ Aktif |
| **Pilihan Anonimitas** | Opsi untuk menyembunyikan identitas dari terlapor | ✅ Aktif |

### 1.3 Membuat & Mengelola Laporan
| Fitur | Deskripsi | Status |
|-------|-----------|--------|
| **Buat Laporan** | Form lengkap untuk melaporkan kekerasan | ✅ Aktif |
| **Laporan Anonim/Identitas** | Pilih apakah identitas ditampilkan ke investigator | ✅ Aktif |
| **Kategori Kekerasan** | Pilih jenis: Seksual, Fisik, Verbal, Psikologis, Cyberbullying, Stalking | ✅ Aktif |
| **Kronologi Lengkap** | Form untuk mengisi detail kejadian (tempat, waktu, kronologi) | ✅ Aktif |
| **Data Korban & Terlapor** | Isi info korban (jika bukan diri sendiri) dan terlapor | ✅ Aktif |
| **Link Dokumen Eksternal** | Bisa attach link Google Drive untuk kronologi panjang | ✅ Aktif |
| **AI Auto-Categorization** | Sistem otomatis kategorisasi dengan Gemini AI | ✅ Aktif |
| **Edit Laporan** | Ubah laporan sebelum diproses admin | ✅ Aktif |
| **Hapus Laporan** | Tarik kembali laporan sebelum review | ✅ Aktif |

### 1.4 Unggah Bukti
| Fitur | Deskripsi | Status |
|-------|-----------|--------|
| **Unggah File Bukti** | Attach foto, screenshot, dokumen sebagai bukti | ✅ Aktif |
| **Multiple File Upload** | Bisa upload beberapa file sekaligus | ✅ Aktif |
| **Tipe File Didukung** | PDF, JPG, PNG, docx, xlsx (size limit: 10MB per file) | ✅ Aktif |
| **Keterangan Bukti** | Tambahkan penjelasan untuk setiap bukti | ✅ Aktif |
| **Unggah Bukti Tambahan** | Bisa upload bukti setelah laporan dibuat (saat proses) | ✅ Aktif |

### 1.5 Tracking & Status Laporan
| Fitur | Deskripsi | Status |
|-------|-----------|--------|
| **Kode Laporan Unik** | Setiap laporan dapat ID unik (RD-20250101-001) | ✅ Aktif |
| **Lacak Status Real-Time** | Lihat tahapan laporan (diterima, verifikasi, pemeriksaan, dll) | ✅ Aktif |
| **Timeline Progress** | Visualisasi 5 tahapan PPKPT dengan status saat ini | ✅ Aktif |
| **Notifikasi Status** | Notif saat laporan masuk tahapan baru | ✅ Aktif |
| **Riwayat Laporan** | Dashboard berisi semua laporan yang pernah dibuat | ✅ Aktif |
| **Estimasi Waktu** | Perkiraan kapan laporan selesai diproses | ✅ Aktif |

### 1.6 Komunikasi dengan Admin/PPKPT
| Fitur | Deskripsi | Status |
|-------|-----------|--------|
| **Balas Progress** | Pelapor bisa respond/balas update status dari admin | ✅ Aktif |
| **Chat/Pesan** | Kirim pesan ke admin mengenai laporan | ✅ Aktif |
| **Pemberitahuan** | Notif real-time saat ada response dari admin | ✅ Aktif |
| **Lihat Catatan Admin** | Bisa baca catatan umum (tidak ada info investigasi rahasia) | ✅ Aktif |

### 1.7 Booking Konseling
| Fitur | Deskripsi | Status |
|-------|-----------|--------|
| **Lihat Jadwal Konselor** | Jadwal ketersediaan konselor | ✅ Aktif |
| **Booking Sesi Konseling** | Pesan sesi dengan konselor pilihan | ✅ Aktif |
| **Fleksibilitas Waktu** | Atur sesuai kenyamanan (offline/online) | ✅ Aktif |
| **Konfirmasi Booking** | Notif konfirmasi saat booking diterima | ✅ Aktif |
| **Reschedule/Pembatalan** | Ubah jadwal atau batalkan jika perlu | ✅ Aktif |
| **Lokasi Konseling** | Info tempat konseling (contoh: REK-407) | ✅ Aktif |
| **Catatan Admin untuk Mahasiswa** | Bisa baca instruksi dari admin (e.g., "Bawa ID card") | ✅ Aktif |
| **Riwayat Sesi** | Lihat daftar sesi yang sudah/akan dilakukan | ✅ Aktif |

### 1.8 Rekam Medis Konseling
| Fitur | Deskripsi | Status |
|-------|-----------|--------|
| **Lihat Ringkasan Sesi** | Akses terbatas ke hasil sesi (bukan catatan rahasia) | ⏳ Planned |
| **Progress Konseling** | Lihat perkembangan kesehatan mental dari sesi-sesi | ⏳ Planned |
| **Rencana Tindak Lanjut** | Pahami rencana terapi berikutnya | ⏳ Planned |

**Catatan**: Catatan lengkap konselor (`catatan_konselor`) bersifat CONFIDENTIAL dan TIDAK bisa dilihat pelapor. Hanya akses terbatas untuk pertumbuhan mereka.

### 1.9 Edukasi & Sumber Daya
| Fitur | Deskripsi | Status |
|-------|-----------|--------|
| **Baca Modul Edukasi** | Artikel tentang jenis kekerasan, cara aman lapor, dll | ✅ Aktif |
| **Video Pembelajaran** | Edukasi tentang tanda-tanda kekerasan, dukungan peer | ✅ Aktif |
| **FAQ** | Pertanyaan umum & jawaban | ✅ Aktif |
| **Kebijakan Privasi** | Jelas bagaimana data dilindungi | ✅ Aktif |
| **Hotline Darurat** | Kontak telepon & WhatsApp untuk krisis | ✅ Aktif |
| **Resources Eksternal** | Link ke organisasi bantuan kekerasan (RAINN, Lentera Hukum, dll) | ✅ Aktif |

### 1.10 Notifikasi & Alert
| Fitur | Deskripsi | Status |
|-------|-----------|--------|
| **Email Notification** | Notif ke email saat ada update laporan | ✅ Aktif |
| **In-App Notification** | Notif badge di dalam dashboard | ✅ Aktif |
| **WhatsApp Notification** | (Optional) Notif via WhatsApp untuk darurat | ⏳ Planned |
| **Push Notification** | (Optional) Notif push di browser | ⏳ Planned |
| **Mute Notification** | Matikan notif sementara jika ingin privasi | ✅ Aktif |

---

## Fitur untuk Admin/PPKPT

**Peran**: PPKPT (Pusat Pelayanan Konsultasi dan Advokasi Terpadu) + Administrator Platform

### 2.1 Authentikasi & Otorisasi
| Fitur | Deskripsi | Status |
|-------|-----------|--------|
| **Registrasi Admin** | Khusus untuk staf PPKPT/admin yang diotorisasi | ✅ Aktif |
| **Login dengan SSO** | Login institusional (Microsoft Entra ID) | ✅ Aktif |
| **Verifikasi Admin** | Approval dari super-admin sebelum akses penuh | ✅ Aktif |
| **Role-Based Access** | Hak akses berbeda: Super Admin, PPKPT, Konselor | ✅ Aktif |
| **Audit Log** | Catat semua aksi admin (siapa, kapan, apa) | ✅ Aktif |

### 2.2 Dashboard Admin
| Fitur | Deskripsi | Status |
|-------|-----------|--------|
| **Dashboard Utama** | Ringkasan KPI: total laporan, pending, selesai, dll | ✅ Aktif |
| **Inbox Laporan** | Daftar laporan baru/pending yang perlu ditindak | ✅ Aktif |
| **Filter & Sorting** | Filter by kategori, urgensi, tahapan, tanggal | ✅ Aktif |
| **Search Laporan** | Cari laporan by kode, nama pelapor, kategori | ✅ Aktif |
| **Bulk Actions** | Multi-select + aksi batch (export, assign, dll) | ⏳ Planned |
| **Quick Stats** | Widget: laporan hari ini, minggu ini, bulan ini | ✅ Aktif |

### 2.3 Review & Verifikasi Laporan
| Fitur | Deskripsi | Status |
|-------|-----------|--------|
| **Buka Laporan Detil** | Lihat semua info: pelapor, korban, terlapor, kronologi | ✅ Aktif |
| **AI Kategori Saran** | Rekomendasi kategori dari Gemini AI | ✅ Aktif |
| **AI Urgency Saran** | Rekomendasi urgensi (darurat, tinggi, sedang, rendah) | ✅ Aktif |
| **AI Toxicity Score** | Nilai toksisitas konten laporan | ✅ Aktif |
| **Override AI Kategori** | Admin bisa ubah kategori jika tidak setuju | ✅ Aktif |
| **Manual Kategorisasi** | Jika AI error, pilih kategori yang benar | ✅ Aktif |
| **Verify Evidence** | Review bukti yang diupload (foto, dokumen, dll) | ✅ Aktif |
| **Add Admin Notes** | Tulis catatan internal (tidak terlihat pelapor) | ✅ Aktif |
| **Approve/Reject Laporan** | Setuju atau tolak laporan (dengan alasan) | ✅ Aktif |
| **Assign Investigator** | Tunjuk konselor/pendamping yang handle kasus | ✅ Aktif |

### 2.4 Manajemen Kasus (Case Management)
| Fitur | Deskripsi | Status |
|-------|-----------|--------|
| **5-Tahapan PPKPT** | Track progres case melalui 5 tahapan resmi | ✅ Aktif |
| **Update Status Laporan** | Ubah status: diterima → verifikasi → pemeriksaan → penanganan → ditutup | ✅ Aktif |
| **Logging Progress** | Setiap status change tercatat dengan timestamp + catatan | ✅ Aktif |
| **Timeline Visualisasi** | Grafis menunjukkan perjalanan kasus | ✅ Aktif |
| **Assign Tahapan** | Tentukan siapa yang handle di tiap tahapan | ✅ Aktif |
| **Deadline Tracking** | Alert jika kasus melebihi waktu yang dialokasikan | ⏳ Planned |
| **Escalation Rules** | Otomatis eskalasi kasus darurat ke level atas | ✅ Aktif |

### 2.5 Manajemen Bukti
| Fitur | Deskripsi | Status |
|-------|-----------|--------|
| **Lihat Semua Bukti** | Akses ke semua file yang diupload pelapor | ✅ Aktif |
| **Download Bukti** | Simpan file untuk investigasi offline | ✅ Aktif |
| **Komentar Bukti** | Tambah catatan pada setiap bukti | ✅ Aktif |
| **Chain of Custody** | Log siapa, kapan, akses bukti | ⏳ Planned |
| **Secure Storage** | Bukti disimpan terenkripsi (GDPR compliant) | ✅ Aktif |
| **Upload Bukti Tambahan** | Admin/investigator bisa upload bukti baru | ✅ Aktif |

### 2.6 Komunikasi dengan Pelapor
| Fitur | Deskripsi | Status |
|-------|-----------|--------|
| **Kirim Update Status** | Notifikasi resmi saat status berubah | ✅ Aktif |
| **Kirim Pesan** | Hubungi pelapor dengan pertanyaan/instruksi | ✅ Aktif |
| **Request Bukti Tambahan** | Minta dokumen tambahan jika perlu | ✅ Aktif |
| **Template Pesan** | Respons standar (verifikasi awal, wawancara, dll) | ✅ Aktif |
| **Konfirmasi Penerimaan** | Verifikasi pelapor menerima pesan | ✅ Aktif |

### 2.7 Manajemen Konselor
| Fitur | Deskripsi | Status |
|-------|-----------|--------|
| **Kelola Data Konselor** | CRUD: Tambah, edit, hapus profil konselor | ✅ Aktif |
| **Kelola Jadwal Konselor** | Set jam kerja & ketersediaan | ✅ Aktif |
| **Spesialisasi Konselor** | Tag konselor: trauma, gender, krisis, dll | ⏳ Planned |
| **Assign Konselor** | Tunjuk konselor untuk pelapor tertentu | ✅ Aktif |
| **Kapasitas Konselor** | Limit booking per konselor (e.g., 5 sesi/minggu) | ✅ Aktif |
| **Riwayat Konselor** | Lihat laporan yang ditangani setiap konselor | ✅ Aktif |

### 2.8 Kelola Jadwal & Booking
| Fitur | Deskripsi | Status |
|-------|-----------|--------|
| **Lihat Semua Booking** | Daftar semua sesi konseling yang dijadwalkan | ✅ Aktif |
| **Konfirmasi/Tolak Booking** | Approve atau reject booking dari pelapor | ✅ Aktif |
| **Edit Jadwal Booking** | Ubah tanggal/waktu booking jika perlu | ✅ Aktif |
| **Batalkan Booking** | Cancel sesi dengan alasan | ✅ Aktif |
| **Remind Klien** | Send pengingat sebelum sesi (1 hari sebelum) | ⏳ Planned |
| **Ruang Konseling** | Kelola info ruangan (lokasi, fasilitas, kapasitas) | ✅ Aktif |

### 2.9 Rekam Medis Konseling
| Fitur | Deskripsi | Status |
|-------|-----------|--------|
| **Buat Rekam Medis** | Konselor/Admin catat hasil sesi | ✅ Aktif |
| **Mood Assessment** | Skala 1-10 mood klien | ✅ Aktif |
| **Risk Assessment** | Cek risiko bunuh diri & self-harm | ✅ Aktif |
| **Intervensi** | Log teknik terapi yang digunakan (CBT, mindfulness, dll) | ✅ Aktif |
| **Progress Notes** | Catat perkembangan klien | ✅ Aktif |
| **Plan Sesi Berikutnya** | Tulis rencana untuk pertemuan selanjutnya | ✅ Aktif |
| **Upload File** | Attach assessment form, hasil test, dll | ✅ Aktif |
| **Access Control** | Hanya admin + konselor pembuat yang bisa lihat | ✅ Aktif |
| **Alert Risk** | Notif jika ada risiko tinggi (bunuh diri, self-harm) | ⏳ Planned |

### 2.10 Konten Edukasi
| Fitur | Deskripsi | Status |
|-------|-----------|--------|
| **Kelola Artikel** | CRUD: Buat, edit, publikasikan artikel edukasi | ✅ Aktif |
| **Kelola Modul** | Upload materi pembelajaran (PDF, video) | ✅ Aktif |
| **FAQ Management** | Update pertanyaan & jawaban sering ditanya | ✅ Aktif |
| **Publish/Unpublish** | Kontrol konten mana yang terlihat publik | ✅ Aktif |
| **Category Content** | Tag by topik: kekerasan seksual, cyberbullying, dll | ✅ Aktif |
| **Schedule Publishing** | Jadwalkan publikasi konten | ⏳ Planned |

### 2.11 Manajemen Pengguna
| Fitur | Deskripsi | Status |
|-------|-----------|--------|
| **Lihat Semua Pengguna** | List user beserta role & status | ✅ Aktif |
| **Edit Data Pengguna** | Ubah profil mahasiswa/dosen | ✅ Aktif |
| **Reset Password User** | Bantuan jika user lupa password | ✅ Aktif |
| **Disable/Enable User** | Nonaktifkan akun jika perlu | ✅ Aktif |
| **Approve Admin Baru** | Super-admin approve registrasi admin baru | ✅ Aktif |
| **Assign Role** | Ubah role: user → admin, user → konselor, dll | ✅ Aktif |
| **Activity Log User** | Lihat aksi user (login, lapor, edit, dll) | ✅ Aktif |

### 2.12 Notifikasi & Alert
| Fitur | Deskripsi | Status |
|-------|-----------|--------|
| **Notif Laporan Baru** | Alert saat ada laporan masuk | ✅ Aktif |
| **Notif Darurat** | Urgent alert jika laporan kategori "darurat" | ✅ Aktif |
| **Notif Task** | Reminder untuk tugas pending | ✅ Aktif |
| **Email Digest** | Ringkasan harian/mingguan laporan | ⏳ Planned |
| **Configure Notification** | Admin pilih channel notif (email, in-app, dll) | ✅ Aktif |

### 2.13 Analitik & Reporting
| Fitur | Deskripsi | Status |
|-------|-----------|--------|
| **Dashboard Analitik** | KPI: jumlah laporan, kategori trending, response time | ✅ Aktif |
| **Grafik Tren** | Visualisasi laporan by bulan, kategori, lokasi | ✅ Aktif |
| **Export Report** | Hasilkan laporan PDF/CSV untuk leadership | ✅ Aktif |
| **Statistics by Category** | Breakdown: berapa kekerasan seksual, fisik, dll | ✅ Aktif |
| **Response Time Metrics** | Rata-rata waktu dari laporan → tindakan | ✅ Aktif |
| **Case Resolution Rate** | % kasus yang selesai vs pending | ✅ Aktif |
| **Counselor Performance** | Statistik beban kerja & kepuasan konselor | ⏳ Planned |
| **Custom Reports** | Buat query khusus untuk analisis lanjutan | ⏳ Planned |

### 2.14 Pengaturan Sistem
| Fitur | Deskripsi | Status |
|-------|-----------|--------|
| **System Settings** | Konfigurasi general platform | ✅ Aktif |
| **Email Configuration** | SMTP settings untuk notifikasi | ✅ Aktif |
| **File Upload Settings** | Batasan ukuran, tipe file | ✅ Aktif |
| **Backup & Restore** | Database backup otomatis/manual | ⏳ Planned |
| **Security Settings** | 2FA, login attempts, password policy | ✅ Aktif |
| **API Keys Management** | Kelola Gemini API key & OAuth credentials | ✅ Aktif |

---

## Fitur untuk Konselor

**Peran**: Konselor profesional yang memberikan layanan kesehatan mental

### 3.1 Authentikasi
| Fitur | Deskripsi | Status |
|-------|-----------|--------|
| **Login Konselor** | Akses dengan akun institusional | ✅ Aktif |
| **Dashboard Konselor** | Halaman utama untuk manajemen sesi | ✅ Aktif |

### 3.2 Manajemen Jadwal
| Fitur | Deskripsi | Status |
|-------|-----------|--------|
| **Set Ketersediaan** | Tentukan jam & hari kerja | ✅ Aktif |
| **Lihat Jadwal Saya** | Daftar booking yang sudah terkonfirmasi | ✅ Aktif |
| **Request Off** | Minta hari libur/tidak tersedia | ⏳ Planned |

### 3.3 Manajemen Klien
| Fitur | Deskripsi | Status |
|-------|-----------|--------|
| **Lihat Klien Saya** | Daftar pelapor yang ditugaskan ke konselor ini | ✅ Aktif |
| **Profil Klien** | Lihat data demografi & background klien | ✅ Aktif |
| **Riwayat Sesi** | Lihat semua sesi yang sudah dilakukan | ✅ Aktif |
| **Notes Klien** | Catatan pribadi (confidential) tentang klien | ✅ Aktif |

### 3.4 Rekam Medis Konseling
| Fitur | Deskripsi | Status |
|-------|-----------|--------|
| **Buat Rekam Medis** | Catat hasil sesi setelah pertemuan | ✅ Aktif |
| **Edit Rekam Medis** | Update catatan jika perlu koreksi | ✅ Aktif |
| **Mood Assessment** | Skala 1-10 kondisi klien | ✅ Aktif |
| **Risk Screening** | Assess risiko bunuh diri & self-harm | ✅ Aktif |
| **Dokumentasi Intervensi** | Log teknik terapi yang digunakan | ✅ Aktif |
| **Plan Tindak Lanjut** | Tulis rencana untuk sesi/rujukan berikutnya | ✅ Aktif |
| **Confidentiality** | Catatan TIDAK bisa dilihat klien | ✅ Aktif |

### 3.5 Komunikasi
| Fitur | Deskripsi | Status |
|-------|-----------|--------|
| **Kirim Pesan ke Klien** | Hubungi klien untuk reminder/follow-up | ✅ Aktif |
| **Menerima Pesan** | Terima response dari klien | ✅ Aktif |

### 3.6 Reporting
| Fitur | Deskripsi | Status |
|-------|-----------|--------|
| **Lihat Kasus Terpandu** | Laporan yang ditangani konselor ini | ✅ Aktif |
| **Progress Report** | Laporan perkembangan klien dari perspektif konselor | ⏳ Planned |

---

## Fitur Bersama (Cross-Role)

### 4.1 Keamanan & Privacy
| Fitur | Deskripsi | Status |
|-------|-----------|--------|
| **Password Policy** | Min 8 karakter, kombinasi huruf/angka/symbol | ✅ Aktif |
| **Session Timeout** | Auto-logout setelah 30 menit inaktif | ✅ Aktif |
| **Encryption at Rest** | Data sensitif di-encrypt di database | ✅ Aktif |
| **HTTPS/TLS** | Semua komunikasi di-encrypt in-transit | ✅ Aktif |
| **GDPR Compliance** | Data handling sesuai regulasi | ✅ Aktif |
| **Data Retention** | Kebijakan berapa lama data disimpan | ⏳ Planned |

### 4.2 Akses & Permissions
| Fitur | Deskripsi | Status |
|-------|-----------|--------|
| **Role-Based Access Control (RBAC)** | Setiap role punya hak akses berbeda | ✅ Aktif |
| **Data Isolation** | Pelapor hanya lihat data mereka sendiri | ✅ Aktif |
| **View-Only vs Edit** | Beberapa role hanya bisa baca, tidak edit | ✅ Aktif |

### 4.3 Audit & Compliance
| Fitur | Deskripsi | Status |
|-------|-----------|--------|
| **Audit Log** | Catat semua aksi user (siapa, kapan, apa) | ✅ Aktif |
| **Change History** | Lihat riwayat perubahan pada data | ✅ Aktif |
| **Compliance Report** | Export laporan untuk audit eksternal | ⏳ Planned |

### 4.4 Help & Support
| Fitur | Deskripsi | Status |
|-------|-----------|--------|
| **FAQ** | Pertanyaan umum & jawaban untuk semua role | ✅ Aktif |
| **Help Center** | Dokumentasi & tutorial | ✅ Aktif |
| **Contact Support** | Form hubungi tim support | ⏳ Planned |
| **Feedback Form** | User bisa berikan feedback/saran | ⏳ Planned |

### 4.5 Accessibility
| Fitur | Deskripsi | Status |
|-------|-----------|--------|
| **Responsive Design** | Bekerja di mobile, tablet, desktop | ✅ Aktif |
| **Dark Mode** | Mode gelap untuk kenyamanan mata | ⏳ Planned |
| **Font Resize** | User bisa ubah ukuran font | ⏳ Planned |
| **Screen Reader Support** | ARIA labels untuk aksesibilitas | ✅ Aktif |

---

## Access Control Matrix

### Data Access by Role

| Data | Pelapor | Admin | Konselor | Public |
|------|---------|-------|----------|--------|
| **Profil Pelapor Sendiri** | ✅ Edit | ✅ View | ✅ View | ❌ |
| **Data Korban** | ✅ View Own | ✅ View All | ✅ View Assigned | ❌ |
| **Data Terlapor** | ✅ Submit | ✅ View All | ✅ View Assigned | ❌ |
| **Laporan Sendiri** | ✅ View, Edit, Delete | ✅ View All | ✅ View Assigned | ❌ |
| **Bukti Laporan** | ✅ Upload Own | ✅ View, Download | ✅ View Assigned | ❌ |
| **Admin Notes** | ❌ | ✅ Create, View | ✅ Create, View | ❌ |
| **Progress Log** | ✅ View | ✅ Create, Edit | ✅ Create | ❌ |
| **Rekam Medis Konseling** | ⚠️ View Limited | ✅ View All | ✅ View Own | ❌ |
| **Booking Saya/Assigned** | ✅ Manage Own | ✅ Manage All | ✅ View Own | ❌ |
| **Semua Pengguna** | ❌ | ✅ View, Edit | ❌ | ❌ |
| **Analitik** | ❌ | ✅ View All | ⚠️ View Own Stats | ❌ |
| **Artikel Edukasi** | ✅ View | ✅ Manage | ✅ View | ✅ View |
| **Kontak Darurat** | ✅ View | ✅ Manage | ✅ View | ✅ View |

**Legend**:
- ✅ Full access
- ⚠️ Limited access
- ❌ No access

---

## Feature Roadmap

### Phase 1 (Current - Q1 2025)
✅ Authentication & Registration  
✅ Laporan CRUD dengan AI moderation  
✅ Basic case management (5 tahapan)  
✅ Booking konseling  
✅ RekamMedis dasar  

### Phase 2 (Q2 2025)
🔄 Advanced analytics dashboard  
🔄 Counselor workload optimization  
🔄 Integration dengan sistem email/SMS  
🔄 Mobile app (React Native/Flutter)  

### Phase 3 (Q3 2025)
🔄 Predictive risk assessment (ML)  
🔄 Peer support community  
🔄 Integration dengan sistem akademik universitas  
🔄 Multi-language support  

### Phase 4 (Q4 2025+)
🔄 Video call integration (Jitsi/Twilio)  
🔄 Advanced search & full-text indexing  
🔄 Export ke sistem PPKPT nasional  
🔄 Integration dengan lembaga hukum  

---

## Summary Table

| Kategori | Pelapor | Admin | Konselor |
|----------|---------|-------|----------|
| **Authentikasi** | ✅ 4 fitur | ✅ 5 fitur | ✅ 1 fitur |
| **Profil & Data** | ✅ 5 fitur | ✅ 1 fitur | ✅ 3 fitur |
| **Laporan** | ✅ 9 fitur | ✅ 9 fitur | ✅ 1 fitur |
| **Bukti** | ✅ 5 fitur | ✅ 5 fitur | ❌ |
| **Tracking** | ✅ 6 fitur | ✅ 2 fitur | ❌ |
| **Komunikasi** | ✅ 4 fitur | ✅ 5 fitur | ✅ 2 fitur |
| **Konseling** | ✅ 8 fitur | ✅ 7 fitur | ✅ 6 fitur |
| **Rekam Medis** | ⚠️ 3 fitur | ✅ 9 fitur | ✅ 6 fitur |
| **Konten** | ✅ 6 fitur | ✅ 4 fitur | ✅ 1 fitur |
| **Notifikasi** | ✅ 5 fitur | ✅ 5 fitur | ❌ |
| **Analytics** | ❌ | ✅ 8 fitur | ⚠️ 1 fitur |
| **Sistem** | ❌ | ✅ 6 fitur | ❌ |
| **TOTAL** | **61 fitur** | **66 fitur** | **30 fitur** |

---

## Notes & Recommendations

1. **Security First**: Semua fitur harus melalui security audit sebelum production
2. **User Testing**: Involve real users (pelapor, admin, konselor) dalam testing
3. **Privacy**: Ensure GDPR/Data Protection Law compliance
4. **Scalability**: Design fitur dengan pertumbuhan pengguna dalam pikiran
5. **Feedback Loop**: Gather user feedback regularly dan improve fitur

---

**Document Version**: 1.0  
**Last Updated**: December 15, 2025  
**Maintainer**: Ruang Dengar Development Team
