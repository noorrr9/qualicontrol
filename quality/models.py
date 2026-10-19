from django.db import models


class ControlLimit(models.Model):
    parameter = models.CharField(max_length=100)  # e.g. pH, moisture, temperature
    unit = models.CharField(max_length=20, blank=True)
    min_value = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    max_value = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)

    def __str__(self):
        return self.parameter


class Sample(models.Model):
    sample_code = models.CharField(max_length=50, unique=True)
    batch = models.ForeignKey("traceability.Batch", on_delete=models.PROTECT, related_name="samples")
    sampled_at = models.DateTimeField()
    sampled_by = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.sample_code


class Measurement(models.Model):
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE, related_name="measurements")
    control_limit = models.ForeignKey(ControlLimit, on_delete=models.PROTECT, related_name="measurements")
    value = models.DecimalField(max_digits=10, decimal_places=3)
    measured_at = models.DateTimeField(auto_now_add=True)
    is_conform = models.BooleanField(default=True, editable=False)

    def save(self, *args, **kwargs):
        limit = self.control_limit
        too_low = limit.min_value is not None and self.value < limit.min_value
        too_high = limit.max_value is not None and self.value > limit.max_value
        self.is_conform = not (too_low or too_high)
        super().save(*args, **kwargs)


class CCP(models.Model):
    name = models.CharField(max_length=150)  # e.g. Pasteurisation
    hazard = models.CharField(max_length=200)
    critical_limit = models.ForeignKey(ControlLimit, on_delete=models.PROTECT, related_name="ccps")

    def __str__(self):
        return self.name


class CCPMonitoring(models.Model):
    ccp = models.ForeignKey(CCP, on_delete=models.PROTECT, related_name="monitorings")
    batch = models.ForeignKey("traceability.Batch", on_delete=models.PROTECT, related_name="ccp_monitorings")
    value = models.DecimalField(max_digits=10, decimal_places=3)
    monitored_at = models.DateTimeField(auto_now_add=True)
    is_within_limit = models.BooleanField(default=True, editable=False)

    def save(self, *args, **kwargs):
        limit = self.ccp.critical_limit
        too_low = limit.min_value is not None and self.value < limit.min_value
        too_high = limit.max_value is not None and self.value > limit.max_value
        self.is_within_limit = not (too_low or too_high)
        super().save(*args, **kwargs)


class CorrectiveAction(models.Model):
    STATUS_CHOICES = [("open", "Open"), ("closed", "Closed")]

    monitoring = models.ForeignKey(CCPMonitoring, on_delete=models.CASCADE, related_name="actions")
    description = models.TextField()
    action_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="open") 
