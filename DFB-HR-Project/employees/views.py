import os
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from employees.models import Employee, StaffDocument
from employees.forms import EmployeeForm, DocumentForm
from donors.models import Donor
from departments.models import Department
from django_countries import countries


# EMPLOYEES APP

@login_required(login_url='/')
def home(request):
    # watever = requests.get("https://nigerian-states-info.herokuapp.com/api/v1/states")
    # json = watever.json()
    # print(dir(json))
    staffs = Employee.objects.filter(is_active=True)
    inactive = Employee.objects.filter(is_active=False)
    dictionary = {
        "active": staffs,
        "inactive": inactive,
        "active_nav": "red-text",
        "title": "Home"
    }
    return render(request, 'employees/home.html', dictionary)


@login_required(login_url='/')
def staff_profile(request, staff_id):
    staff = get_object_or_404(Employee, id=staff_id)
    documents = StaffDocument.objects.filter(employee=staff_id)
    states = ['oyo', 'ogun', 'osun', 'lagos', 'kwara', 'ekiti', 'ondo', 'kogi', 'delta']
    departments = Department.objects.all()
    donors = Donor.objects.all()
    roles = [
        "security officer", "senior security officer", "driver", "senior driver", "cleaner", "senior cleaner",
        "IT Officer", "IT Consultant", "communications officer", "accounts assistant", "accountant", "senior accountant",
        "finance manager", "research assistant", "data manager", "m&e officer", "medical advisor",
        "senior medical advisor", "medical coordinator", "admin assistant", "admin officer", "office manager",
        "operations & hr", "deputy country rep", "country rep"
    ]
    dictionary = {
        "title": "Profile",
        "active_nav": "red-text",
        "staff": staff,
        "documents": documents,
        "countries": countries,
        "states": states,
        "departments": departments,
        "roles": roles,
        "donors": donors
    }
    return render(request, 'employees/profile.html', dictionary)


@login_required(login_url='/')
def add_staff(request):
    if request.method == "GET":
        departments = Department.objects.all()
        donors = Donor.objects.all()
        dictionary = {
            "title": "Add Employee",
            "active_nav": "red-text",
            "countries": countries,
            "departments": departments,
            "donors": donors,
        }
        return render(request, 'employees/add-employee.html', dictionary)
    else:
        try:
            form = EmployeeForm(request.POST, request.FILES)

            if form.is_valid:
                form.save()
                messages.success(request, "Staff Added Successfully")
                return redirect(home)
            else:
                print(form.errors)
                messages.error(request, "Please fill all the fields")
                return redirect(add_staff)
        except Exception as e:
            print(e)
            form = EmployeeForm(request.POST, request.FILES)
            print(form.errors)
            messages.error(request, "Data is not correct")
            departments = Department.objects.all()
            donors = Donor.objects.all()
            dictionary = {
                "title": "Add Employee",
                "countries": countries,
                "departments": departments,
                "donors": donors
            }
            return render(request, 'employees/add-employee.html', dictionary)


@login_required(login_url='/')
def edit_staff(request, staff_id):
    if request.method == "POST":

        try:
            employee = get_object_or_404(Employee, id=staff_id)
            form = EmployeeForm(request.POST, request.FILES, instance=employee)
            if form.is_valid():  # To check whether the fields are
                form.save()
                messages.success(request, "Staff data updated successfully")
                return redirect("employees:staff_profile", staff_id=employee.id)
            else:
                print(form.errors)
                messages.error(request, "Update Empty Fields")
                return redirect("employees:staff_profile", staff_id=employee.id)

        except ValueError:
            employee = get_object_or_404(Employee, id=staff_id)
            messages.error(request, "Update Failed Bad Data")
            return redirect("employees:staff_profile", staff_id=employee.id)
    else:
        pass


@login_required(login_url='/')
def add_files(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        staff_id = request.POST['employee']
        if form.is_valid():
            form.save()
            messages.success(request, "File Added Successfully")
            return redirect("employees:staff_profile", staff_id=staff_id)
        else:
            print(form.errors)
            staff_id = request.POST['employee']
            messages.error(request, "Data is not correct")
            return redirect("employees:staff_profile", staff_id=staff_id)
    else:
        pass


# AUTHENTICATION

def login_user(request):
    if request.user.is_authenticated:
        messages.success(request, "You are already logged in")
        return redirect(home)
    elif request.method == "GET":
        return render(request, 'employees/login.html')

    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, "Sorry username and passwords did not match")
            return render(request, 'employees/login.html')
        else:
            login(request, user)
            messages.success(request, "Login Success")
            return redirect(home)


def logout_user(request):
    if request.method == "POST":
        logout(request)
    return redirect(login_user)


