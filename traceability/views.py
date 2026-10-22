from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Supplier, RawMaterial, MaterialLot, Batch
from .serializers import (
    SupplierSerializer,
    RawMaterialSerializer,
    MaterialLotSerializer,
    BatchSerializer,
)
from .trace_serializers import BatchTraceSerializer, LotRecallSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class RawMaterialViewSet(viewsets.ModelViewSet):
    queryset = RawMaterial.objects.all()
    serializer_class = RawMaterialSerializer

class MaterialLotViewSet(viewsets.ModelViewSet):
    queryset = MaterialLot.objects.all()
    serializer_class = MaterialLotSerializer

    @action(detail=True, methods=["get"])
    def trace(self, request, pk=None):
        lot = get_object_or_404(
            MaterialLot.objects.select_related("raw_material", "supplier")
            .prefetch_related("batches"),
            pk=pk,
        )
        return Response(LotRecallSerializer(lot).data)


class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer

    @action(detail=True, methods=["get"])
    def trace(self, request, pk=None):
        batch = get_object_or_404(
            Batch.objects.prefetch_related(
                "lots__supplier",
                "lots__raw_material",
                "samples__measurements__control_limit",
                "ccp_monitorings__ccp",
                "ccp_monitorings__actions",
            ),
            pk=pk,
        )
        return Response(BatchTraceSerializer(batch).data)
