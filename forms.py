from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Category, Event

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "First name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last name"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email address"}),
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title", "description", "category", "event_date", "event_time", "venue", "capacity", "status"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Event title"}),
            "description": forms.Textarea(attrs={"rows": 5, "placeholder": "Describe the event..."}),
            "event_date": forms.DateInput(attrs={"type": "date"}),
            "event_time": forms.TimeInput(attrs={"type": "time"}),
            "venue": forms.TextInput(attrs={"placeholder": "Venue"}),
            "capacity": forms.NumberInput(attrs={"min": 1}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Category name"}),
            "description": forms.Textarea(attrs={"rows": 3}),
        }

class AdminUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "is_active", "is_staff"]
