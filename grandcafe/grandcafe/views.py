from django.http import HttpResponse


def home_page(request):
    return HttpResponse('<h1>Welcome to prime time bitch</h1>')