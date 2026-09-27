from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Event(models.Model):
    STATUS_CHOICES = [
        ("upcoming", "Upcoming"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="events")
    event_date = models.DateField()
    event_time = models.TimeField()
    venue = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField(default=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="upcoming")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["event_date", "event_time"]

    def __str__(self):
        return self.title

    @property
    def seats_booked(self):
        return self.bookings.filter(status__in=["pending", "approved"]).count()

    @property
    def seats_left(self):
        return max(self.capacity - self.seats_booked, 0)

    @property
    def is_past(self):
        return self.event_date < timezone.localdate()

class Booking(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
        ("cancelled", "Cancelled"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="bookings")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    booked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-booked_at"]
        constraints = [
            models.UniqueConstraint(fields=["user", "event"], name="unique_user_event_booking")
        ]

    def __str__(self):
        return f"{self.user.username} - {self.event.title}"
