from django.urls import path
from .views import SupplierListCreate

urlpatterns = [
    path("suppliers/", SupplierListCreate.as_view(), name="supplier-list"),
]