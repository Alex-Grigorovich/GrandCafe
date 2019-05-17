from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first_list(request):
    return render(request, 'recipegrandcafe/index.html')