from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def index(request):
    return render(request,'index.html')

def all_profiles(request):
    profiles = ProfileModel.objects.all()
    return render(request, 'all_profiles.html', {'profiles': profiles})

def single_profile(request, id):
    profile = ProfileModel.objects.get(id=id)
    return render(request, 'single_profile.html', {'profile': profile})

def add_profile(request):
    if request.method == 'POST':
        # Handle form submission
        pass
    else:
        return render(request, 'add_profile.html')

def update_profile(request, id):
    profile = ProfileModel.objects.get(id=id)
    if request.method == 'POST':
        # Handle form submission
        pass
    else:
        return render(request, 'update_profile.html', {'profile': profile})

def deactivate_profile(request, id):
    profile = ProfileModel.objects.get(id=id)
    profile.deleted_at = datetime.utcnow()
    profile.save()




