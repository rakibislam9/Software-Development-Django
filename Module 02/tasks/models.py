from django.db import models

# Create your models here.

class Employees(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)


    def __str__(self):
        return self.name
    

# Tasks Models create

class Task(models.Model):
    STATUS_CHOICS = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In progress'),
        ('COMPLETED', 'COMPLETED')
    ]
    project = models.ForeignKey("Projects", on_delete=models.CASCADE, default=1, related_name="tasks")
    assigned_to = models.ManyToManyField(Employees, related_name="tasks")
    title = models.CharField(max_length=250)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=15,choices=STATUS_CHOICS, default="PENDING")
    is_completed = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    

# Tasks Details Model Creae

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
    assigned_to = models.CharField(max_length=255, null=True, blank=True)
    priority = models.CharField(max_length=1, choices=PRIORITY_OPTIONS, default=Low)

    notes = models.TextField(blank=True, null=True)



    def __str__(self):
        return f"Details form Task {self.task.title}"

# Projects models create

class Projects(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()


    def __str__(self):
        return self.name