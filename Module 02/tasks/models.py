from django.db import models

# Create your models here.

class Employees(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    


class Task(models.Model):
    Projects = models.ForeignKey("Projects", on_delete=models.CASCADE, default=1, related_name="tasks")
    assigned_to = models.ManyToManyField(Employees, related_name="tasks")
    title = models.CharField(max_length=250)
    description = models.TextField()
    due_date = models.DateField()
    is_complated = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    uodate_at = models.DateTimeField(auto_now_add=True)



class TaskDetails(models.Model):
    High = 'H'
    Miduim = 'M'
    Low = 'L'

    PRIORITY_OPTIONS = (
        (High, 'High'),
        (Miduim, 'Miduim'),
        (Low, 'Low') 
    )
    task = models.OneToOneField(Task, on_delete=models.DO_NOTHING,related_name='details',)

    priority = models.CharField(max_length=1, choices=PRIORITY_OPTIONS, default=Low)

    notes = models.TextField(blank=True, null=True)



class Projects(models.Model):
    Name = models.CharField(max_length=150)
    Start_date = models.DateField()