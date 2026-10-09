from rest_framework import generics
from .models import Supplier
from .serializers import SupplierSerializer


class SupplierListCreate(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
