from django.contrib import admin

from salons.models import (Client, Master, MasterSpecialization, Order,
                           OrderItem, Salon, SalonServiceItem, Schedule,
                           Service, ServiceType)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["name", "phonenumber"]


class SalonServiceItemInline(admin.TabularInline):
    model = SalonServiceItem


@admin.register(Salon)
class SalonAdmin(admin.ModelAdmin):
    list_display = ["name", "address"]
    inlines = [SalonServiceItemInline, ]


class ScheduleInline(admin.TabularInline):
    model = Schedule


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ["name", "specialization"]  # add display photo
    inlines = [ScheduleInline, ]


class ServiceInline(admin.TabularInline):
    model = Service


@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ["name", ]
    inlines = [ServiceInline, ]


class OrderItemInline(admin.TabularInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "client", "status", "promocode"]
    inlines = [OrderItemInline, ]


@admin.register(MasterSpecialization)
class MasterSpecializationAdmin(admin.ModelAdmin):
    list_display = ["name"]
