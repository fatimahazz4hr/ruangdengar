# Technology Stack - Ruang Dengar Platform

**Last Updated**: December 15, 2025  
**Version**: 1.0

---

## 📋 Table of Contents
1. [Backend](#backend)
2. [Frontend](#frontend)
3. [Database](#database)
4. [Development Tools](#development-tools)
5. [Deployment & Infrastructure](#deployment--infrastructure)
6. [Tech Stack Diagram](#tech-stack-diagram)
7. [Performance & Scalability](#performance--scalability)

---

## Backend

### Core Framework
| Technology | Version | Purpose | Link |
|------------|---------|---------|------|
| **Django** | ≥ 5.2.0 | Web framework | https://www.djangoproject.com/ |
| **Python** | 3.8+ | Programming language | https://www.python.org/ |
| **Gunicorn** | ≥ 21.2.0 | WSGI HTTP server (production) | https://gunicorn.org/ |

### Authentication & Authorization
| Technology | Version | Purpose | Link |
|------------|---------|---------|------|
| **django-allauth** | ≥ 0.57.0 | User registration, login, social auth | https://django-allauth.readthedocs.io/ |
| **PyJWT** | ≥ 2.10.0 | JWT token generation & verification | https://pyjwt.readthedocs.io/ |
| **cryptography** | ≥ 46.0.0 | Encryption & secure password handling | https://cryptography.io/ |
| **Microsoft OAuth 2.0** | - | Single Sign-On (SSO) for institutional users | https://learn.microsoft.com/oauth |

### AI & Content Moderation
| Technology | Version | Purpose | Link |
|------------|---------|---------|------|
| **google-generativeai** | ≥ 0.3.0 | Gemini API for AI content analysis | https://ai.google.dev/ |
| **Gemini Pro Model** | Latest | LLM for toxicity detection, urgency assessment | https://ai.google.dev/models/gemini |

**AI Features**:
- **Automated Report Categorization**: Kekerasan Seksual, Fisik, Verbal, Psikologis, Cyberbullying, Stalking
- **Urgency Assessment**: Darurat (Emergency), Tinggi (High), Sedang (Medium), Rendah (Low)
- **Toxicity Scoring**: 0.0-1.0 scale for content severity
- **Keyword Fallback**: Rule-based classification when API unavailable

### File & Media Handling
| Technology | Version | Purpose | Link |
|------------|---------|---------|------|
| **Pillow (PIL)** | ≥ 10.0.0 | Image processing for uploads | https://python-pillow.org/ |
| **FileField** | Django built-in | Evidence & medical record uploads | https://docs.djangoproject.com/en/5.2/ref/models/fields/#filefield |

### Caching & Sessions
| Technology | Version | Purpose | Link |
|------------|---------|---------|------|
| **Redis** | ≥ 5.0.0 | Cache backend (optional, recommended) | https://redis.io/ |
| **Django Session Framework** | Built-in | User session management | https://docs.djangoproject.com/en/5.2/topics/http/sessions/ |

### Environment & Configuration
| Technology | Version | Purpose | Link |
|------------|---------|---------|------|
| **python-decouple** | ≥ 3.8 | Environment variables management | https://github.com/HenryBriggs/python-decouple |
| **.env file** | - | Secure secrets storage (API keys, DB credentials) | https://12factor.net/config |

### API & Serialization
| Technology | Purpose | Link |
|----------|---------|------|
| **Django REST Framework** (optional for API) | JSON/REST API serialization | https://www.django-rest-framework.org/ |
| **JSON** | Data interchange format | https://www.json.org/ |

### Key Django Apps Configured
```python
INSTALLED_APPS = [
    # Django core
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',
    
    # Social authentication
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.microsoft',
    
    # Local
    'users.apps.UsersConfig',
]
```

---

## Frontend

### Core Technologies
| Technology | Purpose | Link |
|------------|---------|------|
| **HTML5** | Semantic markup | https://html.spec.whatwg.org/ |
| **CSS3** | Styling & layout | https://www.w3.org/Style/CSS/ |
| **JavaScript (Vanilla)** | Client-side interactivity | https://developer.mozilla.org/en-US/docs/Web/JavaScript |

### CSS Framework & Utilities
| Technology | Version | Purpose | Link |
|------------|---------|---------|------|
| **Tailwind CSS** | Latest (CDN) | Utility-first CSS framework | https://tailwindcss.com/ |
| **Custom CSS** | - | Component-specific styling | `static/css/` |

**Tailwind Features Used**:
- Responsive design (mobile-first)
- Flexbox & Grid layout
- Dark mode support (optional)
- Spacing, color, and typography utilities
- Custom theme variables

### Icon Library
| Technology | Version | Purpose | Link |
|------------|---------|---------|------|
| **Lucide Icons** | Latest (CDN) | Lightweight SVG icons | https://lucide.dev/ |

**Icons Used**:
- Navigation icons (menu, arrow, bell)
- Status icons (lock, check, alert)
- Category icons (shield, phone, book)
- Social icons (facebook, whatsapp, instagram)

### Typography
| Font | Provider | Usage |
|------|----------|-------|
| **Inter** | Google Fonts | Main sans-serif font, all text | https://fonts.google.com/specimen/Inter |
| **System fonts** | Fallback | If external fonts unavailable | |

### Template Engine
| Technology | Purpose | Link |
|------------|---------|------|
| **Django Templates** | Server-side rendering | https://docs.djangoproject.com/en/5.2/topics/templates/ |
| **Template Tags** | Logic & filters ({% url %}, {% static %}, {{ var }}) | https://docs.djangoproject.com/en/5.2/ref/templates/builtins/ |

### Frontend Pages & Components

**Main Pages**:
- `landing.html` — Public landing page (hero, info cards, PPKPT section)
- `users/login.html` — User login with OAuth
- `users/register_user.html` — Student registration
- `users/register_admin.html` — Admin registration
- `users/role_selection.html` — Role selection (Student/Admin)
- `base.html` — Base template (nav, footer, stylesheets)
- `base_user.html` — Authenticated user base template

**Dashboard Pages** (`templates/dashboard/`):
- `dashboard.html` — Admin main dashboard
- `kelola_laporan.html` — Manage reports
- `kelola_pengguna.html` — Manage users
- `kelola_konten.html` — Manage content
- `kelola_jadwal.html` — Manage counseling schedule
- `edit_profile.html` — Profile editor
- `notifikasi.html` — Notifications

**User Pages** (`templates/menu_users/`):
- `dashboard_user.html` — Student dashboard
- `buat_laporan.html` — Create report form
- `riwayat_laporan.html` — Report history
- `status_laporan.html` — Check report status
- `booking_konseling.html` — Counseling booking
- `edit_profile.html` — Edit student profile
- `rekam_medis_form.html` — Medical record form
- `rekam_medis_list.html` — Medical records list
- `artikel_detail.html` — Educational articles
- `kebijakan_privasi.html` — Privacy policy

**Authentication Pages** (`templates/socialaccount/`):
- `login.html` — SSO login page
- `signup.html` — SSO signup
- `authentication_error.html` — Error handling

### Frontend Features Implemented
✅ Responsive design (mobile, tablet, desktop)  
✅ Navigation bar with active link highlighting  
✅ Hamburger menu for mobile  
✅ Form validation (client-side + server-side)  
✅ Loading states & spinners  
✅ Toast/notification messages  
✅ Modal dialogs for confirmations  
✅ Dark mode toggle (if implemented)  
✅ Accessibility: ARIA labels, semantic HTML, keyboard navigation  
✅ Performance: lazy loading, image optimization  

---

## Database

### Primary Database
| Technology | Version | Purpose | Link |
|------------|---------|---------|------|
| **PostgreSQL** | 12+ (recommended) | Relational database (production) | https://www.postgresql.org/ |
| **SQLite3** | Built-in | Development & testing database | https://www.sqlite.org/ |

### Database Driver
| Technology | Version | Purpose | Link |
|------------|---------|---------|------|
| **psycopg2-binary** | ≥ 2.9.0 | PostgreSQL adapter for Python | https://www.psycopg.org/ |

### Database Models

**Core Tables**:
1. **CustomUser** — Custom user model with roles (Admin, User)
   - Fields: email (PK), nama_lengkap, nim, nidn, fakultas, role, profile_picture, etc.
   - Auth: PASSWORD_FIELD, REQUIRED_FIELDS, is_staff, is_superuser

2. **Laporan** — Violence/incident reports
   - Fields: kode (PK), jenis (violence type), status (state machine), ai_kategori, ai_urgency, ai_toxicity_score
   - Relations: ForeignKey(CustomUser) for pelapor
   - Constraints: 5-stage PPKPT workflow

3. **Evidence** — Attached files to reports
   - Fields: id (PK), laporan_id (FK), file, uploaded_at, uploaded_by
   - Relations: ForeignKey(Laporan), ForeignKey(CustomUser)

4. **Progress** — Case management audit trail
   - Fields: id (PK), laporan_id (FK), status, catatan, oleh, tanggal
   - Relations: ForeignKey(Laporan), ForeignKey(CustomUser)

5. **PelaporResponse** — Two-way communication between reporter and admin
   - Fields: id (PK), laporan_id (FK), pesan, tanggal
   - Relations: ForeignKey(Laporan), ForeignKey(Progress, optional)

6. **Booking** — Counseling session bookings
   - Fields: id (PK), user_id (FK), tanggal, waktu, konselor_fk, status
   - Relations: ForeignKey(CustomUser), ForeignKey(Counselor)
   - Status: terjadwal, selesai, dibatalkan

7. **RekamMedisKonseling** — Clinical counseling records
   - Fields: id (PK), konseling_id (FK), sesi_ke, mood_klien, risiko_bunuh_diri, risiko_self_harm, catatan_konselor
   - Relations: ForeignKey(Booking), ForeignKey(CustomUser)
   - Access: Counselor & Admin only (privacy)

8. **Counselor** — Counselor profiles
   - Fields: id (PK), name, title
   - Relations: referenced by Booking (1-to-many)

### Django ORM Features Used
- **Models**: Abstract & concrete model inheritance
- **Relationships**: ForeignKey, OneToOneField, ManyToManyField
- **Managers**: Custom QuerySets, filter, exclude, select_related, prefetch_related
- **Signals**: post_save, pre_save for automated tasks
- **Validators**: EmailField, PositiveIntegerField with MinValueValidator/MaxValueValidator
- **Choices**: TextChoices for status enums (PPKPT stages, urgency levels)

### Database Features
✅ Cascading deletes (on_delete=models.CASCADE)  
✅ Soft deletes (is_active flag on CustomUser)  
✅ Timestamps (created_at, updated_at with auto_now_add/auto_now)  
✅ Unique constraints (email, username, kode)  
✅ Indexing on frequently queried fields (status, created_at)  
✅ Full-text search (PostgreSQL tsvector, optional)  

---

## Development Tools

### Version Control
| Technology | Purpose | Link |
|------------|---------|------|
| **Git** | Distributed version control | https://git-scm.com/ |
| **GitHub** | Remote repository hosting | https://github.com/ |
| **.gitignore** | Exclude secrets, venv, __pycache__ | Standard practice |

### Python Environment
| Technology | Purpose | Link |
|------------|---------|------|
| **venv** | Python virtual environment | https://docs.python.org/3/library/venv.html |
| **pip** | Package manager | https://pip.pypa.io/ |

### Code Editor
| Technology | Purpose | Link |
|------------|---------|------|
| **Visual Studio Code** | IDE (recommended) | https://code.visualstudio.com/ |
| **VS Code Extensions** | Django, Python, Pylance, GitLens, etc. | https://marketplace.visualstudio.com/ |

### Django Management
| Tool | Purpose | Command |
|------|---------|---------|
| **manage.py** | Django CLI | `python manage.py ...` |
| **Django Admin** | Web-based model management | `/admin/` |
| **django-debug-toolbar** | Development debugging (optional) | Visual SQL, templates, cache |

### Testing & Quality Assurance
| Technology | Version | Purpose | Link |
|------------|---------|---------|------|
| **pytest** (optional) | - | Advanced testing framework | https://pytest.org/ |
| **Django TestCase** | Built-in | Unit & integration tests | https://docs.djangoproject.com/en/5.2/topics/testing/ |
| **Coverage.py** (optional) | - | Test coverage measurement | https://coverage.readthedocs.io/ |
| **Black** (optional) | - | Python code formatter | https://black.readthedocs.io/ |
| **Flake8** (optional) | - | Style guide enforcement | https://flake8.pycqa.org/ |

### API Documentation (Optional)
| Technology | Purpose | Link |
|------------|---------|------|
| **Swagger/OpenAPI** (optional) | Interactive API docs | https://swagger.io/ |
| **drf-spectacular** (optional) | Django REST Framework schema | https://drf-spectacular.readthedocs.io/ |

### Diagram & Documentation Tools
| Technology | Purpose | Format | Link |
|------------|---------|--------|------|
| **Mermaid** | Flowcharts, diagrams | `.mmd` | https://mermaid.js.org/ |
| **PlantUML** | UML diagrams | `.puml` | https://plantuml.com/ |
| **Markdown** | Documentation | `.md` | https://commonmark.org/ |

**Diagrams in Project**:
- `docs/diagrams/erd.mmd` — Entity Relationship Diagram (Mermaid)
- `docs/diagrams/ruangdengar_usecase.mmd` — Use Case Diagram (Mermaid)
- `docs/diagrams/ruangdengar_usecase.puml` — Use Case Diagram (PlantUML)

---

## Deployment & Infrastructure

### Production Server
| Technology | Purpose | Link |
|------------|---------|------|
| **Gunicorn** | WSGI application server | https://gunicorn.org/ |
| **Nginx** | Reverse proxy & static file serving | https://nginx.org/ |
| **WhiteNoise** | Static files middleware | http://whitenoise.readthedocs.io/ |

### Hosting Options
| Platform | Cost | Use Case | Link |
|----------|------|----------|------|
| **Heroku** | $50+/month | Easy deployment, auto-scaling | https://www.heroku.com/ |
| **PythonAnywhere** | $5+/month | Beginner-friendly | https://www.pythonanywhere.com/ |
| **DigitalOcean** | $5+/month | VPS, full control | https://www.digitalocean.com/ |
| **AWS** | Pay-as-you-go | Enterprise, scalable | https://aws.amazon.com/ |
| **Google Cloud** | Pay-as-you-go | Integrated with Google services | https://cloud.google.com/ |
| **Microsoft Azure** | Pay-as-you-go | SSO integration ready | https://azure.microsoft.com/ |

### Environment Variables (Production)
```env
# Django
DEBUG=False
SECRET_KEY=<secure-key>
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
ENVIRONMENT=production

# Database
DATABASE_URL=postgresql://user:password@host:5432/dbname

# Email
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=app-password

# OAuth
SOCIALACCOUNT_PROVIDERS_MICROSOFT_OAUTH_CLIENT_ID=...
SOCIALACCOUNT_PROVIDERS_MICROSOFT_OAUTH_CLIENT_SECRET=...

# AI Moderation
GEMINI_API_KEY=...

# Security
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
ALLOWED_HOSTS=yourdomain.com

# Optional: Redis
REDIS_URL=redis://user:password@host:6379/0
```

### CI/CD Pipeline (Optional)
| Tool | Purpose | Link |
|------|---------|------|
| **GitHub Actions** | Automated testing & deployment | https://github.com/features/actions |
| **Jenkins** (optional) | Advanced CI/CD | https://www.jenkins.io/ |
| **GitLab CI** (optional) | GitLab-integrated pipeline | https://about.gitlab.com/stages-devops-ci/ |

**Example GitHub Actions Workflow**:
```yaml
name: CI/CD
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
      - run: pip install -r requirements.txt
      - run: python manage.py test
      - run: black --check .
      - run: flake8 .
```

### SSL/TLS Certificate
| Provider | Cost | Purpose | Link |
|----------|------|---------|------|
| **Let's Encrypt** | FREE | HTTPS certificate | https://letsencrypt.org/ |
| **Certbot** | FREE | Automated renewal | https://certbot.eff.org/ |

### Monitoring & Logging (Optional)
| Technology | Purpose | Link |
|-----------|---------|------|
| **Sentry** | Error tracking | https://sentry.io/ |
| **Datadog** | Infrastructure monitoring | https://www.datadoghq.com/ |
| **CloudWatch** (AWS) | Centralized logging | https://aws.amazon.com/cloudwatch/ |
| **ELK Stack** (Elasticsearch, Logstash, Kibana) | Log aggregation | https://www.elastic.co/ |

---

## Tech Stack Diagram

```
┌────────────────────────────────────────────────────────────────────┐
│                     RUANG DENGAR TECH STACK                        │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │                    CLIENT LAYER (Frontend)                   │ │
│  ├──────────────────────────────────────────────────────────────┤ │
│  │ HTML5 + CSS3 + JavaScript (Vanilla)                          │ │
│  │ Tailwind CSS (CDN)                                           │ │
│  │ Lucide Icons (CDN)                                           │ │
│  │ Inter Font (Google Fonts)                                    │ │
│  │ Django Templates (Server-side rendering)                    │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                            ↓ (HTTP/HTTPS)                          │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │                 APPLICATION LAYER (Backend)                  │ │
│  ├──────────────────────────────────────────────────────────────┤ │
│  │ Django 5.2+                                                  │ │
│  │ ├─ django-allauth (Auth + OAuth)                             │ │
│  │ ├─ google-generativeai (Gemini AI Moderation)                │ │
│  │ ├─ Pillow (Image Processing)                                │ │
│  │ ├─ PyJWT (Token Management)                                 │ │
│  │ └─ cryptography (Security)                                  │ │
│  │                                                              │ │
│  │ Gunicorn (WSGI Server)                                      │ │
│  │ WhiteNoise (Static Files)                                   │ │
│  │ python-decouple (Config Management)                         │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                            ↓ (TCP/IP)                              │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │              PERSISTENCE LAYER (Data)                        │ │
│  ├──────────────────────────────────────────────────────────────┤ │
│  │ PostgreSQL 12+ (Production)                                  │ │
│  │ SQLite3 (Development/Testing)                                │ │
│  │ psycopg2-binary (DB Driver)                                 │ │
│  │                                                              │ │
│  │ Django ORM (Models, Querysets)                              │ │
│  │ Django Migrations (Schema versioning)                       │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                            ↓                                       │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │            OPTIONAL: CACHING LAYER                           │ │
│  ├──────────────────────────────────────────────────────────────┤ │
│  │ Redis 5.0+ (Cache Backend, Sessions)                         │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                                                                    │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │         EXTERNAL SERVICES & INTEGRATIONS                     │ │
│  ├──────────────────────────────────────────────────────────────┤ │
│  │ Google Gemini API (Content Moderation)                       │ │
│  │ Microsoft OAuth 2.0 (SSO Authentication)                    │ │
│  │ Google Cloud (Image Storage, optional)                      │ │
│  │ SMTP (Email Notifications)                                  │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘

                        DEVELOPMENT TOOLS
    ┌────────────────────────────────────────────────────────┐
    │ Git + GitHub | venv | pip | VS Code | Django CLI     │
    │ pytest | Black | Flake8 | Mermaid | PlantUML         │
    └────────────────────────────────────────────────────────┘

                      DEPLOYMENT INFRASTRUCTURE
    ┌────────────────────────────────────────────────────────┐
    │ Nginx | Gunicorn | Docker (optional) | Let's Encrypt  │
    │ Heroku / DigitalOcean / AWS / Azure / GCP             │
    │ GitHub Actions (CI/CD) | Sentry (Error tracking)      │
    └────────────────────────────────────────────────────────┘
```

---

## Performance & Scalability

### Frontend Optimization
✅ **Tailwind CSS (CDN)** — Minimal, utility-first CSS  
✅ **Lucide Icons (SVG)** — Lightweight icon library  
✅ **Image Optimization** — Pillow for responsive images  
✅ **Lazy Loading** — Defer non-critical resources  
✅ **Caching** — Browser cache headers, Django cache middleware  
✅ **Minification** — CSS/JS minified (Tailwind handles this)  

### Backend Optimization
✅ **Database Indexing** — Indexed on status, created_at, user_id  
✅ **Query Optimization** — select_related, prefetch_related  
✅ **Caching Strategy** — Redis for session + API responses  
✅ **Async Tasks** (optional) — Celery for email, heavy processing  
✅ **Rate Limiting** — Throttle API endpoints  
✅ **Pagination** — Load reports in pages (not all at once)  

### Scalability Considerations

**Vertical Scaling** (single server, more resources):
- Increase PostgreSQL server RAM
- Upgrade Gunicorn workers (`workers = 4 * CPU_cores`)
- Enable Redis for caching

**Horizontal Scaling** (multiple servers):
- Load balancer (Nginx, HAProxy)
- Multiple Gunicorn processes
- PostgreSQL replication or managed service (AWS RDS, Heroku Postgres)
- Redis cluster for distributed caching
- Static files on CDN (Cloudflare, AWS CloudFront)

**Database Optimization**:
- Connection pooling (pgBouncer)
- Read replicas for analytics queries
- Partitioning large tables (e.g., Laporan by year)
- Full-text search indexing (PostgreSQL tsvector)

---

## Summary Table

| Layer | Technology | Version | Role |
|-------|-----------|---------|------|
| **Frontend** | HTML5, CSS3, JS | - | User interface |
| | Tailwind CSS | Latest CDN | Styling framework |
| | Lucide Icons | Latest CDN | Icon library |
| | Django Templates | 5.2+ | Server-side rendering |
| **Backend** | Django | ≥ 5.2.0 | Web framework |
| | Python | 3.8+ | Language |
| | django-allauth | ≥ 0.57.0 | Auth + OAuth |
| | google-generativeai | ≥ 0.3.0 | AI Moderation |
| | Gunicorn | ≥ 21.2.0 | WSGI server |
| | Pillow | ≥ 10.0.0 | Image processing |
| **Database** | PostgreSQL | 12+ | Primary DB (prod) |
| | SQLite | Built-in | Dev/test DB |
| | psycopg2 | ≥ 2.9.0 | DB adapter |
| **Caching** | Redis | ≥ 5.0.0 | Cache + sessions |
| **Deployment** | Gunicorn + Nginx | Latest | Production server |
| | WhiteNoise | ≥ 6.5.0 | Static files |
| | Docker | Latest (optional) | Containerization |
| **DevOps** | GitHub Actions | - | CI/CD |
| | Let's Encrypt | - | HTTPS |
| **Monitoring** | Sentry | - | Error tracking (optional) |

---

## Installation & Setup Quick Reference

### Development Environment
```bash
# 1. Create virtual environment
python -m venv myenv

# 2. Activate it
# On Windows:
myenv\Scripts\activate
# On macOS/Linux:
source myenv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file with secrets
cp .env.example .env
# Edit .env: GEMINI_API_KEY, SOCIALACCOUNT credentials

# 5. Run migrations
python manage.py migrate

# 6. Create superuser
python manage.py createsuperuser

# 7. Collect static files (if needed)
python manage.py collectstatic --noinput

# 8. Run development server
python manage.py runserver
```

### Production Deployment (Heroku Example)
```bash
# 1. Create Heroku app
heroku create ruang-dengar

# 2. Add PostgreSQL addon
heroku addons:create heroku-postgresql:standard-0 -a ruang-dengar

# 3. Set environment variables
heroku config:set DEBUG=False -a ruang-dengar
heroku config:set SECRET_KEY=<your-secure-key> -a ruang-dengar
heroku config:set GEMINI_API_KEY=<your-api-key> -a ruang-dengar
# ... etc

# 4. Deploy
git push heroku main

# 5. Run migrations
heroku run python manage.py migrate -a ruang-dengar

# 6. Create superuser
heroku run python manage.py createsuperuser -a ruang-dengar

# 7. View logs
heroku logs --tail -a ruang-dengar
```

---

## Next Steps & Recommendations

1. **Add Testing**: Implement pytest + coverage for automated testing
2. **Improve Security**: Enable HTTPS, add CORS headers, implement rate limiting
3. **Database Optimization**: Add indexing, use select_related/prefetch_related
4. **API Documentation**: Use drf-spectacular for interactive Swagger docs
5. **Monitoring**: Set up Sentry for production error tracking
6. **CI/CD Pipeline**: Use GitHub Actions for automated testing & deployment
7. **Container**: Create Dockerfile for easier deployment & consistency
8. **Load Testing**: Use Locust to simulate concurrent users
9. **API Rate Limiting**: Add throttling to prevent abuse
10. **Search**: Implement Elasticsearch or PostgreSQL full-text search for reports

---

**Document Version**: 1.0  
**Last Updated**: December 15, 2025  
**Maintainer**: Ruang Dengar Development Team
