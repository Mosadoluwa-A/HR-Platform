from django.contrib import admin
from .models import Employee, StaffDocument

admin.site.register(StaffDocument)


class DocumentInline(admin.TabularInline):
    model = StaffDocument


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    inlines = [
        DocumentInline,
               ]
