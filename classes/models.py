from django.db import models

# Create your models here.
from django.db import models


class Class(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    

from teachers.models import Teacher


class Subject(models.Model):
    name = models.CharField(max_length=100)
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
