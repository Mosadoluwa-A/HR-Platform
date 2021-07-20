from django.forms import ModelForm
from .models import Employee, StaffDocument


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'phone_no', 'address', 'nationality', 'state_of_origin',
                  'marital_status', 'gender', 'date_of_birth', 'department', 'role',
                  'employment_date', 'image', 'donors']


class DocumentForm(ModelForm):
    class Meta:
        model = StaffDocument
        fields = ['name', 'employee', 'file']
