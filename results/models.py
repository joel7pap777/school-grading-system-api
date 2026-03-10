from django.db import models


class Result(models.Model):
    student_name = models.CharField(max_length=100)

    class_score = models.FloatField()
    exam_score = models.FloatField()

    total = models.FloatField(blank=True, null=True)
    grade = models.CharField(max_length=2, blank=True)

    def save(self, *args, **kwargs):
        self.total = self.class_score + self.exam_score

        if self.total >= 80:
            self.grade = "A"
        elif self.total >= 70:
            self.grade = "B"
        elif self.total >= 60:
            self.grade = "C"
        elif self.total >= 50:
            self.grade = "D"
        else:
            self.grade = "F"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student_name} - {self.grade}"