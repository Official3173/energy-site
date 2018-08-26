from django.contrib import admin
from .models import User

admin.site.register(User) # Allows User database to be accessable on the admin page of the site
