"""
Script untuk migrate data dari SQLite ke PostgreSQL
Jalankan dengan: python migrate_to_postgres.py
"""
import os
import django
import sys

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ruangdengar.settings')
django.setup()

from django.core.management import call_command
from django.conf import settings

def migrate_data():
    print("=" * 60)
    print("MIGRATE DATA DARI SQLite KE PostgreSQL")
    print("=" * 60)
    
    # Step 1: Pastikan masih pakai SQLite
    current_engine = settings.DATABASES['default']['ENGINE']
    if 'postgresql' in current_engine:
        print("\n❌ ERROR: Database sudah menggunakan PostgreSQL!")
        print("   Ubah kembali ke SQLite di settings.py untuk export data.")
        return
    
    print("\n✅ Database saat ini: SQLite")
    print("\n📦 Step 1: Export data dari SQLite...")
    
    # Export semua data kecuali contenttypes dan sessions
    try:
        with open('data_backup.json', 'w', encoding='utf-8') as f:
            call_command(
                'dumpdata',
                '--exclude=contenttypes',
                '--exclude=auth.permission',
                '--exclude=sessions.session',
                '--natural-foreign',
                '--natural-primary',
                '--indent=2',
                stdout=f
            )
        print("   ✅ Data berhasil di-export ke data_backup.json")
    except Exception as e:
        print(f"   ❌ ERROR saat export: {e}")
        return
    
    print("\n" + "=" * 60)
    print("LANGKAH SELANJUTNYA:")
    print("=" * 60)
    print("\n1. Edit ruangdengar/settings.py:")
    print("   - Comment SQLite config")
    print("   - Uncomment PostgreSQL config")
    print("   - Ganti PASSWORD dengan password PostgreSQL kamu")
    
    print("\n2. Buat database PostgreSQL:")
    print("   - Buka pgAdmin atau psql")
    print("   - Jalankan: CREATE DATABASE ruangdengar_db;")
    
    print("\n3. Install psycopg2:")
    print("   pip install psycopg2-binary")
    
    print("\n4. Migrate schema ke PostgreSQL:")
    print("   python manage.py migrate")
    
    print("\n5. Import data ke PostgreSQL:")
    print("   python manage.py loaddata data_backup.json")
    
    print("\n6. Jalankan server:")
    print("   python manage.py runserver")
    
    print("\n" + "=" * 60)
    print("✅ Script selesai! File backup: data_backup.json")
    print("=" * 60)

if __name__ == '__main__':
    migrate_data()
