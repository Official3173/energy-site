
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

IMAGE_CHOICES = [
    ('0.5', '0.5'),
    ('1', '1'),
    ('1.5', '1.5'),
    ('2', '2'),
    ('2.5', '2.5'),
    ('3', '3'),
    ('3.5', '3.5'),
    ('4', '4'),
    ('4.5', '4.5'),
    ('5', '5'),
]

PRIMARY_TEMP_CHOICES = [
    ('Hot', 'Hot'),
    ('Cold', 'Cold')
]

SECONDARY_TEMP_CHOICES = [
    ('hot', 'Hot'),
    ('cold', 'Cold')
]

class ContactForm(forms.Form):
    star_rating = forms.CharField(label='Star Rating', widget=forms.Select(choices=IMAGE_CHOICES))
    kwh = forms.CharField(label='kWh')
    model_num = forms.CharField(label='Model Number')
    primary = forms.CharField(label='Primary Water Connection', widget=forms.Select(choices=PRIMARY_TEMP_CHOICES))
    secondary = forms.CharField(label='Secondary Water Connection', widget=forms.Select(choices=SECONDARY_TEMP_CHOICES))


class SignUpForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class SignInForm(forms.Form):
     username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
     password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
