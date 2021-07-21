from django.shortcuts import render
from .models import Donor


def list_donors(request):
    if request.method == "GET":
        donors = Donor.objects.all()
        context = {
            "title": "Donors",
            "active_nav": "red-text",
            "donors": donors
        }
        return render(request, 'donors/donors.html', context)
