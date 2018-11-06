
from django import forms

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


class SignUpForm(forms.Form):
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={'class' : 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.TextInput(attrs={'class' : 'form-control'}))
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    