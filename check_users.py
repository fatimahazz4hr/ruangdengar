import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ruangdengar.settings')
django.setup()

from users.models import CustomUser

print("=" * 60)
print("CEK DATA USER DI DATABASE")
print("=" * 60)

users = CustomUser.objects.all()

if not users.exists():
    print("\n❌ Tidak ada user di database!")
else:
    print(f"\n✓ Total user: {users.count()}\n")
    
    for user in users:
        print(f"Email: {user.email}")
        print(f"Username: {user.username}")
        print(f"Nama: {user.nama_lengkap}")
        print(f"Role: {user.role} ({'ADMIN' if user.role == CustomUser.Role.ADMIN else 'USER'})")
        print(f"NIM: {user.nim if user.nim else '-'}")
        print(f"NIDN: {user.nidn if user.nidn else '-'}")
        print(f"Prodi: {user.prodi if user.prodi else '-'}")
        print(f"Active: {user.is_active}")
        print("-" * 60)

print("\nRole Choices:")
print(f"ADMIN = '{CustomUser.Role.ADMIN}'")
print(f"USER = '{CustomUser.Role.USER}'")
