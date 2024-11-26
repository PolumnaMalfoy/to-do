from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    STATUS = [
        ['not started', 'not started'],
        ['in progress', 'in progress'],
        ['completed', 'completed']
    ]
    title = models.CharField(max_length=255)
    deadline = models.DateField()
    status = models.CharField(max_length=50, choices=STATUS, null=True)
    detail = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title