from django.urls import path
from tasks.views import manager_dashboard, user_dashboard, Test, task_form, view_task



urlpatterns = [
    path('dashboard/', manager_dashboard, name = "manager-dashboard"),
    path('userdashboard/', user_dashboard),
    path('test/', Test),
    path('task_form/', task_form),
    path('view_task/',view_task)
]
