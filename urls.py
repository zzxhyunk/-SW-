from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/<int:id>/', views.task_detail, name='task_detail'),
    path('new/', views.task_create, name='task_create'),
    path('edit/<int:id>/', views.task_update, name='task_update'),
    path('delete/<int:id>/', views.task_delete, name='task_delete'),
]
