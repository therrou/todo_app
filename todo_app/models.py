from django.contrib.auth.models import User
from django.db import models


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text} - {self.status}"
