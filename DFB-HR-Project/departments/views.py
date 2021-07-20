from django.shortcuts import render
from .models import Department


def list_departments(request):
    if request.method == "GET":
        departments = Department.objects.all()
        context = {
            "title": "Departments",
            "active_nav": "red-text",
            "departments": departments
        }
        return render(request, 'departments/departments.html', context)
