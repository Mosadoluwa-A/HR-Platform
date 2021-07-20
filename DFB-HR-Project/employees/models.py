from django.db import models
from django_countries.fields import CountryField
from departments.models import Department
from donors.models import Donor


class Employee(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_no = models.CharField(max_length=15)
    address = models.TextField()
    nationality = CountryField()
    STATES = (
        ("oyo", "Oyo"),
        ("ogun", "Ogun"),
        ("osun", "Osun"),
        ("lagos", "Lagos"),
        ("ondo", "Ondo"),
        ("kwara", "Kwara"),
        ("kogi", "Kogi"),
        ("ekiti", "ekiti"),
        ("delta", "Delta"),
    )
    state_of_origin = models.CharField(max_length=12, choices=STATES)
    M_STATUS = (
        ("single", "Single"),
        ("married", "Married"),
    )
    marital_status = models.CharField(max_length=8, choices=M_STATUS)
    GENDER = (
        ("male", "Male"),
        ("female", "Female"),
    )
    gender = models.CharField(max_length=7, choices=GENDER)
    date_of_birth = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="employees")
    ROLES = (
        ("security officer", "Security Officer"), ("senior security officer", "Senior Security Officer"),
        ("driver", "Driver"), ("senior driver", "Senior Driver"),
        ("cleaner", "Cleaner"), ("senior cleaner", "Senior Cleaner"),
        ("IT Officer", "IT Officer"), ("IT Consultant", "IT Consultant"),
        ("communications officer", "Communications Officer"),
        ("accounts assistant", "Accounts Assistant"), ("accountant", "Accountant"),
        ("senior accountant", "Senior Accountant"), ("finance manager", "Finance Manager"),
        ("research assistant", "Research Assistant"), ("data manager", "Data Manager"),
        ("m&e officer", "M&E Officer"), ("medical advisor", "Medical Advisor"),
        ("senior medical advisor", "Senior Medical Advisor"),
        ("medical coordinator", "Medical Coordinator"), ("admin assistant", "Admin Assistant"),
        ("admin officer", "Admin Officer"), ("office manager", "Office Manager"),
        ("operations & hr", "Operations & HR"), ("deputy country rep", "Deputy Country Rep"),
        ("country rep", "Country Rep"),
    )
    role = models.CharField(max_length=50, choices=ROLES, null=True)
    donors = models.ManyToManyField(Donor, verbose_name="Donors")
    employment_date = models.DateField()
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='staff/images/', default='default.png')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('employees:staff_profile', kwargs={'id': self.id})


class StaffDocument(models.Model):
    name = models.CharField(max_length=30, default="Staff Document")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="files")
    file = models.FileField(upload_to="files")

    def __str__(self):
        return self.name
