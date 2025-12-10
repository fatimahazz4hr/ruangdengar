import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Koneksi ke PostgreSQL (ke database 'postgres' default dulu)
try:
    conn = psycopg2.connect(
        dbname='postgres',  # Connect ke database default
        user='postgres',
        password='V!nividivic1',  # Password dari settings.py
        host='localhost',
        port='5432'
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    
    cursor = conn.cursor()
    
    # Cek apakah database sudah ada
    cursor.execute("SELECT 1 FROM pg_database WHERE datname = 'ruangdengar_db'")
    exists = cursor.fetchone()
    
    if exists:
        print("✓ Database 'ruangdengar_db' sudah ada!")
    else:
        # Buat database baru
        cursor.execute("CREATE DATABASE ruangdengar_db")
        print("✓ Database 'ruangdengar_db' berhasil dibuat!")
    
    cursor.close()
    conn.close()
    
except psycopg2.OperationalError as e:
    print(f"❌ Error koneksi ke PostgreSQL:")
    print(f"   {e}")
    print("\nPastikan:")
    print("1. PostgreSQL sudah running")
    print("2. Password di script ini benar (line 9)")
    print("3. User 'postgres' ada dan bisa login")
except Exception as e:
    print(f"❌ Error: {e}")
