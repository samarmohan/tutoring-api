from django.db import models
from django.contrib.auth.models import User


class Tutor(models.Model):
    full_name = models.CharField(max_length=40)
    email = models.EmailField()
    notes = models.TextField()

    def __str__(self):
        return self.full_name


class Tutee(models.Model):
    full_name = models.CharField(max_length=40)
    email = models.EmailField()
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, related_name="tutees", null=True)
    subjects = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name
