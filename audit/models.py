from django.db import models


class AuditLog(models.Model):
    ACTION_CHOICES = [("create", "Create"), ("update", "Update"), ("delete", "Delete")]

    model_name = models.CharField(max_length=100)
    object_id = models.CharField(max_length=50)
    object_repr = models.CharField(max_length=200)
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return f"{self.action} {self.model_name} #{self.object_id}"