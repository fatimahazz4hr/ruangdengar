import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ruangdengar.settings')
django.setup()

from users.models import Konten

# Hapus konten lama jika ada
Konten.objects.all().delete()

# Buat konten sample
konten_list = [
    {
        'judul': 'Mengenali Kekerasan Seksual dan Dampaknya',
        'kategori': 'kesadaran',
        'deskripsi': 'Memahami berbagai bentuk kekerasan seksual, tanda-tanda, dan dampak psikologis serta sosial pada korban.',
        'konten': '''Kekerasan seksual merupakan isu kompleks dan meresahkan yang melanda berbagai lapisan masyarakat di seluruh dunia. Fenomena ini tidak hanya meninggalkan luka fisik, tetapi juga trauma psikologis yang mendalam bagi para korban.

Memahami bentuk-bentuk kekerasan seksual, tanda-tandanya, serta dampaknya adalah langkah pertama yang krusial dalam upaya pencegahan dan penanganan.

Bentuk-bentuk Kekerasan Seksual:
1. Pelecehan Seksual Verbal
2. Pelecehan Seksual Non-verbal
3. Pemaksaan Aktivitas Seksual
4. Eksploitasi Seksual

Dampak Psikologis:
- Trauma dan PTSD
- Depresi dan Kecemasan
- Gangguan Tidur
- Penurunan Kepercayaan Diri

Langkah Pencegahan:
- Edukasi sejak dini
- Membangun lingkungan yang aman
- Meningkatkan kesadaran masyarakat
- Mendukung korban tanpa menghakimi''',
        'penulis': 'Dr. Siti Aminah, S.Psi, M.A.',
    },
    {
        'judul': 'Strategi Pencegahan Kekerasan Seksual di Lingkungan Kampus',
        'kategori': 'pencegahan',
        'deskripsi': 'Panduan menciptakan lingkungan aman dan mendukung di institusi pendidikan tinggi dengan langkah proaktif.',
        'konten': '''Lingkungan kampus seharusnya menjadi tempat yang aman untuk belajar dan berkembang. Namun, realitanya kekerasan seksual masih menjadi masalah serius di banyak institusi pendidikan tinggi.

Strategi Pencegahan di Kampus:

1. Kebijakan Kampus yang Jelas
   - SOP penanganan kekerasan seksual
   - Sanksi tegas bagi pelaku
   - Perlindungan untuk pelapor

2. Edukasi dan Sosialisasi
   - Workshop kesadaran gender
   - Seminar pencegahan kekerasan seksual
   - Kampanye consent dan batasan

3. Sistem Pelaporan yang Aman
   - Jalur pelaporan rahasia
   - Pendampingan profesional
   - Respon cepat dari pihak kampus

4. Lingkungan Fisik yang Aman
   - Penerangan memadai
   - CCTV di area strategis
   - Sistem keamanan 24 jam

5. Peer Support System
   - Kelompok dukungan mahasiswa
   - Buddy system untuk mahasiswa baru
   - Hotline darurat kampus''',
        'penulis': 'Tim Ruang Dengar',
    },
    {
        'judul': 'Mendukung Korban Kekerasan Seksual: Apa yang Harus Dilakukan?',
        'kategori': 'dukungan',
        'deskripsi': 'Informasi untuk memberikan dukungan empati kepada korban kekerasan seksual tanpa menghakimi.',
        'konten': '''Ketika seseorang mengungkapkan pengalaman kekerasan seksual kepada Anda, respons Anda sangat penting untuk proses pemulihan mereka.

Hal yang HARUS Dilakukan:

1. Dengarkan dengan Penuh Empati
   - Berikan perhatian penuh
   - Jangan menyela atau menghakimi
   - Validasi perasaan mereka

2. Percayai Cerita Mereka
   - Jangan mempertanyakan kebenaran
   - Hindari pertanyaan yang menyalahkan
   - Tunjukkan bahwa Anda percaya

3. Hormati Keputusan Mereka
   - Biarkan mereka yang memimpin proses
   - Jangan memaksa untuk melapor
   - Dukung pilihan mereka

4. Berikan Informasi tentang Bantuan
   - Layanan konseling
   - Hotline darurat
   - Pendampingan hukum

5. Jaga Kerahasiaan
   - Jangan menyebarkan informasi
   - Hormati privasi mereka
   - Minta izin sebelum bertindak

Hal yang TIDAK Boleh Dilakukan:
❌ Menyalahkan korban
❌ Mempertanyakan apa yang mereka kenakan
❌ Menyarankan mereka "move on"
❌ Membandingkan dengan pengalaman orang lain
❌ Mengambil alih keputusan mereka

Ingat: Dukungan Anda sangat berarti dalam proses pemulihan korban.''',
        'penulis': 'Prof. Dr. Ahmad Wijaya, M.Psi',
    },
]

print("=" * 60)
print("MEMBUAT KONTEN SAMPLE")
print("=" * 60)

for data in konten_list:
    konten = Konten.objects.create(**data)
    print(f"✓ Created: {konten.judul} (ID: {konten.id})")

print(f"\n✓ Total konten dibuat: {Konten.objects.count()}")
print("=" * 60)
