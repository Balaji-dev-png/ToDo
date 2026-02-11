from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Category
from .forms import TaskForm
# Create your views here.

def categorylist(request):
    categories = Category.objects.all()
    return render(request, "categorylist.html", {"categories" : categories})


def tasklist(request):
    category = get_object_or_404(Category, pk = pk)
    tasks = Task.objects.all()
    return render(request, 'tasklist.html', {'tasks' : tasks, 'category' : category})




def createtask(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasklist')
        
    else:
        form = TaskForm()

    return render(request, 'taskform.html', {'form' : form})






def updatetask(request, pk):
    task = get_object_or_404(Task, pk = pk)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=Task)
        if form.is_valid():
            form.save()
            return redirect('tasklist')
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'taskform.html', {'form' : form})






def deletetask(request, pk):
    task = get_object_or_404(Task, pk = pk)
    if request.method == 'POST':
        task.delete()
        return redirect('tasklist') 
    
    return render(request, 'taskdelete.html', {'task' : task})