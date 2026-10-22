from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import AuditLog

TRACKED_APPS = {"traceability", "quality"}


@receiver(post_save)
def log_save(sender, instance, created, **kwargs):
    if sender._meta.app_label not in TRACKED_APPS:
        return
    AuditLog.objects.create(
        model_name=sender.__name__,
        object_id=str(instance.pk),
        object_repr=str(instance)[:200],
        action="create" if created else "update",
    )


@receiver(post_delete)
def log_delete(sender, instance, **kwargs):
    if sender._meta.app_label not in TRACKED_APPS:
        return
    AuditLog.objects.create(
        model_name=sender.__name__,
        object_id=str(instance.pk),
        object_repr=str(instance)[:200],
        action="delete",
    )
    