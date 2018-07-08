from django.urls import path
from Task import views

urlpatterns = [
    path('api/getTaskList',views.get_task_list, name ='get all records'),
    path('api/getTask', views.get_a_task_to_edit, name='get a record to edit'),
    path('api/addTask', views.add_a_record, name='add a record'),
    path('api/updateTask', views.update_a_record, name='update a record to edit'),
    path('api/deleteTask', views.delete_a_task, name='delete a record to edit'),
]