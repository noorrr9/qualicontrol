from django.contrib import admin
from .models import ControlLimit, Sample, Measurement, CCP, CCPMonitoring, CorrectiveAction


@admin.register(ControlLimit)
class ControlLimitAdmin(admin.ModelAdmin):
    list_display = ("parameter", "unit", "min_value", "max_value")
    search_fields = ("parameter",)


@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    list_display = ("sample_code", "batch", "sampled_at", "sampled_by")
    search_fields = ("sample_code",)


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ("sample", "control_limit", "value", "is_conform", "measured_at")
    list_filter = ("is_conform", "control_limit")
    readonly_fields = ("is_conform", "measured_at")


@admin.register(CCP)
class CCPAdmin(admin.ModelAdmin):
    list_display = ("name", "hazard", "critical_limit")


@admin.register(CCPMonitoring)
class CCPMonitoringAdmin(admin.ModelAdmin):
    list_display = ("ccp", "batch", "value", "is_within_limit", "monitored_at")
    list_filter = ("is_within_limit", "ccp")
    readonly_fields = ("is_within_limit", "monitored_at")


@admin.register(CorrectiveAction)
class CorrectiveActionAdmin(admin.ModelAdmin):
    list_display = ("monitoring", "action_date", "status")
    list_filter = ("status",)
