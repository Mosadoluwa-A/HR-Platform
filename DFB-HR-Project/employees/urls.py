from django.urls import path
from . import views

app_name = "employees"

urlpatterns = [
    # path('home', views.home, name="home"),
    path('<int:staff_id>', views.staff_profile, name="staff_profile"),
    path('create', views.add_staff, name="create"),
    path('<int:staff_id>/update', views.edit_staff, name="edit_staff"),
    path('add_file', views.add_files, name="add_file")
]
