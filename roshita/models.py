from django.db import models
from django.utils import timezone

# Create your models here.

class Roshita(models.Model):
    title = models.CharField(max_length=150)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title