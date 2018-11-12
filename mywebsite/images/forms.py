
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

class ContactForm(forms.Form):
    star_rating = forms.CharField(label='Star Rating', widget=forms.Select(choices=IMAGE_CHOICES))
    kwh = forms.CharField(label='kWh')
    model_num = forms.CharField(label='Model Number')

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )




    
    