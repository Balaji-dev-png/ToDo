from django.urls import path
from . import views

urlpatterns = [
    path('', views.categorylist, name='categorylist'),
    path('category/<int:category_id>/', views.tasklist, name='tasklist'),
    path('category/<int:category_id>/add/', views.createtask, name='createtask'),
    path('category/<int:category_id>/delete/', views.deletecategory, name='deletecategory'),
    path('task/delete/<int:pk>/', views.deletetask, name='deletetask'),
]