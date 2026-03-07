from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from classes.models import Class


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    admission_number = models.CharField(max_length=50, unique=True)
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username