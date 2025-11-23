from django.shortcuts import render
from django.http import HttpResponse
from tasks.form import TaskForm
from tasks.models import Employees

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
    context = {"form": form}
    return render(request,"dashboard/test_create_mathod.html", context)