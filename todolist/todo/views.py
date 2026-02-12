from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Category
from .forms import TaskForm, CategoryForm 


def categorylist(request):
    categories = Category.objects.all()
    
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categorylist')
    else:
        form = CategoryForm()
        
    return render(request, 'categorylist.html', {'categories': categories, 'form': form})




def tasklist(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    tasks = Task.objects.filter(name=category) 
    return render(request, 'tasklist.html', {'tasks': tasks, 'category': category})





def createtask(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.name = category  
            task.save()
            return redirect('tasklist', category_id=category.id)
    else:
        form = TaskForm()
    return render(request, 'taskform.html', {'form': form, 'category': category})









def deletecategory(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    
    if request.method == "POST":
        category.delete() 
        return redirect('categorylist')
    return render(request, 'taskdelete.html', {'item': category, 'type': 'Category'})







def deletetask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    category_id = task.name.id 
    if request.method == 'POST':
        task.delete()
        return redirect('tasklist', category_id=category_id)
    return render(request, 'taskdelete.html', {'item': task, 'type': 'Task'})