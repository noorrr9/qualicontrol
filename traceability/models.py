from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=150)
    country = models.CharField(max_length=100)
    contact_email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name