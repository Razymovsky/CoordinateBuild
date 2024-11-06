from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=255)  # Название организации
    street = models.CharField(max_length=255)  # Улица
    house_number = models.CharField(max_length=10)  # Номер дома

    def __str__(self):
        return self.name


class Entrance(models.Model):
    # Связь с организацией (один ко многим)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='entrances')
    
    # Координаты входа
    latitude = models.DecimalField(max_digits=9, decimal_places=6)  # Широта
    longitude = models.DecimalField(max_digits=9, decimal_places=6)  # Долгота

    def __str__(self):
        return f"Entrance for {self.organization.name} at {self.latitude}, {self.longitude}"