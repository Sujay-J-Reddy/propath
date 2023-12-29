# shared/models.py

from django.db import models

class Notification(models.Model):
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message  # This is just for representation in Django admin
