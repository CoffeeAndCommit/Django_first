from django.shortcuts import render

from .models import ChaiVariety

# Create your views here.

def all_app(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'newapp/allapp.html', {'chais': chais})