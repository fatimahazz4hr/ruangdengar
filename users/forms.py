from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

# Pilihan Program Studi per Fakultas (Telkom University Purwokerto)
PRODI_CHOICES = [
    ('', '-- Pilih Program Studi --'),
    # Fakultas Teknik Elektro
    ('S1 Teknik Telekomunikasi', 'S1 Teknik Telekomunikasi'),
    ('S1 Teknik Elektro', 'S1 Teknik Elektro'),
    ('S1 Teknik Biomedis', 'S1 Teknik Biomedis'),
    ('S1 Teknologi Pangan', 'S1 Teknologi Pangan'),
    # Fakultas Rekayasa Industri
    ('S1 Teknik Industri', 'S1 Teknik Industri'),
    ('S1 Sistem Informasi', 'S1 Sistem Informasi'),
    ('S1 Digital Supply Chain', 'S1 Digital Supply Chain'),
    # Fakultas Informatika
    ('S1 Informatika', 'S1 Informatika'),
    ('S1 Rekayasa Perangkat Lunak', 'S1 Rekayasa Perangkat Lunak'),
    ('S1 Data Sains', 'S1 Data Sains'),
    # Fakultas Ekonomi dan Bisnis
    ('S1 Digital Business', 'S1 Digital Business'),
    # Fakultas Industri Kreatif
    ('S1 Desain Komunikasi Visual', 'S1 Desain Komunikasi Visual'),
    ('S1 Desain Produk', 'S1 Desain Produk'),
    # Fakultas Ilmu Terapan
    ('D3 Teknik Telekomunikasi', 'D3 Teknik Telekomunikasi'),
]

# --- Form Registrasi Pengguna ---
class CustomUserCreationForm(UserCreationForm):
    prodi = forms.ChoiceField(
        choices=PRODI_CHOICES,
        label="Program Studi",
        widget=forms.Select(attrs={'id': 'id_prodi'})
    )
    
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('nama_lengkap', 'nim', 'email', 'fakultas', 'prodi', 'status_pengguna', 'usia', 'no_whatsapp')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nama_lengkap'].label = "Nama Lengkap"
        self.fields['nim'].label = "NIM"
        self.fields['email'].label = "Email Kampus"
        self.fields['fakultas'].label = "Fakultas"
        self.fields['status_pengguna'].label = "Status"
        self.fields['usia'].label = "Usia"
        self.fields['no_whatsapp'].label = "Nomor WhatsApp"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Konfirmasi Password"

        self.fields['email'].widget.attrs.update({'placeholder': 'contoh@student.telkomuniversity.ac.id'})
        self.fields['nim'].widget.attrs.update({'placeholder': 'Contoh: 1301190123'})
        self.fields['fakultas'].widget.attrs.update({'id': 'id_fakultas'})
        self.fields['usia'].widget.attrs.update({'placeholder': 'Contoh: 20', 'min': '17', 'max': '100'})
        self.fields['no_whatsapp'].widget.attrs.update({'placeholder': 'Contoh: 081234567890'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Minimal 8 karakter'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Ulangi password'})

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = CustomUser.Role.USER  # Set role otomatis
        user.is_profile_complete = True  # Manual registration sudah lengkap
        if commit:
            user.save()
        return user

# --- Form Registrasi Admin ---
class AdminUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('nama_lengkap', 'username', 'nidn', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nama_lengkap'].label = "Nama"
        self.fields['username'].label = "Username"
        self.fields['nidn'].label = "NIDN"
        self.fields['email'].label = "Email Kampus"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Konfirmasi Password"

        self.fields['email'].widget.attrs.update({'placeholder': 'contoh.email@gmail.com'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Minimal 8 karakter'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Minimal 8 karakter'})

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = CustomUser.Role.ADMIN  # Set role otomatis
        user.is_staff = True  # Admin harus bisa login ke admin site
        if commit:
            user.save()
        return user

# --- Form Login ---
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label='Email Kampus',
        widget=forms.EmailInput(attrs={'placeholder': 'contoh.email@gmail.com', 'autofocus': True})
    )
    password = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Minimal 8 karakter', 'autocomplete': 'current-password'})
    )
    remember_me = forms.BooleanField(
        label='Remember me',
        required=False,
        initial=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )


# --- Form Edit Profile ---
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            'nama_lengkap', 'email', 'nim', 'nidn', 'prodi', 'fakultas', 
            'status_pengguna', 'usia', 'no_whatsapp', 'profile_picture',
            'nomor_telepon', 'alamat', 'nomor_telepon_kerabat'
        )
        widgets = {
            'nama_lengkap': forms.TextInput(attrs={'readonly': 'readonly', 'style': 'background-color: #f3f4f6; cursor: not-allowed;'}),
            'email': forms.EmailInput(attrs={'readonly': 'readonly', 'style': 'background-color: #f3f4f6; cursor: not-allowed;'}),
            'nim': forms.TextInput(attrs={'readonly': 'readonly', 'style': 'background-color: #f3f4f6; cursor: not-allowed;'}),
            'nidn': forms.TextInput(attrs={'readonly': 'readonly', 'style': 'background-color: #f3f4f6; cursor: not-allowed;'}),
            'alamat': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Masukkan alamat lengkap'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Readonly fields
        self.fields['nama_lengkap'].label = "Nama Lengkap"
        self.fields['nama_lengkap'].help_text = "⚠️ Nama lengkap tidak dapat diubah"
        
        self.fields['email'].label = "Email Kampus"
        self.fields['email'].help_text = "⚠️ Email tidak dapat diubah"
        
        # NIM/NIDN fields (readonly, tapi bisa kosong untuk non-mahasiswa)
        self.fields['nim'].label = "NIM"
        self.fields['nim'].help_text = "⚠️ NIM tidak dapat diubah (khusus Mahasiswa)"
        self.fields['nim'].required = False
        
        self.fields['nidn'].label = "NIDN"
        self.fields['nidn'].help_text = "⚠️ NIDN tidak dapat diubah (khusus Dosen)"
        self.fields['nidn'].required = False
        
        # Editable fields
        self.fields['prodi'].label = "Program Studi"
        self.fields['prodi'].widget.attrs.update({'placeholder': 'Contoh: Teknik Informatika'})
        
        self.fields['fakultas'].label = "Fakultas"
        
        self.fields['status_pengguna'].label = "Status"
        
        self.fields['usia'].label = "Usia"
        self.fields['usia'].widget.attrs.update({'placeholder': 'Contoh: 20', 'type': 'number', 'min': '17', 'max': '100'})
        
        self.fields['no_whatsapp'].label = "Nomor WhatsApp"
        self.fields['no_whatsapp'].widget.attrs.update({'placeholder': '08xxxxxxxxxx'})
        self.fields['no_whatsapp'].help_text = "Nomor WhatsApp untuk komunikasi"
        
        self.fields['profile_picture'].label = "Foto Profile"
        self.fields['profile_picture'].help_text = "Upload foto profile (Max 2MB, format: JPG, PNG)"
        
        self.fields['nomor_telepon'].label = "Nomor Telepon Pribadi"
        self.fields['nomor_telepon'].widget.attrs.update({'placeholder': '08xxxxxxxxxx'})
        
        self.fields['alamat'].label = "Alamat Lengkap"
        
        self.fields['nomor_telepon_kerabat'].label = "Nomor Telepon Kerabat/Orangtua"
        self.fields['nomor_telepon_kerabat'].widget.attrs.update({'placeholder': '08xxxxxxxxxx (Darurat)'})
        self.fields['nomor_telepon_kerabat'].help_text = "Nomor yang dapat dihubungi dalam keadaan darurat"


# --- Form Change Password ---
class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(
        label='Password Lama',
        widget=forms.PasswordInput(attrs={'placeholder': 'Masukkan password lama'})
    )
    new_password1 = forms.CharField(
        label='Password Baru',
        widget=forms.PasswordInput(attrs={'placeholder': 'Minimal 8 karakter'})
    )
    new_password2 = forms.CharField(
        label='Konfirmasi Password Baru',
        widget=forms.PasswordInput(attrs={'placeholder': 'Ulangi password baru'})
    )
    
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)
    
    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.user.check_password(old_password):
            raise forms.ValidationError('Password lama salah')
        return old_password
    
    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')
        
        if new_password1 and new_password2:
            if new_password1 != new_password2:
                raise forms.ValidationError('Password baru tidak cocok')
            if len(new_password1) < 8:
                raise forms.ValidationError('Password minimal 8 karakter')
        
        return cleaned_data
