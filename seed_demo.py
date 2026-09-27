from datetime import date, time, timedelta
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from events.models import Category, Event, Booking

class Command(BaseCommand):
    help = "Create demo users, categories and events."

    def handle(self, *args, **options):
        admin, created = User.objects.get_or_create(username="admin")
        if created:
            admin.set_password("admin123")
        admin.email = "admin@example.com"
        admin.is_staff = True
        admin.is_superuser = True
        admin.is_active = True
        admin.save()

        demo, created = User.objects.get_or_create(username="demo")
        if created:
            demo.set_password("demo123")
        demo.email = "demo@example.com"
        demo.first_name = "Demo"
        demo.last_name = "User"
        demo.is_active = True
        demo.save()

        categories = {}
        for name, desc in [
            ("Technology", "Technology, coding and innovation events."),
            ("Business", "Business, entrepreneurship and networking."),
            ("Workshop", "Hands-on workshops and learning sessions."),
            ("Cultural", "Cultural, creative and community events."),
        ]:
            cat, _ = Category.objects.get_or_create(name=name, defaults={"description": desc})
            categories[name] = cat

        samples = [
            ("AI & Future Tech Summit", "Explore practical AI, ML and emerging technologies with industry speakers.", "Technology", 20),
            ("Startup & Entrepreneurship Meetup", "Meet founders, builders and students working on new startup ideas.", "Business", 35),
            ("Full Stack Web Development Workshop", "Build and deploy a complete web application in a hands-on workshop.", "Workshop", 30),
            ("Creative Culture Fest", "A community event featuring music, art, food and student performances.", "Cultural", 100),
        ]

        start = date.today() + timedelta(days=7)
        for i, (title, description, cat, capacity) in enumerate(samples):
            Event.objects.get_or_create(
                title=title,
                defaults={
                    "description": description,
                    "category": categories[cat],
                    "event_date": start + timedelta(days=i * 5),
                    "event_time": time(10 + i, 30),
                    "venue": f"City Convention Hall - Room {i+1}",
                    "capacity": capacity,
                    "status": "upcoming",
                }
            )

        self.stdout.write(self.style.SUCCESS("Demo data is ready."))
        self.stdout.write("Admin: admin / admin123")
        self.stdout.write("User: demo / demo123")
