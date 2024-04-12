from django.db import models

# relacionada a base de dados

class Users(models.Model):
    email = models.TextField(primary_key=True, null=False, blank=False, unique=True)
    senha = models.IntegerField(null=False, blank=False)