# 🚀 Deployment Guide - Ruang Dengar

Panduan lengkap untuk deploy **Ruang Dengar** ke production server.

---

## 📋 Prerequisites

- Server Linux (Ubuntu 20.04+ recommended)
- Python 3.10+
- PostgreSQL 12+
- Nginx (web server)
- Domain dengan SSL certificate
- Min. 2GB RAM (untuk AI model)

---

## 🔧 Step 1: Server Setup

### 1.1 Update System
```bash
sudo apt update && sudo apt upgrade -y
```

### 1.2 Install Dependencies
```bash
# Python & pip
sudo apt install python3-pip python3-venv python3-dev -y

# PostgreSQL
sudo apt install postgresql postgresql-contrib libpq-dev -y

# Nginx
sudo apt install nginx -y

# Redis (optional, for caching)
sudo apt install redis-server -y

# System tools
sudo apt install git curl build-essential -y
```

### 1.3 Create Application User
```bash
sudo adduser ruangdengar
sudo usermod -aG sudo ruangdengar
su - ruangdengar
```

---

## 📦 Step 2: Application Setup

### 2.1 Clone Repository
```bash
cd /home/ruangdengar
git clone <your-repository-url> ruangdengar
cd ruangdengar
```

### 2.2 Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2.3 Install Python Packages
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 2.4 Setup Environment Variables
```bash
# Copy template
cp .env.example .env

# Edit dengan nano atau vim
nano .env
```

**Isi .env dengan nilai production:**
```env
DJANGO_ENV=production
SECRET_KEY=<generate-dengan-command-dibawah>
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

DB_NAME=ruangdengar_db
DB_USER=ruangdengar_user
DB_PASSWORD=<strong-password>
DB_HOST=localhost
DB_PORT=5432

STATIC_ROOT=/var/www/ruangdengar/static
MEDIA_ROOT=/var/www/ruangdengar/media
```

**Generate SECRET_KEY:**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

## 🗄️ Step 3: Database Setup

### 3.1 Create PostgreSQL Database
```bash
sudo -u postgres psql
```

```sql
-- Di PostgreSQL prompt:
CREATE DATABASE ruangdengar_db;
CREATE USER ruangdengar_user WITH PASSWORD 'your-strong-password';
ALTER ROLE ruangdengar_user SET client_encoding TO 'utf8';
ALTER ROLE ruangdengar_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE ruangdengar_user SET timezone TO 'Asia/Jakarta';
GRANT ALL PRIVILEGES ON DATABASE ruangdengar_db TO ruangdengar_user;
\q
```

### 3.2 Run Migrations
```bash
# Gunakan settings production
python manage.py migrate --settings=ruangdengar.settings_production

# Create superuser
python manage.py createsuperuser --settings=ruangdengar.settings_production
```

### 3.3 Collect Static Files
```bash
# Create static directory
sudo mkdir -p /var/www/ruangdengar/static
sudo mkdir -p /var/www/ruangdengar/media
sudo chown -R ruangdengar:ruangdengar /var/www/ruangdengar

# Collect static files
python manage.py collectstatic --settings=ruangdengar.settings_production --noinput
```

---

## 🔥 Step 4: Gunicorn Setup

### 4.1 Test Gunicorn
```bash
gunicorn --bind 0.0.0.0:8000 ruangdengar.wsgi:application --settings=ruangdengar.settings_production
```

### 4.2 Create Gunicorn Service
```bash
sudo nano /etc/systemd/system/ruangdengar.service
```

**Paste configuration:**
```ini
[Unit]
Description=Ruang Dengar Gunicorn Daemon
After=network.target

[Service]
User=ruangdengar
Group=www-data
WorkingDirectory=/home/ruangdengar/ruangdengar
Environment="DJANGO_SETTINGS_MODULE=ruangdengar.settings_production"
ExecStart=/home/ruangdengar/ruangdengar/venv/bin/gunicorn \
          --workers 3 \
          --bind unix:/home/ruangdengar/ruangdengar/gunicorn.sock \
          --timeout 120 \
          --log-level info \
          --access-logfile /home/ruangdengar/ruangdengar/logs/gunicorn-access.log \
          --error-logfile /home/ruangdengar/ruangdengar/logs/gunicorn-error.log \
          ruangdengar.wsgi:application

[Install]
WantedBy=multi-user.target
```

### 4.3 Start Gunicorn Service
```bash
# Create logs directory
mkdir -p /home/ruangdengar/ruangdengar/logs

# Reload systemd
sudo systemctl daemon-reload

# Start service
sudo systemctl start ruangdengar

# Enable on boot
sudo systemctl enable ruangdengar

# Check status
sudo systemctl status ruangdengar
```

---

## 🌐 Step 5: Nginx Configuration

### 5.1 Create Nginx Config
```bash
sudo nano /etc/nginx/sites-available/ruangdengar
```

**Paste configuration:**
```nginx
upstream ruangdengar {
    server unix:/home/ruangdengar/ruangdengar/gunicorn.sock fail_timeout=0;
}

server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

    client_max_body_size 10M;

    # Logs
    access_log /var/log/nginx/ruangdengar-access.log;
    error_log /var/log/nginx/ruangdengar-error.log;

    # Static files
    location /static/ {
        alias /var/www/ruangdengar/static/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    # Media files
    location /media/ {
        alias /var/www/ruangdengar/media/;
        expires 7d;
    }

    # Proxy to Gunicorn
    location / {
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_pass http://ruangdengar;
    }
}
```

### 5.2 Enable Site
```bash
# Create symlink
sudo ln -s /etc/nginx/sites-available/ruangdengar /etc/nginx/sites-enabled/

# Test configuration
sudo nginx -t

# Restart Nginx
sudo systemctl restart nginx
```

---

## 🔒 Step 6: SSL Certificate (HTTPS)

### 6.1 Install Certbot
```bash
sudo apt install certbot python3-certbot-nginx -y
```

### 6.2 Obtain Certificate
```bash
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

Follow prompts:
- Enter email address
- Agree to Terms of Service
- Choose redirect HTTP to HTTPS (option 2)

### 6.3 Test Auto-Renewal
```bash
sudo certbot renew --dry-run
```

---

## 🤖 Step 7: AI Model Setup

### 7.1 Download Model (First Run)
```bash
# Model akan download otomatis ~418 MB
python -c "from users.ai_moderation import moderate_laporan; moderate_laporan('test')"
```

### 7.2 Verify Model
```bash
ls -lh ~/.cache/torch/hub/checkpoints/
# Should see: toxic_original-c1212f89.ckpt (~418 MB)
```

---

## 📊 Step 8: Monitoring & Maintenance

### 8.1 Check Logs
```bash
# Django logs
tail -f /home/ruangdengar/ruangdengar/logs/django.log

# Gunicorn logs
tail -f /home/ruangdengar/ruangdengar/logs/gunicorn-error.log

# Nginx logs
sudo tail -f /var/log/nginx/ruangdengar-error.log
```

### 8.2 Service Management
```bash
# Restart services
sudo systemctl restart ruangdengar
sudo systemctl restart nginx

# Check status
sudo systemctl status ruangdengar
sudo systemctl status nginx
```

### 8.3 Database Backup
```bash
# Create backup script
nano ~/backup_db.sh
```

```bash
#!/bin/bash
BACKUP_DIR="/home/ruangdengar/backups"
DATE=$(date +%Y%m%d_%H%M%S)

mkdir -p $BACKUP_DIR

pg_dump -U ruangdengar_user ruangdengar_db > $BACKUP_DIR/ruangdengar_$DATE.sql

# Keep only last 7 days
find $BACKUP_DIR -name "ruangdengar_*.sql" -mtime +7 -delete

echo "Backup completed: ruangdengar_$DATE.sql"
```

```bash
# Make executable
chmod +x ~/backup_db.sh

# Add to crontab (daily at 2 AM)
crontab -e
```

Add line:
```
0 2 * * * /home/ruangdengar/backup_db.sh
```

---

## 🔄 Step 9: Updates & Deployment

### 9.1 Update Application
```bash
cd /home/ruangdengar/ruangdengar

# Pull latest code
git pull origin main

# Activate venv
source venv/bin/activate

# Install new dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate --settings=ruangdengar.settings_production

# Collect static files
python manage.py collectstatic --settings=ruangdengar.settings_production --noinput

# Restart Gunicorn
sudo systemctl restart ruangdengar
```

### 9.2 Zero-Downtime Deployment (Optional)
```bash
# Install supervisor for process management
sudo apt install supervisor -y

# Configure multiple Gunicorn workers
# Edit /etc/supervisor/conf.d/ruangdengar.conf
```

---

## 🛡️ Step 10: Security Hardening

### 10.1 Firewall Setup
```bash
# Allow SSH, HTTP, HTTPS
sudo ufw allow OpenSSH
sudo ufw allow 'Nginx Full'
sudo ufw enable
sudo ufw status
```

### 10.2 Fail2Ban (Prevent Brute Force)
```bash
sudo apt install fail2ban -y
sudo systemctl enable fail2ban
sudo systemctl start fail2ban
```

### 10.3 PostgreSQL Security
```bash
sudo nano /etc/postgresql/12/main/pg_hba.conf
```

Ensure only local connections:
```
local   all             all                                     peer
host    all             all             127.0.0.1/32            md5
```

```bash
sudo systemctl restart postgresql
```

---

## ✅ Step 11: Health Check

### 11.1 Check All Services
```bash
# PostgreSQL
sudo systemctl status postgresql

# Redis
sudo systemctl status redis

# Gunicorn
sudo systemctl status ruangdengar

# Nginx
sudo systemctl status nginx
```

### 11.2 Test Website
```bash
# HTTP to HTTPS redirect
curl -I http://yourdomain.com

# HTTPS working
curl -I https://yourdomain.com

# Static files
curl -I https://yourdomain.com/static/css/lihat_jadwal_style.css

# Admin panel
curl -I https://yourdomain.com/admin/
```

### 11.3 Verify AI Moderation
```bash
source venv/bin/activate
python manage.py shell --settings=ruangdengar.settings_production
```

```python
from users.ai_moderation import moderate_laporan
result = moderate_laporan("Test laporan")
print(result)
# Should return AI analysis result
```

---

## 📈 Performance Optimization

### Database Indexing
Already optimized in migrations, but verify:
```sql
-- Check indexes
SELECT * FROM pg_indexes WHERE tablename = 'users_laporan';
```

### Nginx Caching
Add to Nginx config:
```nginx
# Gzip compression
gzip on;
gzip_vary on;
gzip_types text/plain text/css application/json application/javascript text/xml application/xml;
```

### Redis Cache
Ensure Redis is running:
```bash
redis-cli ping
# Should return: PONG
```

---

## 🆘 Troubleshooting

### Gunicorn Won't Start
```bash
# Check logs
sudo journalctl -u ruangdengar -n 50

# Test manually
cd /home/ruangdengar/ruangdengar
source venv/bin/activate
gunicorn --bind 0.0.0.0:8000 ruangdengar.wsgi:application
```

### Static Files Not Loading
```bash
# Verify permissions
ls -la /var/www/ruangdengar/static/

# Re-collect
python manage.py collectstatic --settings=ruangdengar.settings_production --clear --noinput
```

### Database Connection Error
```bash
# Test connection
psql -U ruangdengar_user -d ruangdengar_db -h localhost

# Check PostgreSQL status
sudo systemctl status postgresql
```

### AI Model Error
```bash
# Check cache
ls -lh ~/.cache/torch/hub/checkpoints/

# Re-download if corrupted
rm -rf ~/.cache/torch/hub/checkpoints/
python -c "from users.ai_moderation import moderate_laporan; moderate_laporan('test')"
```

---

## 📞 Support Checklist

Before asking for help, check:
- [ ] All services running (`systemctl status`)
- [ ] Logs checked (`tail -f logs/*.log`)
- [ ] .env file configured correctly
- [ ] Database migrations applied
- [ ] Static files collected
- [ ] Firewall allows traffic
- [ ] SSL certificate valid
- [ ] Domain DNS pointing to server IP

---

## 🎯 Quick Commands Reference

```bash
# Restart all
sudo systemctl restart ruangdengar nginx postgresql redis

# View logs
tail -f ~/ruangdengar/logs/django.log
sudo tail -f /var/log/nginx/ruangdengar-error.log

# Database backup
pg_dump -U ruangdengar_user ruangdengar_db > backup.sql

# Restore database
psql -U ruangdengar_user ruangdengar_db < backup.sql

# Check disk space
df -h

# Check memory
free -h

# Check processes
ps aux | grep gunicorn
```

---

## 🚀 Post-Deployment

✅ Update DNS records  
✅ Test all features (login, laporan, konten, booking)  
✅ Verify AI moderation working  
✅ Check email notifications (if configured)  
✅ Setup monitoring (optional: UptimeRobot, Sentry)  
✅ Document admin credentials securely  
✅ Schedule regular backups  

---

**Deployment Complete! 🎉**

Your Ruang Dengar application is now live and secure in production.

For issues or questions, check logs first, then troubleshooting section.
