from __future__ import annotations

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Clue(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    next_clue = models.OneToOneField('self', on_delete=models.SET_NULL, null=True, blank=True)
    is_dead_end = models.BooleanField(default=False)
    is_solution = models.BooleanField(default=False)

class UserProgress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_clue = models.ForeignKey(Clue, on_delete=models.SET_NULL, null=True)
    start_time = models.DateTimeField(auto_now_add=True)
    time_taken_per_clue = models.JSONField(default=dict)
    attempts_per_clue = models.JSONField(default=dict)
