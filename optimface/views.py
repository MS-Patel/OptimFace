from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Function based view

def home(request):
    return render(request,"index.html",{})#response