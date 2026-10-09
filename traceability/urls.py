from rest_framework.routers import DefaultRouter
from .views import (
    SupplierViewSet,
    RawMaterialViewSet,
    MaterialLotViewSet,
    BatchViewSet,
)

router = DefaultRouter()
router.register("suppliers", SupplierViewSet)
router.register("raw-materials", RawMaterialViewSet)
router.register("lots", MaterialLotViewSet)
router.register("batches", BatchViewSet)

urlpatterns = router.urls