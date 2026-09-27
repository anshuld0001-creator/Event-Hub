from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.db.models import Q, Count
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import RegisterForm, ProfileForm, EventForm, CategoryForm
from .models import Category, Event, Booking

def home(request):
    events = Event.objects.filter(
        status="upcoming",
        event_date__gte=timezone.localdate()
    ).select_related("category")[:6]
    return render(request, "events/home.html", {"events": events})

def event_list(request):
    events = Event.objects.filter(status="upcoming", event_date__gte=timezone.localdate()).select_related("category")
    q = request.GET.get("q", "").strip()
    category = request.GET.get("category", "")
    if q:
        events = events.filter(Q(title__icontains=q) | Q(description__icontains=q) | Q(venue__icontains=q))
    if category:
        events = events.filter(category_id=category)
    return render(request, "events/event_list.html", {
        "events": events,
        "categories": Category.objects.all(),
        "q": q,
        "selected_category": category,
    })

def event_detail(request, pk):
    event = get_object_or_404(Event.objects.select_related("category"), pk=pk)
    booking = None
    if request.user.is_authenticated:
        booking = Booking.objects.filter(user=request.user, event=event).first()
    return render(request, "events/event_detail.html", {"event": event, "booking": booking})

@login_required
def book_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method != "POST":
        return redirect("event_detail", pk=pk)
    if event.status != "upcoming" or event.event_date < timezone.localdate():
        messages.error(request, "This event is not available for booking.")
        return redirect("event_detail", pk=pk)
    if event.seats_left <= 0:
        messages.error(request, "Sorry, this event is fully booked.")
        return redirect("event_detail", pk=pk)
    booking, created = Booking.objects.get_or_create(user=request.user, event=event)
    if not created:
        messages.info(request, f"Your existing booking is {booking.status}.")
    else:
        messages.success(request, "Event registration submitted successfully.")
    return redirect("my_bookings")

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).select_related("event", "event__category")
    return render(request, "events/my_bookings.html", {"bookings": bookings})

@login_required
def cancel_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == "POST":
        if booking.status not in ["cancelled", "rejected"]:
            booking.status = "cancelled"
            booking.save(update_fields=["status"])
            messages.success(request, "Booking cancelled successfully.")
    return redirect("my_bookings")

def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Welcome! Your account has been created.")
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})

@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("profile")
    else:
        form = ProfileForm(instance=request.user)
    return render(request, "events/profile.html", {"form": form})

@login_required
def password_change(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password changed successfully.")
            return redirect("profile")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "registration/password_change.html", {"form": form})

def is_staff(user):
    return user.is_authenticated and user.is_staff

staff_required = user_passes_test(is_staff, login_url="login")

@staff_required
def admin_dashboard(request):
    context = {
        "total_events": Event.objects.count(),
        "total_users": User.objects.count(),
        "total_bookings": Booking.objects.count(),
        "pending_bookings": Booking.objects.filter(status="pending").count(),
        "upcoming_events": Event.objects.filter(status="upcoming", event_date__gte=timezone.localdate()).count(),
        "recent_bookings": Booking.objects.select_related("user", "event")[:8],
    }
    return render(request, "adminpanel/dashboard.html", context)

@staff_required
def admin_events(request):
    events = Event.objects.select_related("category").annotate(booking_count=Count("bookings"))
    q = request.GET.get("q", "").strip()
    if q:
        events = events.filter(Q(title__icontains=q) | Q(venue__icontains=q))
    return render(request, "adminpanel/events.html", {"events": events, "q": q})

@staff_required
def admin_event_create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Event created successfully.")
            return redirect("admin_events")
    else:
        form = EventForm()
    return render(request, "adminpanel/event_form.html", {"form": form, "title": "Add New Event"})

@staff_required
def admin_event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, "Event updated successfully.")
            return redirect("admin_events")
    else:
        form = EventForm(instance=event)
    return render(request, "adminpanel/event_form.html", {"form": form, "title": "Edit Event"})

@staff_required
def admin_event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        event.delete()
        messages.success(request, "Event deleted successfully.")
        return redirect("admin_events")
    return render(request, "adminpanel/confirm_delete.html", {"object": event, "back_url": "admin_events"})

@staff_required
def admin_categories(request):
    return render(request, "adminpanel/categories.html", {"categories": Category.objects.all()})

@staff_required
def admin_category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category added.")
            return redirect("admin_categories")
    else:
        form = CategoryForm()
    return render(request, "adminpanel/category_form.html", {"form": form, "title": "Add Category"})

@staff_required
def admin_category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Category updated.")
            return redirect("admin_categories")
    else:
        form = CategoryForm(instance=category)
    return render(request, "adminpanel/category_form.html", {"form": form, "title": "Edit Category"})

@staff_required
def admin_category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        category.delete()
        messages.success(request, "Category deleted.")
        return redirect("admin_categories")
    return render(request, "adminpanel/confirm_delete.html", {"object": category, "back_url": "admin_categories"})

@staff_required
def admin_bookings(request):
    bookings = Booking.objects.select_related("user", "event", "event__category")
    status = request.GET.get("status", "")
    if status:
        bookings = bookings.filter(status=status)
    return render(request, "adminpanel/bookings.html", {"bookings": bookings, "selected_status": status})

@staff_required
def admin_booking_action(request, pk, action):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == "POST":
        if action in ["approve", "reject"]:
            booking.status = "approved" if action == "approve" else "rejected"
            booking.save(update_fields=["status"])
            messages.success(request, f"Booking {booking.status}.")
    return redirect("admin_bookings")

@staff_required
def admin_users(request):
    users = User.objects.all().order_by("-date_joined")
    q = request.GET.get("q", "").strip()
    if q:
        users = users.filter(Q(username__icontains=q) | Q(email__icontains=q) | Q(first_name__icontains=q) | Q(last_name__icontains=q))
    return render(request, "adminpanel/users.html", {"users": users, "q": q})

@staff_required
def admin_user_toggle(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST" and user != request.user:
        user.is_active = not user.is_active
        user.save(update_fields=["is_active"])
        messages.success(request, f"User {'activated' if user.is_active else 'deactivated'}.")
    return redirect("admin_users")
