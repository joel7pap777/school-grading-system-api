from django.db import models

# Create your models here.

from django.db import models
from students.models import Student
from classes.models import Subject


class Score(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    classwork_score = models.DecimalField(max_digits=5, decimal_places=2)
    exam_score = models.DecimalField(max_digits=5, decimal_places=2)

    total_score = models.DecimalField(max_digits=5, decimal_places=2)
    grade = models.CharField(max_length=2)

    class Meta:
        unique_together = ('student', 'subject')

    def __str__(self):
        return f"{self.student} - {self.subject}"