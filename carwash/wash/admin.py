from django.contrib import admin
from .models import Service, Client, Washer, Box, CarWashBooking


from django.contrib import admin

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration')
    search_fields = ['name']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'discount')
    search_fields = ['name', 'phone']


@admin.register(Washer)
class WasherAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']


@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    list_display = ('number', 'available_spots')
    search_fields = ['number']


@admin.register(CarWashBooking)
class CarWashBookingAdmin(admin.ModelAdmin):
    list_display = ('client', 'service', 'washer', 'box', 'booking_time', 'total_price')
    search_fields = ['client__name', 'service__name', 'washer__name']
    list_filter = ['service', 'washer']
