from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    due_date = models.DateField()
    is_complated = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    uodate_at = models.DateTimeField(auto_now_add=True)
