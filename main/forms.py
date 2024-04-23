from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import Purchase


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")


class SuperModelForm(ModelForm):
    class Meta:
        model = Purchase
        fields = "__all__"
