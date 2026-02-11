from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasklist, name="tasklist"),
    path('create/', views.createtask, name = "createtask"),
    path('<int:pk>/delete/', views.deletetask, name="deletetask"),
    path('<int:pk>/update/',views.updatetask, name="updatetask"),
]