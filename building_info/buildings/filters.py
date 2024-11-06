import django_filters
from .models import Organization

class OrganizationFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Name')  # Поиск по имени, частичное совпадение
    street = django_filters.CharFilter(lookup_expr='icontains', label='Street')  # Поиск по улице, частичное совпадение
    house_number = django_filters.CharFilter(lookup_expr='icontains', label='House Number')  # Поиск по номеру дома

    class Meta:
        model = Organization
        fields = ['name', 'street', 'house_number']  # Указываем, по каким полям можно фильтровать