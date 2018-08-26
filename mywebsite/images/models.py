from django.db import models

# Models are blueprints for the database, like how data goes in

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_picture = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    # prints out a string with the first name and last name in the manage.py shell
    # with first name and last name displayed