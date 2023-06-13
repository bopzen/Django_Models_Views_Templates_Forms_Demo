from django.contrib import admin

from models_demo.barbershops.models import Barbershop, Address, Barber


@admin.register(Barbershop)
class BarbershopsAdmin(admin.ModelAdmin):
    pass


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(Barber)
class BarberAdmin(admin.ModelAdmin):
    pass

