from django.db import models

# FISNIH THIS
# CREATE A MIGRATION


class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)