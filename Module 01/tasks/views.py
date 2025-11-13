from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from tasks.models import Task

# Create your views here.

def home(request):
    return HttpResponse("Welcome to HttpResponse")


def contuct(request):
    return HttpResponse("<h1 style= 'color: red' >This is countuct page</h1>")


def show_task(request):
    return HttpResponse("This is tasks page")