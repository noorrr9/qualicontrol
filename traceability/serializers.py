from rest_framework import serializers
from .models import Supplier, RawMaterial, MaterialLot, Batch


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"


class RawMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawMaterial
        fields = "__all__"


class MaterialLotSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialLot
        fields = "__all__"


class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = "__all__"