from django.contrib import admin
from .models import CustomUser, Laporan, Evidence, Progress, Booking, Counselor


@admin.register(Counselor)
class CounselorAdmin(admin.ModelAdmin):
	list_display = ('name', 'title')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
	list_display = ('user', 'tanggal', 'waktu', 'konselor', 'status')
	list_filter = ('status', 'tanggal')
	search_fields = ('user__nama_lengkap', 'konselor', 'nama', 'topik')

@admin.register(Laporan)
class LaporanAdmin(admin.ModelAdmin):
	list_display = ('kode', 'jenis', 'status', 'created_at')
