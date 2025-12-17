from django.shortcuts import render, redirect
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm, TaskDetaileModeleForm
from tasks.models import Employees, Task, TaskDetails,Projects
from datetime import date, timedelta
from django.db.models import Q, Count, Max, Min, Avg
from django.utils import timezone
from django.contrib import messages

# Create your views here.

def manager_dashboard(request):



    type = request.GET.get('type', 'all')
    # print(type)

    tasks = Task.objects.select_related('details').prefetch_related('assigned_to').all()


    counts = Task.objects.aggregate(
        total = Count('id'),
        complated = Count('id', filter= Q(status='COMPLETED')),
        in_progress = Count('id', filter=Q(status='IN_PROGRESS')),
        pending = Count('id', filter=Q(status='PENDING')),
    )

    # Retrive data

    baces_qurey = Task.objects.select_related('details').prefetch_related('assigned_to')


    if type == 'complated':
        tasks =  baces_qurey .filter(status='COMPLETED')
    elif type == 'in_progress':
        tasks =  baces_qurey .filter(status='IN_PROGRESS')
    elif type == 'pending':
        tasks =  baces_qurey .filter(status='PENDING')
    elif type == 'all':
        tasks =  baces_qurey .all()

    context = {
        "tasks" : tasks,
        "counts" : counts
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
    task_form = TaskModelForm()
    task_detail_form = TaskDetaileModeleForm()

    if request.method == "POST":
        task_form = TaskModelForm(request.POST)
        task_detail_form = TaskDetaileModeleForm(request.POST)
        if task_form.is_valid() and task_detail_form.is_valid():

            """For Model Form Data"""

            task = task_form.save()
            task_detail = task_detail_form.save(commit = False)
            task_detail.task = task
            task_detail.save()


            messages.success(request, "Task Create Successfully")
            return redirect('task-form')
                          
    
    

    context = {"task_form": task_form, "task_detail_form" : task_detail_form }
    return render(request,"dashboard/test_create_mathod.html", context)

# view_task define
def view_task(request):

    # task_count = Task.objects.aggregate(num_task=Count('id'))
    projects  = Projects.objects.annotate(num_task=Count('tasks'))
    

    


    return render(request, "show_task.html", {"projects": projects})