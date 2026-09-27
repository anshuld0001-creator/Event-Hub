from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("events/", views.event_list, name="event_list"),
    path("events/<int:pk>/", views.event_detail, name="event_detail"),
    path("events/<int:pk>/book/", views.book_event, name="book_event"),
    path("bookings/", views.my_bookings, name="my_bookings"),
    path("bookings/<int:pk>/cancel/", views.cancel_booking, name="cancel_booking"),
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("profile/", views.profile, name="profile"),
    path("password/", views.password_change, name="password_change"),

    path("admin-panel/", views.admin_dashboard, name="admin_dashboard"),
    path("admin-panel/events/", views.admin_events, name="admin_events"),
    path("admin-panel/events/add/", views.admin_event_create, name="admin_event_create"),
    path("admin-panel/events/<int:pk>/edit/", views.admin_event_edit, name="admin_event_edit"),
    path("admin-panel/events/<int:pk>/delete/", views.admin_event_delete, name="admin_event_delete"),
    path("admin-panel/categories/", views.admin_categories, name="admin_categories"),
    path("admin-panel/categories/add/", views.admin_category_create, name="admin_category_create"),
    path("admin-panel/categories/<int:pk>/edit/", views.admin_category_edit, name="admin_category_edit"),
    path("admin-panel/categories/<int:pk>/delete/", views.admin_category_delete, name="admin_category_delete"),
    path("admin-panel/bookings/", views.admin_bookings, name="admin_bookings"),
    path("admin-panel/bookings/<int:pk>/<str:action>/", views.admin_booking_action, name="admin_booking_action"),
    path("admin-panel/users/", views.admin_users, name="admin_users"),
    path("admin-panel/users/<int:pk>/toggle/", views.admin_user_toggle, name="admin_user_toggle"),
]
