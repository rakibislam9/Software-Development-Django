from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm
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
    employees = Employees.objects.all()
    form = TaskForm(employees=employees)

    if request.method == "POST":
        form = TaskForm(request.POST, employees=employees)
        if form.is_valid():
            # print(form.cleaned_data)

            data = form.cleaned_data
            title = data.get('title')
            description = data.get('description')
            due_date = data.get('due_date')
            assigned_to = data.get('assigned_to')

            task = Task.objects.create(
                title=title, description=description, due_date=due_date
            )

            for emp_id in assigned_to:
                employees = Employees.objects.get(id=emp_id)
                task.assigned_to.add(employees)

            return HttpResponse("Task Added successfully")

    context = {"form": form}
    return render(request,"dashboard/test_create_mathod.html", context)