from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Category
from .forms import TaskForm # Assumes you have a CategoryForm if adding categories manually

# 1. Main Page: List all Categories (Work Headings)
from .forms import TaskForm, CategoryForm # Make sure both are imported

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
    # This specifically gets tasks linked to THIS category
    tasks = Task.objects.filter(name=category) 
    return render(request, 'tasklist.html', {'tasks': tasks, 'category': category})

def createtask(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            # This line fixes the [null] in your database image
            task.name = category  
            task.save()
            return redirect('tasklist', category_id=category.id)
    else:
        form = TaskForm()
    return render(request, 'taskform.html', {'form': form, 'category': category})


def deletecategory(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    
    if request.method == "POST":
        category.delete()  # This physically removes it from the DB
        return redirect('categorylist') # Redirect back to the main list
    
    # If it's a GET request, show the confirmation page
    return render(request, 'taskdelete.html', {'item': category, 'type': 'Category'})

# 5. Delete Task: Your existing delete logic
def deletetask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    category_id = task.name.id # Save ID to redirect back to the correct list
    if request.method == 'POST':
        task.delete()
        return redirect('tasklist', category_id=category_id)
    return render(request, 'taskdelete.html', {'item': task, 'type': 'Task'})