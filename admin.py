from django.contrib import admin
from .models import Category, Event, Booking

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "event_date", "event_time", "venue", "capacity", "status")
    list_filter = ("status", "category")
    search_fields = ("title", "venue")

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("user", "event", "status", "booked_at")
    list_filter = ("status",)
    search_fields = ("user__username", "event__title")
