from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings
from django.core.exceptions import ValidationError


class EmailDomainAdapter(DefaultAccountAdapter):
    """
    Custom adapter untuk restrict registrasi hanya ke email domain tertentu
    (email Telkom University: @telkomuniversity.ac.id atau @student.telkomuniversity.ac.id)
    """
    
    def clean_email(self, email):
        """
        Validasi email domain saat registrasi
        """
        email = super().clean_email(email)
        
        # Cek apakah email domain diizinkan
        allowed_domains = getattr(settings, 'ALLOWED_EMAIL_DOMAINS', [])
        email_domain = email.split('@')[1] if '@' in email else ''
        
        if email_domain not in allowed_domains:
            raise ValidationError(
                f"Registrasi hanya diperbolehkan untuk email Telkom University "
                f"(@telkomuniversity.ac.id atau @student.telkomuniversity.ac.id)"
            )
        
        return email
