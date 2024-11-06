'''from django.contrib import admin
from buildings.models import Organization, Entrance

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'street', 'house_number')

@admin.register(Entrance)
class EntranceAdmin(admin.ModelAdmin):
    list_display = ('organization', 'latitude', 'longitude')
# Register your models here.
'''
'''
from django.contrib import admin
from .models import Organization, Entrance

class EntranceInline(admin.TabularInline):
    model = Entrance
    extra = 1  # количество дополнительных форм входа для каждой организации

class OrganizationAdmin(admin.ModelAdmin):
    inlines = [EntranceInline]  # Вставляем входы в редактирование организации

admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Entrance)


'''



from django.contrib import admin
from .models import Organization, Entrance
from .filters import OrganizationFilter

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'street', 'house_number')  # Отображаем нужные поля
    list_filter = ('name', 'street', 'house_number')  # Фильтрация по полям

class EntranceInline(admin.TabularInline):
    model = Entrance
    extra = 1  # количество дополнительных форм входа для каждой организации


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Entrance)