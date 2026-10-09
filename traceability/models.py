from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=150)
    country = models.CharField(max_length=100)
    contact_email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class RawMaterial(models.Model):
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=100, blank=True)
    unit = models.CharField(max_length=20, default="kg")

    def __str__(self):
        return self.name


class MaterialLot(models.Model):
    lot_code = models.CharField(max_length=50, unique=True)
    raw_material = models.ForeignKey(RawMaterial, on_delete=models.PROTECT, related_name="lots")
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, related_name="lots")
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    received_date = models.DateField()
    expiry_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.lot_code


class Batch(models.Model):
    batch_code = models.CharField(max_length=50, unique=True)
    product_name = models.CharField(max_length=150)
    production_date = models.DateField()
    lots = models.ManyToManyField(MaterialLot, related_name="batches", blank=True)

    def __str__(self):
        return self.batch_code