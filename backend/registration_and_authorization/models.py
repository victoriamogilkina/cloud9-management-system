import uuid
from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **kwargs):
        user = self.model(username= username, **kwargs)
        user.set_password(password)
        user.save(using=self.db)
        return user


class Users(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    username = models.CharField(max_length=50, unique=True)
    password = models.TextField()
    role = models.CharField(max_length=50)
    last_login = models.DateTimeField(blank=True, null=True)

    USERNAME_FIELD = 'username'
    objects = UserManager()

    class Meta:
        managed = False
        db_table = 'users'