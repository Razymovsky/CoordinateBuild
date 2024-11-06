from django.contrib import admin
from .models import Organization, Entrance
from .filters import OrganizationFilter

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'street', 'house_number')  
    list_filter = ('name', 'street', 'house_number')  

class EntranceInline(admin.TabularInline):
    model = Entrance
    extra = 1  


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Entrance)