from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class Task(models.Model):
    PENDING = 1
    DONE = 0

    name = models.CharField(max_length=250)
    description = models.TextField()
    status = models.IntegerField(
        choices=[
            (PENDING, "PENDING"),
            (DONE, "DONE")
        ],
        default=PENDING
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
