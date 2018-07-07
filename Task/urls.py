from django.urls import path
from Task import views

urlpatterns = [
    path('api/add', views.add_a_record, name='add'),
    path('api/getTaskList',views.get_task_list, name ='get all records'),
    path('api/getTask/<int:Task_id>/', views.get_a_task_to_edit, name='get a record to edit'),
    # path('api/deleteTask/<int:Task_id>/', views.delete_a_task, name='delete a record to edit'),
    path('api/deleteTask/', views.delete_a_task, name='delete a record to edit'),
]