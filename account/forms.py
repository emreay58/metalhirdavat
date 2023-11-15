from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(label="Adınız  ", max_length=100)
    last_name = forms.CharField(label="Soyadınız", max_length=100)
    email = forms.EmailField(label="E-Maliniz", max_length=100)

    class meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
