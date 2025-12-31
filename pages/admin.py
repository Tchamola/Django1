from django.contrib import admin
from .models import ContactMessage

# Personnaliser l'interface d'administration 
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at", "is_treated")
    list_filter = ("is_treated", "created_at")
    search_fields = ("name", "email", "message")
        

# Enregistrer vos models ici
admin.site.register(ContactMessage, ContactMessageAdmin) 
