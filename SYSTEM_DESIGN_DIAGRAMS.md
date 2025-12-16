# System Design Diagrams
## 3.4.3 - 3.4.5 Class, Activity & Sequence Diagrams

**Ruang Dengar Platform**  
**Version**: 1.0  
**Last Updated**: December 15, 2025

---

## 📋 Table of Contents

1. [3.4.3 Class Diagram](#343-class-diagram)
2. [3.4.4 Activity Diagram](#344-activity-diagram)
3. [3.4.5 Sequence Diagram](#345-sequence-diagram)

---

## 3.4.3 Class Diagram

### Overview
Class Diagram menunjukkan struktur Django models dan relationships antar entitas dalam Ruang Dengar Platform.

### Mermaid Class Diagram

```mermaid
classDiagram
    class CustomUser {
        +UUID id
        +EmailField email
        +CharField nama_lengkap
        +CharField nim
        +CharField nidn
        +CharField status_pengguna
        +CharField fakultas
        +CharField prodi
        +BooleanField is_active
        +BooleanField is_staff
        +BooleanField is_superuser
        +CharField role
        +ImageField profile_picture
        +DateTimeField created_at
        +DateTimeField updated_at
        +__str__() String
        +save() void
    }
    
    class Laporan {
        +int id
        +ForeignKey pelapor
        +CharField jenis
        +BooleanField is_anonim
        +BooleanField apakah_korban_langsung
        +CharField nama_korban
        +CharField nim_nip_korban
        +CharField status_korban
        +CharField fakultas_korban
        +CharField prodi_korban
        +CharField jenis_kelamin_korban
        +IntegerField jumlah_terlapor
        +CharField nama_terlapor
        +CharField nim_nip_terlapor
        +CharField asal_instansi_terlapor
        +TextField cronologi_singkat
        +TextField deskripsi
        +CharField lokasi
        +URLField link_pelaporan
        +CharField status
        +CharField kode_laporan
        +CharField ai_kategori
        +CharField ai_urgency
        +FloatField ai_toxicity_score
        +BooleanField ai_needs_blur
        +BooleanField ai_analyzed
        +DateTimeField created_at
        +DateTimeField updated_at
        +__str__() String
        +get_status_display() String
        +calculate_days_pending() int
    }
    
    class Evidence {
        +int id
        +ForeignKey laporan
        +FileField file
        +CharField keterangan
        +ForeignKey uploaded_by
        +DateTimeField uploaded_at
        +BigIntegerField file_size
        +CharField file_type
        +BooleanField is_blurred
        +__str__() String
        +get_file_url() String
    }
    
    class Progress {
        +int id
        +ForeignKey laporan
        +CharField status_saat_ini
        +CharField tahapan_sebelumnya
        +TextField catatan
        +ForeignKey oleh
        +ForeignKey assigned_to
        +DateTimeField created_at
        +DateTimeField updated_at
        +__str__() String
        +get_timeline() List
    }
    
    class PelaporResponse {
        +int id
        +ForeignKey laporan
        +ForeignKey dari
        +TextField pesan
        +CharField tipe
        +DateTimeField created_at
        +DateTimeField updated_at
        +BooleanField is_read
        +__str__() String
    }
    
    class Counselor {
        +int id
        +OneToOneField user
        +CharField spesialisasi
        +IntegerField pengalaman_tahun
        +CharField sertifikasi
        +TextField bio
        +CharField lokasi_kantor
        +BooleanField is_available
        +IntegerField max_slots_per_day
        +__str__() String
        +get_available_slots() List
    }
    
    class Booking {
        +int id
        +ForeignKey pelapor
        +ForeignKey konselor
        +DateField tanggal
        +TimeField waktu_mulai
        +IntegerField durasi
        +CharField tipe_sesi
        +CharField lokasi
        +CharField topik
        +CharField nama_sesi
        +CharField status
        +TextField alasan_pembatalan
        +DateTimeField created_at
        +DateTimeField updated_at
        +__str__() String
        +is_past() Boolean
        +can_reschedule() Boolean
    }
    
    class RekamMedisKonseling {
        +int id
        +OneToOneField booking
        +ForeignKey pelapor
        +ForeignKey konselor
        +IntegerField sesi_ke
        +DateField tanggal_sesi
        +CharField diagnosis_awal
        +IntegerField mood_klien
        +CharField risk_bunuh_diri
        +CharField risk_self_harm
        +TextField catatan_konselor
        +CharField intervensi
        +TextField progress_notes
        +TextField rencana_tindak_lanjut
        +DateField sesi_selanjutnya
        +FileField file_lampiran
        +DateTimeField created_at
        +DateTimeField updated_at
        +__str__() String
        +is_high_risk() Boolean
    }
    
    CustomUser "1" --> "*" Laporan : creates
    CustomUser "1" --> "*" Evidence : uploads
    CustomUser "1" --> "*" Progress : updates
    CustomUser "1" --> "*" PelaporResponse : sends
    CustomUser "1" --> "0..1" Counselor : is
    Counselor "1" --> "*" Booking : schedules
    CustomUser "1" --> "*" Booking : makes
    Booking "1" --> "1" RekamMedisKonseling : generates
    Laporan "1" --> "*" Evidence : has
    Laporan "1" --> "1" Progress : tracks
    Laporan "1" --> "*" PelaporResponse : receives
```

### Key Relationships

| Relationship | Type | Description |
|---|---|---|
| CustomUser → Laporan | 1:N | User sebagai pelapor dapat membuat banyak laporan |
| Laporan → Evidence | 1:N | Satu laporan dapat memiliki banyak bukti/file |
| Laporan → Progress | 1:1 | Satu laporan memiliki satu timeline progress |
| Laporan → PelaporResponse | 1:N | Satu laporan dapat memiliki banyak pesan/komunikasi |
| Counselor → Booking | 1:N | Satu konselor dapat memiliki banyak booking |
| CustomUser → Booking | 1:N | Satu user dapat membuat banyak booking |
| Booking → RekamMedisKonseling | 1:1 | Satu booking menghasilkan satu rekam medis |

---

## 3.4.4 Activity Diagram

### Overview
Activity Diagram menggambarkan alur proses (workflow) untuk fitur-fitur utama sistem.

### AD-001: Laporan Creation Workflow

```mermaid
flowchart TD
    Start([Start]) --> A[User akses Buat Laporan]
    A --> B[Isi form laporan:<br/>- Jenis kekerasan<br/>- Apakah anonim?<br/>- Data korban<br/>- Data terlapor<br/>- Kronologi & deskripsi<br/>- Lokasi]
    B --> C[Submit form]
    C --> D{Form valid?}
    D -->|No| E[Tampilkan error message]
    E --> F[User edit form]
    F --> C
    D -->|Yes| G[Simpan Laporan<br/>status=diterima]
    G --> H[Generate kode laporan unik<br/>Format: RD-YYYYMMDD-NNN]
    H --> I[Trigger AI Moderation async job]
    I --> J1[Call Gemini API]
    I --> J2[Notif admin: new report]
    J1 --> K1[Analyze text<br/>urgency, toxicity]
    K1 --> L1[Update ai_kategori,<br/>ai_urgency]
    J2 --> K2[Send email to admin]
    L1 --> M[Redirect ke Upload Bukti]
    K2 --> M
    M --> N[User upload evidence files]
    N --> O[Notif: Laporan diterima,<br/>tunggu verifikasi]
    O --> End([End])
    
    style G fill:#ffcccc
    style H fill:#ffffcc
    style I fill:#ccffcc
    style J1 fill:#ccccff
    style J2 fill:#ffccff
```

### AD-002: Status Update & Case Management Workflow

```mermaid
flowchart TD
    Start([Start]) --> A[Admin akses laporan detail]
    A --> B[Lihat status saat ini & timeline]
    B --> C[Klik Update Status]
    C --> D[Select status baru dari dropdown]
    D --> E{Validasi: transisi valid?}
    E -->|No| F[Error: Invalid status transition]
    F --> G[Show allowed transitions]
    G --> H[User select lagi]
    H --> E
    E -->|Yes| I[Input catatan<br/>wajib untuk status tertentu]
    I --> J[Optional: assign person<br/>untuk tahapan berikutnya]
    J --> K[Review & submit]
    K --> L[Create Progress entry:<br/>status, catatan, oleh, tanggal]
    L --> M[Update Laporan.status]
    M --> N[Notif pelapor: status changed<br/>Email + in-app notification]
    N --> O[Log audit trail]
    O --> P[Update updated_at timestamp]
    P --> End([End])
    
    style L fill:#ccffcc
    style M fill:#ccffcc
    style N fill:#ffcccc
    style O fill:#ffffcc
```

### AD-003: Booking & Konseling Workflow

```mermaid
flowchart TD
    Start([Start]) --> A[User akses Booking Konseling]
    A --> B[Lihat jadwal konselor tersedia]
    B --> C[Select konselor & slot yang mau]
    C --> D{Check: slot available?}
    D -->|No| E[Error: Slot taken]
    E --> F[Refresh jadwal]
    F --> G[User select lagi]
    G --> D
    D -->|Yes| H[Isi form booking:<br/>- Konselor, tanggal, waktu<br/>- Tipe sesi online/offline<br/>- Topik]
    H --> I{Validasi:<br/>Min 24h advance?<br/>No conflict?}
    I -->|No| J[Error message]
    J --> K[User edit]
    K --> H
    I -->|Yes| L[Create Booking<br/>status=terjadwal]
    L --> M1[Notif konselor]
    L --> M2[Notif pelapor konfirmasi email]
    L --> M3[Update jadwal reserved]
    M1 --> N[Sesi tiba]
    M2 --> N
    M3 --> N
    N --> O[Konselor update booking<br/>status=berlangsung]
    O --> P[Sesi selesai]
    P --> Q[Konselor create Rekam Medis Konseling]
    Q --> R[Input: risk assessment,<br/>catatan, intervensi]
    R --> S{Risk = HIGH?}
    S -->|Yes| T1[Trigger alert ke<br/>admin & management]
    S -->|No| T2[Log creation]
    T1 --> U[Update Booking<br/>status=selesai]
    T2 --> U
    U --> V[Notif pelapor:<br/>rekam medis created]
    V --> End([End])
    
    style L fill:#ccccff
    style Q fill:#ffcccc
    style S fill:#ffffcc
    style T1 fill:#ff9999
```

### AD-004: AI Moderation Workflow

```mermaid
flowchart TD
    Start([Start]) --> A[Laporan dibuat trigger event]
    A --> B[Extract text:<br/>jenis + deskripsi + kronologi]
    B --> C{Check: Gemini API available?}
    C -->|Yes| D[Call Gemini API]
    C -->|No| E[Fallback: keyword-based classification]
    D --> F{Response received<br/>within 2 min?}
    F -->|Yes| G[Parse JSON response]
    F -->|Timeout| E
    G --> H[Extract: urgency,<br/>toxicity_score, needs_blur]
    H --> I{Validasi JSON structure?}
    I -->|No| J[Use default values]
    J --> K[Log warning]
    I -->|Yes| L[Update Laporan fields]
    K --> L
    E --> L
    L --> M[Set fields:<br/>- ai_kategori<br/>- ai_urgency<br/>- ai_toxicity_score<br/>- ai_needs_blur<br/>- ai_analyzed = True]
    M --> N{Check: ai_urgency<br/>= DARURAT?}
    N -->|Yes| O[Trigger escalation alert]
    O --> P[Notif admin untuk<br/>review urgent case]
    N -->|No| Q[Log AI result audit trail]
    P --> Q
    Q --> End([End])
    
    style D fill:#ccccff
    style E fill:#ffffcc
    style L fill:#ccffcc
    style O fill:#ff9999
    style P fill:#ff9999
```

---

## 3.4.5 Sequence Diagram

### Overview
Sequence Diagram menunjukkan interaksi antar komponen sistem dalam urutan waktu.

### SD-001: Laporan Creation Sequence

```mermaid
sequenceDiagram
    participant U as User
    participant WA as WebApp
    participant DB as Django Backend
    participant PG as PostgreSQL
    participant GA as Gemini API
    participant ES as Email Service
    participant ADM as Admin
    
    U->>WA: Klik "Buat Laporan"
    WA->>WA: Load form template
    WA-->>U: Tampilkan form
    
    U->>WA: Isi form & submit
    WA->>DB: POST /laporan/create/
    DB->>DB: Validasi input
    DB->>PG: INSERT Laporan (status=diterima)
    PG-->>DB: Return laporan_id & kode_laporan
    DB->>DB: Trigger AI moderation job (async)
    
    par AI Moderation
        DB->>GA: Call Gemini API<br/>(extract text + prompt)
        GA-->>DB: JSON response<br/>{urgency, toxicity_score, needs_blur}
        DB->>DB: Parse & validate response
        DB->>PG: UPDATE Laporan<br/>(ai_kategori, ai_urgency, ai_toxicity_score)
        PG-->>DB: OK
    and Admin Notification
        DB->>ES: Send email<br/>(Admin notif: new report)
        ES-->>ADM: Email received
    end
    
    DB-->>WA: Redirect /laporan/id/upload-bukti/
    WA-->>U: Tampilkan "Upload Bukti" page
    
    Note over U,ADM: Laporan successfully created & submitted
```

### SD-002: Status Update Sequence

```mermaid
sequenceDiagram
    participant ADM as Admin
    participant WA as WebApp
    participant DB as Django Backend
    participant PG as PostgreSQL
    participant ES as Email Service
    participant U as User
    participant AL as AuditLog
    
    ADM->>WA: Klik "Update Status" pada laporan
    WA->>DB: GET /laporan/id/update-status/
    DB-->>WA: Form template dengan status options
    
    ADM->>WA: Select new status & input catatan
    WA->>DB: POST /laporan/id/update-status/
    
    DB->>DB: Validasi status transition
    DB->>DB: Validasi catatan (jika wajib)
    
    DB->>PG: INSERT Progress<br/>(laporan_id, status, catatan, oleh)
    PG-->>DB: Progress created
    
    DB->>PG: UPDATE Laporan<br/>(status=new_status, updated_at)
    PG-->>DB: OK
    
    DB->>AL: Log action:<br/>(admin, action, laporan_id, old_status, new_status)
    AL-->>DB: Audit logged
    
    DB->>ES: Send email to User<br/>(Subject: "Status laporan berubah")
    ES-->>U: Email received
    
    DB-->>WA: Redirect /laporan/id/detail/
    WA-->>ADM: Tampilkan updated status & timeline
    
    Note over ADM,U: Status update successful & notified
```

### SD-003: Booking Sequence

```mermaid
sequenceDiagram
    participant U as User
    participant WA as WebApp
    participant DB as Django Backend
    participant PG as PostgreSQL
    participant ES as Email Service
    participant C as Counselor
    
    U->>WA: Akses "Booking Konseling"
    WA->>DB: GET /booking/available/
    DB->>PG: SELECT jadwal konselor<br/>(WHERE is_available=True AND tanggal >= today)
    PG-->>DB: Jadwal list
    
    DB-->>WA: Jadwal list (JSON)
    WA-->>U: Tampilkan calendar & konselor options
    
    U->>WA: Select konselor & slot
    WA->>WA: Client-side validation<br/>(min 24h advance)
    WA->>DB: POST /booking/create/
    
    DB->>DB: Validasi:<br/>- Slot available?<br/>- No conflict?<br/>- 24h advance check?
    DB->>PG: SELECT COUNT(Booking)<br/>WHERE slot=selected AND status!=DIBATALKAN
    PG-->>DB: Availability status
    
    alt Slot Available
        DB->>PG: INSERT Booking<br/>(pelapor, konselor, tanggal, waktu, status=TERJADWAL)
        PG-->>DB: booking_id created
        
        DB->>DB: Reserve slot (update jadwal)
        
        par Email Notifications
            DB->>ES: Send email to Counselor<br/>(New booking notification)
            ES-->>C: Email received
        and
            DB->>ES: Send email to User<br/>(Confirmation)
            ES-->>U: Email received
        end
        
        DB-->>WA: Success response + booking_id
        WA-->>U: Tampilkan "Booking Confirmed"
    else Slot Not Available
        DB-->>WA: Error: "Slot taken"
        WA-->>U: Tampilkan error & refresh jadwal
    end
    
    Note over U,C: Booking successfully created
```

### SD-004: Rekam Medis Creation Sequence (High Risk Alert)

```mermaid
sequenceDiagram
    participant C as Counselor
    participant WA as WebApp
    participant DB as Django Backend
    participant PG as PostgreSQL
    participant ES as Email Service
    participant MGMT as Management
    participant AL as AuditLog
    
    C->>WA: Klik "Add Clinical Notes" setelah booking selesai
    WA->>DB: GET /booking/id/rekam-medis/form/
    DB-->>WA: Form template
    
    C->>WA: Isi form:<br/>- mood_klien<br/>- risk_bunuh_diri<br/>- risk_self_harm<br/>- catatan<br/>- intervensi<br/>- rencana_lanjut
    WA->>DB: POST /booking/id/rekam-medis/create/
    
    DB->>DB: Validasi form fields
    DB->>PG: INSERT RekamMedisKonseling<br/>(booking_id, sesi_ke, catatan, risk_scores)
    PG-->>DB: rekam_medis_id created
    
    DB->>DB: Assess risk level<br/>if (risk_bunuh_diri=TINGGI OR risk_self_harm=TINGGI)
    
    alt High Risk Detected
        DB->>ES: Send HIGH RISK ALERT email<br/>(To: Management)
        ES-->>MGMT: Alert email received
        
        DB->>DB: Create urgent ticket/task<br/>(For management review)
        
        Note right of DB: Escalation triggered!
    else Low/Medium Risk
        DB->>DB: Standard logging
    end
    
    DB->>AL: Log creation:<br/>(konselor, booking_id, risk_assessment, timestamp)
    AL-->>DB: Audit logged
    
    DB->>PG: UPDATE Booking<br/>(status=SELESAI)
    PG-->>DB: OK
    
    DB-->>WA: Success response
    WA-->>C: Tampilkan "Rekam medis saved"
    
    Note over C,MGMT: Rekam medis created<br/>High risk escalation triggered
```

### SD-005: Evidence Upload & Blur Sequence

```mermaid
sequenceDiagram
    participant U as User
    participant WA as WebApp
    participant DB as Django Backend
    participant FS as FileStorage
    participant PG as PostgreSQL
    participant IP as ImageProcessor
    
    U->>WA: Akses "Upload Bukti"
    WA-->>U: Tampilkan upload form
    
    U->>WA: Select file & input keterangan
    WA->>WA: Client-side validation<br/>(file size, type)
    WA->>DB: POST /evidence/upload/
    
    DB->>DB: Validate:<br/>- File size <= 10MB?<br/>- File type allowed?<br/>- File count <= 20?
    DB->>FS: Save file (encrypted)
    FS-->>DB: file_path & file_hash
    
    DB->>PG: INSERT Evidence<br/>(laporan_id, file_path, keterangan, uploaded_by, uploaded_at)
    PG-->>DB: evidence_id created
    
    DB->>DB: Check: is_sensitive_image?<br/>(AI moderation atau manual flag)
    
    alt Needs Blur
        DB->>IP: Blur image<br/>(face, sensitive data)
        IP-->>DB: blurred_file_path
        
        DB->>PG: UPDATE Evidence<br/>(is_blurred=True)
        PG-->>DB: OK
    else No Blur Needed
        DB->>DB: Mark is_blurred=False
    end
    
    DB->>PG: UPDATE Evidence<br/>(is_blurred, file_size)
    PG-->>DB: OK
    
    DB-->>WA: Success response
    WA-->>U: "File uploaded successfully"
    
    Note over U,PG: Evidence stored & processed
```

---

## Diagram Legend

### Activity Diagram Symbols
- **Oval**: Start/End
- **Rectangle**: Activity/Action
- **Diamond**: Decision point (if/then/else)
- **Arrow**: Flow direction
- **Fork/Join**: Parallel activities
- **Note**: Additional information

### Sequence Diagram Symbols
- **Actor**: External user/system
- **Participant**: Component/service
- **Arrow**: Synchronous message (→)
- **Dashed Arrow**: Return message (-->)
- **Alt/Loop**: Conditional/loop behavior
- **Note**: Additional context

### Color Coding
- **Red**: Create/Insert operations
- **Green**: Update operations
- **Blue**: Retrieve/Query operations
- **Yellow**: External API calls
- **Purple**: Validation & business logic

---

## Key Workflow States

### Laporan Status States
```
diterima 
  ↓ (admin verify)
verifikasi_awal 
  ↓ (schedule interview)
wawancara_pelapor 
  ↓ (collect evidence)
pengumpulan_bukti 
  ↓ (interview subject)
wawancara_terlapor 
  ↓ (analyze)
analisis_kronologi 
  ↓ (internal meeting)
rapat_pemutusan 
  ↓ (generate recommendation)
rekomendasi 
  ↓ (implement action)
pelaksanaan 
  ↓ (case closed)
ditutup
```

### Booking Status States
```
TERJADWAL 
  ↓ (session starts)
BERLANGSUNG 
  ↓ (session ends)
SELESAI 
  ↓ OR (user cancels 24h+)
DIBATALKAN
```

### Rekam Medis Risk Levels
```
TINGGI (High Risk)
  → Immediate escalation to management
  → Email alert
  → Urgent review task created

SEDANG (Medium Risk)
  → Logged for monitoring
  → Standard follow-up

RENDAH (Low Risk)
  → Normal case handling
```

---

## Integration Points

### External Systems
1. **Gemini API**: AI moderation for content analysis
2. **Email Service**: SMTP untuk notifikasi & komunikasi
3. **File Storage**: S3/Local untuk evidence & lampiran
4. **Microsoft Entra ID**: SSO authentication (oauth2)
5. **Database**: PostgreSQL untuk persistent storage

### Async Jobs (Celery/APScheduler)
- AI moderation (laporan create)
- Bulk email notifications
- Data backup & archival
- Report generation

---

**Document Version**: 1.0  
**Last Updated**: December 15, 2025  
**Diagrams Format**: PlantUML & Mermaid (both supported in VS Code)  
**Next Review**: January 2025 (after MVP launch)
