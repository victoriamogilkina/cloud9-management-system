from django.db import models

# Create your models here.
class Clients(models.Model):
    id = models.UUIDField(primary_key=True)
    full_name = models.CharField(max_length=200)
    pc_number = models.CharField(max_length=5, unique=True)
    remaining_time = models.DateTimeField()
    status = models.CharField(max_length=50)
    create_at = models.DateTimeField()
    expires_at = models.DateTimeField()
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'clients'

class Users(models.Model):
    id = models.UUIDField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.TextField()
    role = models.CharField(max_length=50)
    last_login = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
