from django.shortcuts import render
from .models import *


# Create your views here.


def main(request):
    tasks = Task.objects.all()

    context = {'tasks': tasks}

    return render(request, 'pimbo/main.html', context)
