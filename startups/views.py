from django.shortcuts import render
from .models import Startup

def startup_list(request):
    startups = Startup.objects.all()
    return render(request, 'startups/startup_list.html', {'startups': startups})