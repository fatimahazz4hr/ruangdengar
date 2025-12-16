# Access Control, Roadmap & Summary - Ruang Dengar

**Version**: 1.0  
**Last Updated**: December 15, 2025

---

## Table of Contents

1. [Access Control Matrix (Detailed)](#access-control-matrix-detailed)
2. [Feature Roadmap with Timeline](#feature-roadmap-with-timeline)
3. [Summary Statistics](#summary-statistics)

---

## Access Control Matrix (Detailed)

### 1.1 Tabel Lengkap - Siapa Akses Apa?

**Status Saat Ini (MVP Phase 1)**:
- 🟢 2 Roles: **User** (Pelapor) dan **Admin** (mencakup PPKPT Staff + Konselor)
- ⚠️ Konselor saat ini menggunakan role ADMIN (belum terpisah)
- 🔴 Tidak ada Super Admin terpisah (future phase)

#### **SECTION: Authentication & User Management**

| Data/Fitur | User (Pelapor) | Admin (PPKPT + Konselor) | Public |
|------------|---------|-------|--------|
| Login Sendiri | ✅ | ✅ | - |
| Reset Password Sendiri | ✅ | ✅ | - |
| View Profil Sendiri | ✅ | ✅ | - |
| Edit Profil Sendiri | ✅ | ✅ | - |
| View Profil User Lain | ❌ | ✅ View All | ❌ |
| Edit Profil User Lain | ❌ | ✅ (limited) | ❌ |
| Disable/Enable User | ❌ | ⚠️ Limited (PPKPT only) | ❌ |
| Reset Password User Lain | ❌ | ⚠️ Limited (PPKPT only) | ❌ |
| Activity Log User | ❌ | ⚠️ Limited (own actions only) | ❌ |

---

#### **SECTION: Laporan (Report Management)**

| Data/Fitur | User (Pelapor) | Admin (PPKPT + Konselor) | Public |
|------------|---------|-------|--------|
| Buat Laporan | ✅ Own | ❌ | ❌ |
| Lihat Laporan Sendiri | ✅ | ✅ View All | ❌ |
| Edit Laporan Sendiri | ✅ Draft Only | ❌ | ❌ |
| Edit Laporan Orang Lain | ❌ | ✅ | ❌ |
| Hapus Laporan Sendiri | ✅ Draft Only | ❌ | ❌ |
| Hapus Laporan Orang Lain | ❌ | ✅ | ❌ |
| Lihat AI Kategori | ✅ | ✅ | ❌ |
| Override AI Kategori | ❌ | ✅ | ❌ |
| Add Admin Notes | ❌ | ✅ | ❌ |
| View Admin Notes | ❌ | ✅ | ❌ |
| Approve/Reject Laporan | ❌ | ✅ | ❌ |
| Assign Investigator | ❌ | ✅ | ❌ |
| Change Status Laporan | ❌ | ✅ | ❌ |
| Export Laporan | ❌ | ✅ | ❌ |

---

#### **SECTION: Bukti (Evidence)**

| Data/Fitur | User (Pelapor) | Admin (PPKPT + Konselor) | Public |
|------------|---------|-------|--------|
| Upload Bukti Sendiri | ✅ | ❌ | ❌ |
| Upload Bukti di Laporan | ✅ Own | ✅ All | ❌ |
| View Bukti Sendiri | ✅ | ✅ View All | ❌ |
| Download Bukti | ✅ Own | ✅ | ❌ |
| Delete Bukti Sendiri | ✅ | ❌ | ❌ |
| Delete Bukti Orang Lain | ❌ | ✅ | ❌ |
| Add Komentar Bukti | ❌ | ✅ | ❌ |

---

#### **SECTION: Progress & Case Management**

| Data/Fitur | User (Pelapor) | Admin (PPKPT + Konselor) | Public |
|------------|---------|-------|--------|
| View Progress Laporan Sendiri | ✅ | ✅ | ❌ |
| View Progress Laporan Orang Lain | ❌ | ✅ | ❌ |
| Create Progress Entry | ❌ | ✅ | ❌ |
| Edit Progress Entry | ❌ | ✅ | ❌ |
| Update Status Laporan | ❌ | ✅ | ❌ |
| View Timeline PPKPT | ✅ Own | ✅ All | ❌ |

---

#### **SECTION: Komunikasi (Communication)**

| Data/Fitur | User (Pelapor) | Admin (PPKPT + Konselor) | Public |
|------------|---------|-------|--------|
| Lihat Pesan Sendiri | ✅ | ✅ | ❌ |
| Send Pesan ke Pelapor | ❌ | ✅ | ❌ |
| Balas Pesan dari Admin | ✅ Own | ❌ | ❌ |
| View Chat History | ✅ Own | ✅ All | ❌ |

---

#### **SECTION: Konseling (Counseling)**

| Data/Fitur | User (Pelapor) | Admin (PPKPT + Konselor) | Public |
|------------|---------|-------|--------|
| View Jadwal Konselor | ✅ | ✅ | ❌ |
| Booking Konseling | ✅ | ❌ | ❌ |
| Lihat Booking Sendiri | ✅ | ✅ | ❌ |
| Confirm Booking | ❌ | ✅ | ❌ |
| Reject Booking | ❌ | ✅ | ❌ |
| Reschedule Booking | ✅ Own | ✅ | ❌ |
| Cancel Booking | ✅ Own | ✅ | ❌ |
| Manage Konselor List | ❌ | ✅ | ❌ |
| Set Konselor Ketersediaan | ❌ | ✅ | ❌ |

---

#### **SECTION: Rekam Medis Konseling**

| Data/Fitur | User (Pelapor) | Admin (PPKPT + Konselor) | Public |
|------------|---------|-------|--------|
| Buat Rekam Medis | ❌ | ✅ | ❌ |
| View Rekam Medis (Lengkap) | ❌ | ✅ All | ❌ |
| View Ringkasan Rekam Medis | ⚠️ Own Limited | ✅ | ❌ |
| Edit Rekam Medis | ❌ | ✅ | ❌ |
| Delete Rekam Medis | ❌ | ✅ | ❌ |
| Add Risk Alert | ❌ | ✅ | ❌ |

---

#### **SECTION: Konten Edukasi**

| Data/Fitur | User (Pelapor) | Admin (PPKPT + Konselor) | Public |
|------------|---------|-------|--------|
| View Artikel | ✅ | ✅ | ✅ |
| View Video | ✅ | ✅ | ✅ |
| View FAQ | ✅ | ✅ | ✅ |
| Buat Artikel | ❌ | ✅ | ❌ |
| Edit Artikel | ❌ | ✅ | ❌ |
| Publish Artikel | ❌ | ✅ | ❌ |
| Delete Artikel | ❌ | ✅ | ❌ |

---

#### **SECTION: Analitik & Reporting**

| Data/Fitur | User (Pelapor) | Admin (PPKPT + Konselor) | Public |
|------------|---------|-------|--------|
| View Dashboard | ❌ | ✅ | ❌ |
| View Tren Laporan | ❌ | ✅ | ❌ |
| View Kategori Breakdown | ❌ | ✅ | ❌ |
| View Response Time Metrics | ❌ | ✅ | ❌ |
| Export Report | ❌ | ✅ | ❌ |

---

#### **SECTION: Pengaturan Sistem**

| Data/Fitur | User (Pelapor) | Admin (PPKPT + Konselor) | Public |
|------------|---------|-------|--------|
| View System Settings | ❌ | ⚠️ Limited | ❌ |
| Change System Settings | ❌ | ⚠️ Limited (PPKPT only) | ❌ |
| Configure Email | ❌ | ❌ | ❌ |
| Configure API Keys | ❌ | ❌ | ❌ |
| View Audit Log | ❌ | ⚠️ Limited (own actions) | ❌ |

---

### 1.2 Legend & Notasi

| Simbol | Arti |
|--------|------|
| ✅ | Full Access |
| ⚠️ | Limited/Conditional Access |
| ❌ | No Access |
| - | Not Applicable |

**Current Status (MVP Phase 1)**:
- Semua admin (PPKPT + Konselor) punya role yang sama: **ADMIN**
- Django permissions & view-level authorization digunakan untuk diferensiasi
- Super Admin tidak ada di Phase 1 (semua hal admin dihandle dari satu role)

---

### 1.3 Definisi Setiap Role (MVP Phase 1)

#### **User (Pelapor)**
- Mahasiswa, Dosen, atau Tenaga Penunjang yang melaporkan kekerasan
- Hanya bisa akses dan kelola laporan mereka sendiri
- Bisa booking konseling dan lihat progress laporan
- Privacy: tidak bisa lihat catatan admin atau rekam medis lengkap

#### **Admin**
- **PPKPT Staff** (menangani laporan, investigasi, case management)
- **Konselor** (saat ini juga punya role ADMIN untuk booking & rekam medis)
- Kelola semua laporan, bukti, progress, konseling
- Akses penuh ke platform (kecuali database backup/system settings)
- ⚠️ **Note**: Tidak ada pemisahan fine-grained permissions antara PPKPT dan Konselor (future phase)

---

## Feature Roadmap with Timeline

### 2.1 Roadmap Visual

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                        RUANG DENGAR FEATURE ROADMAP                             │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  PHASE 1: MVP (Q4 2024 - Q1 2025)  ████████████████████░░░░░░░░░░░░░░░░░░░░   │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│  Launch Date: January 15, 2025                                                │
│                                                                                 │
│  ✅ DONE (Completed in Phase 1):                                               │
│     • User authentication & registration (Email, OAuth)                        │
│     • Basic laporan CRUD (Create, Read, Update, Delete)                        │
│     • Kategori kekerasan & jenis laporan                                       │
│     • Upload bukti (Evidence management)                                       │
│     • AI moderation (Gemini API) untuk auto-categorization & urgency          │
│     • 5-Tahapan PPKPT workflow (State machine)                                │
│     • Admin dashboard (Inbox, Status tracking)                                │
│     • Booking konseling (Schedule management)                                 │
│     • RekamMedis dasar (Clinical notes)                                       │
│     • Notifikasi email (Status updates)                                        │
│     • Public landing page dengan edukasi                                      │
│     • User role management (Pelapor, Admin, Konselor)                         │
│                                                                                 │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  PHASE 2: Enhancement & Scaling (Q2 2025)  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│  Target Launch: April 2025                                                    │
│                                                                                 │
│  🔄 IN PROGRESS / PLANNED:                                                    │
│     • Advanced analytics dashboard (Tren, kategori, response time)            │
│     • Konselor workload optimization & assignment algo                        │
│     • Email/SMS integration (SendGrid, Twilio)                                │
│     • Mobile app (React Native) untuk pelapor                                 │
│     • Two-factor authentication (2FA)                                         │
│     • Bulk actions & batch processing                                         │
│     • Report export (PDF, CSV)                                                │
│     • Search & filtering optimization                                         │
│     • Improved UI/UX (dark mode, accessibility)                               │
│     • Performance optimization (caching, DB indexing)                         │
│                                                                                 │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  PHASE 3: Intelligence & Integration (Q3 2025)  ░░░░░░░░░░░░░░░░░░░░░░░░░░░  │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│  Target Launch: July 2025                                                     │
│                                                                                 │
│  🔮 PLANNED:                                                                   │
│     • Predictive risk assessment (ML model untuk suicide risk)                │
│     • Peer support community (forum, support groups)                          │
│     • Integration dengan sistem akademik universitas                          │
│     • Multi-language support (English, regional languages)                    │
│     • Advanced search & full-text indexing (Elasticsearch)                    │
│     • Automated case routing (ML-based assignment)                            │
│     • Video call integration (Jitsi/Twilio)                                   │
│     • Counselor skill-based matching                                          │
│     • Follow-up reminder automation                                           │
│                                                                                 │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  PHASE 4: Enterprise & Scale (Q4 2025 - Q1 2026)  ░░░░░░░░░░░░░░░░░░░░░░░░░░  │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│  Target Launch: October 2025                                                  │
│                                                                                 │
│  🚀 FUTURE:                                                                    │
│     • Multi-university deployment (SaaS model)                                │
│     • Integration dengan lembaga hukum (e-filing)                             │
│     • Integration dengan sistem PPKPT nasional                                │
│     • Advanced analytics untuk institutional change                           │
│     • Blockchain for evidence integrity (optional)                            │
│     • AI-powered case outcome prediction                                      │
│     • Automated compliance reporting (audit trail)                            │
│     • Admin mobile app (iOS & Android)                                        │
│                                                                                 │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  Legend:                                                                       │
│  ████ = Completed          ░░░░ = Planned          ━━━━━━ = Timeline         │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

### 2.2 Fase-Fase Detail dengan Deliverables

#### **PHASE 1: MVP Foundation (Q4 2024 - Q1 2025)**
**Status**: 🟢 In Final Testing  
**Launch Date**: January 15, 2025  
**Target Users**: 100 mahasiswa + 10 admin/konselor  

**Key Deliverables**:
- ✅ Platform dapat diakses di staging
- ✅ Semua fitur core sudah tested
- ✅ Security audit passed
- ✅ GDPR-compliant

**Milestones**:
| Milestone | Timeline | Owner |
|-----------|----------|-------|
| Beta testing (50 users) | Dec 2024 | QA Team |
| Bug fixes & optimization | Early Jan 2025 | Dev Team |
| Security audit | Mid Jan 2025 | Security |
| Production launch | Jan 15, 2025 | Product Lead |
| Monitoring & support | Jan 15 onwards | Ops Team |

---

#### **PHASE 2: Enhancement (Q2 2025)**
**Status**: 🟡 In Planning  
**Target Launch**: April 1, 2025  
**Target Users**: 500 mahasiswa + 20 admin/konselor  

**Key Features**:
| Feature | Effort | Priority | Owner |
|---------|--------|----------|-------|
| Analytics Dashboard | 40h | HIGH | Frontend + Backend |
| Mobile App (React Native) | 120h | HIGH | Mobile Team |
| SMS Integration | 20h | MEDIUM | Backend |
| 2FA Implementation | 16h | MEDIUM | Security |
| Performance Optimization | 30h | HIGH | DevOps |
| Advanced Search | 25h | MEDIUM | Backend |

**Milestones**:
| Milestone | Timeline | Owner |
|-----------|----------|-------|
| Design finalized | Feb 2025 | UX/UI |
| Development sprint 1 | Feb 1-15, 2025 | Dev |
| Development sprint 2 | Feb 15 - Mar 5, 2025 | Dev |
| QA & testing | Mar 5-20, 2025 | QA |
| Soft launch (beta users) | Mar 20, 2025 | Product |
| General availability | Apr 1, 2025 | Product |

---

#### **PHASE 3: Intelligence (Q3 2025)**
**Status**: 🔴 Backlog  
**Target Launch**: July 1, 2025  
**Target Users**: 2000+ mahasiswa, multi-universitas  

**Key Features**:
| Feature | Effort | Priority | Owner |
|---------|--------|----------|-------|
| Risk Prediction ML | 80h | HIGH | ML Engineer |
| Peer Support Community | 60h | MEDIUM | Frontend |
| Elasticsearch Integration | 40h | HIGH | DevOps |
| Video Call (Jitsi) | 30h | MEDIUM | Backend |
| Multi-language | 50h | LOW | Frontend |
| Auto-routing Algorithm | 45h | HIGH | Backend |

**Milestones**:
| Milestone | Timeline | Owner |
|-----------|----------|-------|
| ML model training | Apr-May 2025 | ML |
| Feature specs finalized | May 2025 | Product |
| Development | May-Jun 2025 | Dev |
| Testing & validation | Jun 2025 | QA |
| Soft launch | Jun 15, 2025 | Product |
| Full launch | Jul 1, 2025 | Product |

---

#### **PHASE 4: Enterprise (Q4 2025+)**
**Status**: 🔴 Future Planning  
**Target Launch**: Q4 2025  
**Target Users**: 10,000+ mahasiswa, nasional  

**Key Features**:
| Feature | Effort | Priority | Owner |
|---------|--------|----------|-------|
| SaaS Multi-Tenant | 100h | HIGH | DevOps + Backend |
| Legal Integration | 60h | HIGH | Backend |
| National System Integration | 80h | HIGH | Backend |
| Admin Mobile App | 90h | MEDIUM | Mobile |
| Blockchain Evidence | 120h | LOW | Security |
| Predictive Analytics | 70h | MEDIUM | ML |

---

### 2.3 Dependency & Risk Matrix

| Phase | Dependency | Risk | Mitigation |
|-------|-----------|------|-----------|
| Phase 1 | Gemini API availability | API rate limit | Implement fallback, queue system |
| Phase 2 | Mobile team resources | Talent shortage | Hire contractors or use pre-built templates |
| Phase 3 | ML training data | Data quality | Collect & label manually in Phase 2 |
| Phase 4 | Multi-university approval | Regulatory delay | Start advocacy in Phase 3 |

---

## Summary Statistics

### 3.1 Feature Count by Phase & Role

#### **Phase 1: MVP (Current)**
```
Total Features Implemented: 47

By Role (MVP Reality):
  User (Pelapor):        22 features
  Admin (PPKPT + Konselor):  25 features
  Public:                0 features (landing page only)

By Category:
  Authentication:     2
  Laporan:            9
  Bukti:              5
  Tracking:           6
  Komunikasi:         4
  Konseling:          8
  Edukasi:            3
```

**Note**: Konselor dan PPKPT staff sama-sama punya role `admin` di Phase 1.

#### **Phase 2: Enhancement (Planned)**
```
Additional Features: 24+

By Role:
  Pelapor:        8 features (mobile, notifications)
  Admin:          10 features (analytics, bulk actions)
  Konselor:       4 features (performance tracking)
  Public:         2 features (help center, feedback)

By Category:
  Analytics:      5
  Mobile:         6
  Integration:    5
  Security:       3
  User Experience: 5
```

#### **Phase 3: Intelligence (Planned)**
```
Additional Features: 18+

By Role:
  Pelapor:        4 features (peer support, community)
  Admin:          8 features (predictive insights, auto-routing)
  Konselor:       3 features (workload optimization)
  Public:         3 features (resource library)

By Category:
  Machine Learning: 5
  Community:        4
  Integration:      5
  Search:           4
```

#### **Phase 4: Enterprise (Planned)**
```
Additional Features: 12+

By Role:
  All roles:      Enhanced capabilities across all roles

By Category:
  SaaS:           4
  Enterprise:     5
  Compliance:     3
```

---

### 3.2 Development Effort Summary

| Phase | Total Effort (Hours) | Team Size | Duration |
|-------|---------------------|-----------|----------|
| Phase 1 | 240-300h | 5-7 people | 12 weeks |
| Phase 2 | 250-350h | 8-10 people | 8 weeks |
| Phase 3 | 300-400h | 10-12 people | 10 weeks |
| Phase 4 | 400-500h | 12-15 people | 12 weeks |
| **TOTAL** | **1190-1550h** | **Peak: 15** | **42 weeks** |

**Assumptions**:
- Includes development, testing, and deployment
- Excludes project management, documentation, training
- Assumes parallel teams for multiple features
- Includes 20% buffer for unknowns

---

### 3.3 User Growth Projection

| Phase | Expected Users | Max Concurrent | Infrastructure |
|-------|----------------|----------------|-----------------|
| Phase 1 | 100 | 5 | Single server |
| Phase 2 | 500 | 25 | Horizontal scaling |
| Phase 3 | 2000 | 100 | Load balancer + DB replica |
| Phase 4 | 10000+ | 500+ | Multi-region, CDN |

---

### 3.4 Technology Stack Evolution

| Layer | Phase 1 | Phase 2 | Phase 3 | Phase 4 |
|-------|---------|---------|---------|---------|
| **Frontend** | Django Templates | + React Web | + Mobile App | + Admin App |
| **Backend** | Django 5.2 | + REST API | + GraphQL | + Microservices |
| **Database** | PostgreSQL | PostgreSQL | + Elasticsearch | + Data Warehouse |
| **Cache** | Optional Redis | Redis | Redis Cluster | Memcached |
| **AI/ML** | Gemini API | + ML Pipeline | + TensorFlow | + Custom Models |
| **Deployment** | Heroku/DO | Docker | Kubernetes | Multi-region K8s |

---

### 3.5 Budget Estimate (If Using Contractors)

| Phase | Development | Infrastructure | Tools & License | Total |
|-------|-------------|-----------------|-----------------|-------|
| Phase 1 | $12,000 | $2,000/month | $500 | $12,500/month × 3 = **$37,500** |
| Phase 2 | $15,000 | $3,000/month | $800 | $18,800/month × 2 = **$37,600** |
| Phase 3 | $18,000 | $4,000/month | $1,200 | $23,200/month × 2.5 = **$58,000** |
| Phase 4 | $20,000 | $5,000+/month | $2,000 | $27,000/month × 3 = **$81,000** |
| **GRAND TOTAL** | | | | **~$214,100** |

**Notes**:
- Assumes $50-75/hour for contractor development
- Infrastructure costs for production environment
- Excludes internal team salaries
- Budget can be reduced with open-source tools

---

### 3.6 Risk & Mitigation Summary

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|-----------|
| API Rate Limits (Gemini) | HIGH | MEDIUM | Implement queue, fallback, cache |
| Data Breach | MEDIUM | CRITICAL | Security audit, encryption, compliance |
| User Adoption Low | MEDIUM | MEDIUM | Marketing, user testing, feedback loop |
| Resource Shortage | HIGH | MEDIUM | Hire contractors, outsource, prioritize |
| Regulatory Delays | LOW | HIGH | Early advocacy, legal consultation |
| Performance Issues at Scale | MEDIUM | MEDIUM | Caching, CDN, DB optimization |

---

### 3.7 Success Metrics by Phase

#### **Phase 1 Success Criteria**:
- ✅ Platform launches on schedule (Jan 15, 2025)
- ✅ Zero critical bugs in production
- ✅ 100+ active users within first week
- ✅ GDPR/Data Protection compliant
- ✅ 95%+ uptime
- ✅ Average response time < 2 seconds
- ✅ User satisfaction > 4.0/5.0

#### **Phase 2 Success Criteria**:
- ✅ 500+ active users
- ✅ Mobile app downloads > 1000
- ✅ Mobile app rating > 4.2/5.0
- ✅ Analytics engagement > 80%
- ✅ Average case resolution time < 30 days

#### **Phase 3 Success Criteria**:
- ✅ 2000+ active users across multiple universities
- ✅ Predictive model accuracy > 85%
- ✅ Peer community 30% user engagement
- ✅ Elasticsearch search response < 500ms
- ✅ Video call success rate > 95%

#### **Phase 4 Success Criteria**:
- ✅ 10,000+ users nationally
- ✅ Multi-university SaaS deployments > 5
- ✅ Legal integration successful
- ✅ Cost per user < $5/month

---

## Quick Reference Tables

### Summary of All Three Sections

#### **Access Control Quick Ref**
```
Role         | Akses ke Laporan | Akses Bukti | Akses Rekam Medis | Akses Analytics |
-------------|------------------|------------|-------------------|-----------------|
User         | Own Only         | Own        | Limited (Own)      | No              |
Admin        | All              | All        | All                | Yes             |
Public       | No               | No         | No                 | No              |

Note: Admin includes both PPKPT Staff and Konselor in Phase 1
```

#### **Roadmap Quick Ref**
```
Phase | When       | Users     | Key Features                    | Roles                | Status |
------|------------|-----------|--------------------------------|----------------------|--------|
1     | Q1 2025    | 100       | MVP, Laporan, Konseling        | User, Admin          | 🟢 Testing |
2     | Q2 2025    | 500       | Analytics, Mobile, SMS          | User, Admin, Konselor| 🟡 Planning |
3     | Q3 2025    | 2000      | ML, Community, Search           | +Super Admin         | 🔴 Backlog |
4     | Q4 2025+   | 10000+    | SaaS, Legal, National           | Custom roles         | 🔴 Future |
```

#### **Feature Stats Quick Ref**
```
Phase | Features | User | Admin | Effort  | Budget |
------|----------|------|-------|---------|--------|
1     | 47       | 22   | 25    | 240-300h| $37.5K |
2     | +24      | +8   | +16   | 250-350h| $37.6K |
3     | +18      | +4   | +14   | 300-400h| $58.0K |
4     | +12      | +2   | +10   | 400-500h| $81.0K |
TOTAL | 101      | 36   | 65    | 1190-1550h| $214.1K |

Note: Phase 1 = 47 features dengan 2 roles (User + Admin gabungan)
```

---

**Document Version**: 1.0  
**Last Updated**: December 15, 2025  
**Maintainer**: Ruang Dengar Development Team
