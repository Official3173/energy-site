
from django import forms

class ContactForm(forms.Form):
    star_rating = forms.CharField()
    kwh = forms.CharField()
    model_num = forms.CharField()
    
    