from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *
from .filters import OrganizationFilter

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)  
    filterset_class = OrganizationFilter  
    search_fields = ['name', 'street', 'house_number']
    permission_classes = [AllowAny]

class EntranceViewSet(viewsets.ModelViewSet):
    queryset = Entrance.objects.all()
    serializer_class = EntranceSerializer
    permission_classes = [AllowAny]