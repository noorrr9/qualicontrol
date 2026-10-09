from rest_framework import viewsets
from .models import Supplier, RawMaterial, MaterialLot, Batch
from .serializers import (
    SupplierSerializer,
    RawMaterialSerializer,
    MaterialLotSerializer,
    BatchSerializer,
)


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class RawMaterialViewSet(viewsets.ModelViewSet):
    queryset = RawMaterial.objects.all()
    serializer_class = RawMaterialSerializer


class MaterialLotViewSet(viewsets.ModelViewSet):
    queryset = MaterialLot.objects.all()
    serializer_class = MaterialLotSerializer


class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
