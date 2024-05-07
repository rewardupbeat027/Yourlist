from django import forms
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
        exclude = ('user',)


class ProductForm(forms.ModelForm):
    product = forms.ModelMultipleChoiceField(
        queryset=Purchase.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False  # Указываем, что это поле необязательно
    )

    class Meta:
        model = Purchase
        fields = ['product']  # Указываем, что поле product должно быть в форме
