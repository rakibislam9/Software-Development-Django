from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import Employees, Task

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

            '''For Django Form'''
            # print(form.cleaned_data)

            # data = form.cleaned_data
            # title = data.get('title')
            # description = data.get('description')
            # due_date = data.get('due_date')
            # assigned_to = data.get('assigned_to')

            # task = Task.objects.create(
            #     title=title, description=description, due_date=due_date
            # )

            # for emp_id in assigned_to:
            #     employees = Employees.objects.get(id=emp_id)
            #     task.assigned_to.add(employees)

            

    context = {"form": form}
    return render(request,"dashboard/test_create_mathod.html", context)


def view_task(request):
    tasks = Task.objects.all()

    tasks3 = Task.objects.get(id=3)

    first_task = Task.objects.first()

    return render(request, "show_task.html", {"tasks": tasks, "tasks3" : tasks3, "first_task": first_task})