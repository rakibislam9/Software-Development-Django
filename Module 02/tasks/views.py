from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import Employees, Task, TaskDetails,Projects
from datetime import date, timedelta
from django.db.models import Q, Count, Max, Min, Avg
from django.utils import timezone

# Create your views here.

def manager_dashboard(request):

    tasks = Task.objects.select_related('details').prefetch_related('assigned_to').all()

    # tatal_task = tasks.count()

    # comlead_task = Task.objects.filter(status="COMPLETED").count()

    # in_progres_task = Task.objects.filter(status="IN_PROGRESS").count()

    # peinding_task = Task.objects.filter(status="PENDING").count()

    # context = {
    #     'tasks' : tasks,
    #     'tatal_task' : tatal_task,
    #     'peinding_task' : peinding_task,
    #     'in_progres_task' : in_progres_task,
    #     'comlead_task' : comlead_task
    # }

    counts = Task.objects.aggregate(
        total = Count('id'),
        complated = Count('id', filter= Q(status='COMPLETED')),
        in_progress = Count('id', filter=Q(status='IN_PROGRESS')),
        pending = Count('id', filter=Q(status='PENDING')),
    )

    context = {
        "tasks" : tasks,
        "Counts" : counts
    }
    return render(request, "dashboard/manager-dashboard.html", context)
    
# User Dashboard 
def user_dashboard(request):
    return render(request, "dashboard/userdashboard.html")



def Test(request):
    context = {
        "name" : ["Rakib", "Imone", "Shahin"],
        "age" : 22
    }
    return render(request, "dashboard/test.html", context)

def Test(request):
    context = {
        "num" : [10,20,30,40,50]
    }
    return render(request, "dashboard/test.html", context)

def task_form(request):
    # employees = Employees.objects.all()
    form = TaskModelForm()

    if request.method == "POST":
        form = TaskModelForm(request.POST)
        if form.is_valid():

            """For Model Form Data"""

            form.save()

            return render(request, "dashboard/test_create_mathod.html", {"form": form, "message": "Task added Successfully"})
                          
    
    

    context = {"form": form}
    return render(request,"dashboard/test_create_mathod.html", context)

# view_task define
def view_task(request):

    # task_count = Task.objects.aggregate(num_task=Count('id'))
    projects  = Projects.objects.annotate(num_task=Count('tasks'))
    # projects  = Projects.objects.annotate(num_task=Max('tasks'))

    


    return render(request, "show_task.html", {"projects": projects})