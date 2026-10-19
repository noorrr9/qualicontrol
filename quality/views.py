from rest_framework import viewsets
from .models import ControlLimit, Sample, Measurement, CCP, CCPMonitoring, CorrectiveAction
from .serializers import (
    ControlLimitSerializer, SampleSerializer, MeasurementSerializer,
    CCPSerializer, CCPMonitoringSerializer, CorrectiveActionSerializer,
)


class ControlLimitViewSet(viewsets.ModelViewSet):
    queryset = ControlLimit.objects.all()
    serializer_class = ControlLimitSerializer


class SampleViewSet(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer


class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class CCPViewSet(viewsets.ModelViewSet):
    queryset = CCP.objects.all()
    serializer_class = CCPSerializer


class CCPMonitoringViewSet(viewsets.ModelViewSet):
    queryset = CCPMonitoring.objects.all()
    serializer_class = CCPMonitoringSerializer


class CorrectiveActionViewSet(viewsets.ModelViewSet):
    queryset = CorrectiveAction.objects.all()
    serializer_class = CorrectiveActionSerializer 

