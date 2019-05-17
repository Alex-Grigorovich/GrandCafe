from django.urls import path
import django.contrib.staticfiles
from .views import *

urlpatterns = [
    path('', first_list)

]
