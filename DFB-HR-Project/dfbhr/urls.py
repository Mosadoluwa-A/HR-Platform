"""dfbhr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from employees import views
from departments.views import list_departments
from donors.views import list_donors

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_user, name="login_user"),
    path('home/', views.home, name="home"),
    path('logout', views.logout_user, name="logout_user"),
    path('employees/', include('employees.urls')),
    path('departments/', list_departments, name="list_departments"),
    path('donors/', list_donors, name="list_donors")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
