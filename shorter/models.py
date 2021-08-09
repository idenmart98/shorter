import base64
import hashlib

from django.db import models

from .utils import generate_random_string


class Url(models.Model):
    origin_url = models.URLField(unique=True)
    code_url = models.CharField(max_length=5, unique=True)

    def save(self, *args, **kwargs):
        while True:
            random_str = generate_random_string()
            if not Url.objects.filter(code_url=random_str).exists():
                self.code_url = random_str
                break
            else:
                continue
        super().save(*args, **kwargs)


