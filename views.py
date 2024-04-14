# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()  # 데이터베이스에서 모든 Task 객체를 가져옵니다.
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def task_detail(request, id):
    task = get_object_or_404(Task, pk=id)  # 주어진 ID를 가진 Task 객체를 가져오거나, 404 에러를 발생시킵니다.
    return render(request, 'todo/task_detail.html', {'task': task})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # 폼 데이터가 유효하면 Task 객체를 저장합니다.
            return redirect('task_list')  # 할 일 목록 페이지로 리다이렉트합니다.
    else:
        form = TaskForm()  # GET 요청시 비어있는 폼을 생성합니다.
    return render(request, 'todo/task_form.html', {'form': form})

def task_update(request, id):
    task = get_object_or_404(Task, pk=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/task_form.html', {'form': form})

def task_delete(request, id):
    task = get_object_or_404(Task, pk=id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'todo/task_confirm_delete.html', {'task': task})
