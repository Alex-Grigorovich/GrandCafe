from django.shortcuts import render


# Create your views here.

def first_list(request):
    return render(request, 'recipegrandcafe/index.html')