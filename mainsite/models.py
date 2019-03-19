from django.db import models

# Create your models here.
class user(models.Model):
    user_id = models.CharField(max_length=10)
    user_passwd = models.CharField(max_length=10)
