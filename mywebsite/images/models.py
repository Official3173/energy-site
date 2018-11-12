from django.contrib.auth.models import User
from django import forms


'''
class UserForm(forms.ModelForm):
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget = forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['email', 'password']
'''




#from django.db import models # this is needed to create new database entries, was imported for User code below
'''
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_picture = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    # prints out a string with the first name and last name in the manage.py shell
    # with first name and last name displayed 
'''