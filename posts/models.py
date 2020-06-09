from django.db import models


class User(models.Model):
    
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    is_admin = models.BooleanField(default=False)
    
    bio = models.CharField(blank=True, max_length=100)
    
    birthdate = models.DateTimeField(blank=True, null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.email
    