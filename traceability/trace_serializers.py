from rest_framework import serializers
from .models import Supplier, RawMaterial, MaterialLot, Batch
from quality.models import Sample, Measurement, CCPMonitoring, CorrectiveAction


class TraceSupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ["id", "name", "country"]


class TraceRawMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawMaterial
        fields = ["id", "name", "category", "unit"]


class TraceLotSerializer(serializers.ModelSerializer):
    raw_material = TraceRawMaterialSerializer(read_only=True)
    supplier = TraceSupplierSerializer(read_only=True)

    class Meta:
        model = MaterialLot
        fields = ["id", "lot_code", "quantity", "received_date", "expiry_date",
                  "raw_material", "supplier"]


class TraceMeasurementSerializer(serializers.ModelSerializer):
    parameter = serializers.CharField(source="control_limit.parameter")
    unit = serializers.CharField(source="control_limit.unit")
    min_value = serializers.DecimalField(source="control_limit.min_value",
                                         max_digits=10, decimal_places=3)
    max_value = serializers.DecimalField(source="control_limit.max_value",
                                         max_digits=10, decimal_places=3)

    class Meta:
        model = Measurement
        fields = ["id", "parameter", "unit", "value", "min_value", "max_value",
                  "is_conform", "measured_at"]


class TraceSampleSerializer(serializers.ModelSerializer):
    measurements = TraceMeasurementSerializer(many=True, read_only=True)

    class Meta:
        model = Sample
        fields = ["id", "sample_code", "sampled_at", "sampled_by", "measurements"]


class TraceActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CorrectiveAction
        fields = ["id", "description", "action_date", "status"]


class TraceCCPMonitoringSerializer(serializers.ModelSerializer):
    ccp = serializers.CharField(source="ccp.name")
    actions = TraceActionSerializer(many=True, read_only=True)

    class Meta:
        model = CCPMonitoring
        fields = ["id", "ccp", "value", "is_within_limit", "monitored_at", "actions"]


class BatchTraceSerializer(serializers.ModelSerializer):
    lots = TraceLotSerializer(many=True, read_only=True)
    samples = TraceSampleSerializer(many=True, read_only=True)
    ccp_monitorings = TraceCCPMonitoringSerializer(many=True, read_only=True)
    summary = serializers.SerializerMethodField()

    class Meta:
        model = Batch
        fields = ["id", "batch_code", "product_name", "production_date",
                  "summary", "lots", "samples", "ccp_monitorings"]

    def get_summary(self, batch):
        measurements = [m for s in batch.samples.all() for m in s.measurements.all()]
        monitorings = list(batch.ccp_monitorings.all())
        open_actions = sum(
            1 for mon in monitorings for a in mon.actions.all() if a.status == "open"
        )
        non_conform = sum(1 for m in measurements if not m.is_conform)
        ccp_deviations = sum(1 for mon in monitorings if not mon.is_within_limit)
        return {
            "lots_used": batch.lots.count(),
            "measurements": len(measurements),
            "non_conform_measurements": non_conform,
            "ccp_deviations": ccp_deviations,
            "open_corrective_actions": open_actions,
            "overall_conform": non_conform == 0 and ccp_deviations == 0,
        }


class RecallBatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = ["id", "batch_code", "product_name", "production_date"]


class LotRecallSerializer(serializers.ModelSerializer):
    raw_material = TraceRawMaterialSerializer(read_only=True)
    supplier = TraceSupplierSerializer(read_only=True)
    batches = RecallBatchSerializer(many=True, read_only=True)

    class Meta:
        model = MaterialLot
        fields = ["id", "lot_code", "raw_material", "supplier", "batches"]