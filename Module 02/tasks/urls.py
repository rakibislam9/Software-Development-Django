from django.urls import path
from tasks.views import manager_dashboard, user_dashboard, Test



urlpatterns = [
    path('dashboard/', manager_dashboard),
    path('userdashboard/', user_dashboard),
    path('test/', Test)
]
