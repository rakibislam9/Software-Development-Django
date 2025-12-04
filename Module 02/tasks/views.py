from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import Employees, Task, TaskDetails,Projects
from datetime import date, timedelta
from django.db.models import Q, Count, Max, Min, Avg
from django.utils import timezone

# Create your views here.

def manager_dashboard(request):
    return render(request, "dashboard/manager-dashboard.html")
    

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