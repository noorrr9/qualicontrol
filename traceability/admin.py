from django.contrib import admin
from .models import Supplier, RawMaterial, MaterialLot, Batch


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "contact_email", "created_at")
    search_fields = ("name", "country")


@admin.register(RawMaterial)
class RawMaterialAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "unit")
    search_fields = ("name",)


@admin.register(MaterialLot)
class MaterialLotAdmin(admin.ModelAdmin):
    list_display = ("lot_code", "raw_material", "supplier", "quantity", "received_date", "expiry_date")
    list_filter = ("supplier", "raw_material")
    search_fields = ("lot_code",)


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ("batch_code", "product_name", "production_date")
    search_fields = ("batch_code", "product_name")
    filter_horizontal = ("lots",)
