from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Passenger)
admin.site.register(models.Bus)
admin.site.register(models.Terminal)
admin.site.register(models.Driver)
admin.site.register(models.Trip)
admin.site.register(models.Rating)
admin.site.register(models.Booking)
admin.site.register(models.Bus_Trip)
admin.site.register(models.Bus_Driver)
admin.site.register(models.CurrentTerminal)