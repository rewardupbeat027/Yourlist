from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, DateInput

from .models import Purchase


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")


class SuperModelForm(ModelForm):
    date = forms.DateTimeField(
        input_formats=['%Y-%m-%dT%H:%M'],
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        label='Выберите дату'
    )

    class Meta:
        model = Purchase
        fields = "__all__"
        exclude = ('user', 'is_visible')

    # widgets = {
    #     'date': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),}


class ProductForm(forms.ModelForm):
    product = forms.ModelMultipleChoiceField(
        queryset=Purchase.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False  # Указываем, что это поле необязательно
    )

    class Meta:
        model = Purchase
        fields = ['product']  # Указываем, что поле product должно быть в форме
