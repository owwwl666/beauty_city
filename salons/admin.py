from django.contrib import admin
from salons.models import (Client, Master, Order, OrderItem, Salon,
                           SalonServiceItem, Schedule, Service)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["name", "phonenumber"]


@admin.register(Salon)
class SalonAdmin(admin.ModelAdmin):
    list_display = ["name", "address"]


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ["name", ]  # add display photo


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ["master", "date_time", "client"]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]


# make tabular inline inside of Salon (all salons)
@admin.register(SalonServiceItem)
class SalonServiceItemAdmin(admin.ModelAdmin):
    list_display = ["salon", "service", "master"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["client", "status", "promocode"]


# make tabular inline inside of Order
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["order", "salon_service"]
