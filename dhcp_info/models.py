from django.db import models

class Switch(models.Model):
    name = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    vlan = models.PositiveIntegerField()
class Port(models.Model):
    number = models.PositiveIntegerField()
    ip_address = models.GenericIPAddressField()