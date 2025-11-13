
from django.contrib import admin
from django.urls import path, include
from tasks.views import home, contuct

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", home),
    path("countuct/", contuct),
    path("tasks/", include("tasks.urls"))
]
