from django.shortcuts import HttpResponse,get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from .models import Task

def index(request):
    if request.method == 'POST':
        data = request.POST.get('task_name')
        if data:
            Task.objects.create(title=data)
        return redirect('/')
    tasks = Task.objects.all()
    return render(request, 'hello.html', {'tasks': tasks})
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('/')
def patch_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = not task.is_completed
    task.save()
    return redirect('/')








# def index(request):
#     my_tasks = ['Finish Django Tutorial', 'Eat Lunch', 'Sleep', 'Repeat']
#     return render(request, 'hello.html',{'tasks': my_tasks})
# from django.shortcuts import render
# from django.http import httpresponse
# def index(request):
#     person = {
#         'name': 'Rahul',
#         'age': 25,
#         'city': 'Bangalore'
#     }
#     return render(request, 'hello.html',person)

# def index(request):
    # return render(request, 'hello.html')