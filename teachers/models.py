from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staff_id = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.user.username