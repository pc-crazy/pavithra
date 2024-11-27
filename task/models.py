from email.policy import default
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Task(models.Model):
    created_at = models.DateTimeField(blank=True, null=True, auto_now=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    title = models.CharField(max_length=1024, blank=True, null=True)
    description= models.TextField(blank=True, null=True)
    assigned_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    status = models.BooleanField(default=False) # FALSE is Pending, True is Completed
    due_date = models.DateField(blank=True, null=True)

