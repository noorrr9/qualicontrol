from rest_framework import serializers
from .models import ControlLimit, Sample, Measurement, CCP, CCPMonitoring, CorrectiveAction


class ControlLimitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlLimit
        fields = "__all__"


class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = "__all__"


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = "__all__"


class CCPSerializer(serializers.ModelSerializer):
    class Meta:
        model = CCP
        fields = "__all__"


class CCPMonitoringSerializer(serializers.ModelSerializer):
    class Meta:
        model = CCPMonitoring
        fields = "__all__"


class CorrectiveActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CorrectiveAction
        fields = "__all__"