from rest_framework.routers import DefaultRouter
from .views import (
    ControlLimitViewSet, SampleViewSet, MeasurementViewSet,
    CCPViewSet, CCPMonitoringViewSet, CorrectiveActionViewSet,
)

router = DefaultRouter()
router.register("control-limits", ControlLimitViewSet)
router.register("samples", SampleViewSet)
router.register("measurements", MeasurementViewSet)
router.register("ccps", CCPViewSet)
router.register("ccp-monitorings", CCPMonitoringViewSet)
router.register("corrective-actions", CorrectiveActionViewSet)

urlpatterns = router.urls