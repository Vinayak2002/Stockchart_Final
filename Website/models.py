from django.db import models

# Create your models here.
class Userdetails(models.Model):

    """
    This creates a model for keeping the details of users for signup and login.
    The data is stored in the 'db.sqlite3' local database.
    """

    email = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=200, null=True)
    