from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255, primary_key=True)
    employee_id = models.CharField(max_length=255)
    user_password = models.CharField(max_length=255)
    access_level = models.CharField(max_length=255)