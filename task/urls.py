from django.urls import path
from task.views import *

urlpatterns=[
    path('add_task/', add_task, name='add_task'),
    path('edit_task/<int:task_id>/', edit_task, name='edit_task'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
    path('view_all_tasks/', view_all_tasks, name='view_all_tasks'),
    path('filter_tasks_by_priority/', filter_tasks_by_priority, name='filter_tasks_by_priority'),
]