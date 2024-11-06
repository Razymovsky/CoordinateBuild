import django_filters
from .models import Organization

class OrganizationFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Name')  
    street = django_filters.CharFilter(lookup_expr='icontains', label='Street')  
    house_number = django_filters.CharFilter(lookup_expr='icontains', label='House Number') 

    class Meta:
        model = Organization
        fields = ['name', 'street', 'house_number'] 