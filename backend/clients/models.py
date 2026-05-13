from django.db import models
import uuid
from django.utils import timezone
from django.conf import settings


# Create your models here.
class Clients(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    full_name = models.CharField(max_length=200)
    pc_number = models.CharField(max_length=5, unique=True)
    status = models.CharField(max_length=50, default='active')
    create_at = models.DateTimeField(default=timezone.now())
    expires_at = models.DateTimeField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'clients'

    def get_remaining_seconds(self):
        now = timezone.now()
        if now >= self.expires_at:
            return 0
        return int((self.expires_at - now).total_seconds())

class Users(models.Model):
    id = models.UUIDField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.TextField()
    role = models.CharField(max_length=50)
    last_login = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        managed = False
        db_table = 'users'
