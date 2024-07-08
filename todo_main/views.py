from django.http import HttpResponse
from django.shortcuts import render

from todos.models import Task


def home(request):
    # order_ by wont work now due to the issue of datetimefield not beingn string
    tasks = Task.objects.filter(is_completed=False).order_by('updated_at')
    context = {
        'tasks' : tasks
    }
    return render(request, 'home.html', context)