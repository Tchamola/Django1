from django.db import models

# Création des models pour l'application pages

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_treated = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.email})"
