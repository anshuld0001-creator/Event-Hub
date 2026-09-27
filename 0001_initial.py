from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, unique=True)),
                ("description", models.TextField(blank=True)),
            ],
            options={
                "verbose_name_plural": "Categories",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("event_date", models.DateField()),
                ("event_time", models.TimeField()),
                ("venue", models.CharField(max_length=255)),
                ("capacity", models.PositiveIntegerField(default=100)),
                ("status", models.CharField(choices=[("upcoming", "Upcoming"), ("completed", "Completed"), ("cancelled", "Cancelled")], default="upcoming", max_length=20)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("category", models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="events", to="events.category")),
            ],
            options={
                "ordering": ["event_date", "event_time"],
            },
        ),
        migrations.CreateModel(
            name="Booking",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("status", models.CharField(choices=[("pending", "Pending"), ("approved", "Approved"), ("rejected", "Rejected"), ("cancelled", "Cancelled")], default="pending", max_length=20)),
                ("booked_at", models.DateTimeField(auto_now_add=True)),
                ("event", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="bookings", to="events.event")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="bookings", to="auth.user")),
            ],
            options={
                "ordering": ["-booked_at"],
            },
        ),
        migrations.AddConstraint(
            model_name="booking",
            constraint=models.UniqueConstraint(
                fields=("user", "event"),
                name="unique_user_event_booking",
            ),
        ),
    ]
