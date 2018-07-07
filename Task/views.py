import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import TaskEntry


# get all records
def get_task_list(request):
    if request.method == 'GET':
        all_task_list = []
        task_list = TaskEntry.objects.all()

        for each_items in task_list:
            jsonDic = {'Task_id': each_items.Task_id, 'Task_des': each_items.Task_des,
                       'Task_priority': each_items.Task_priority, 'Task_weight': each_items.Task_weight,
                       'Task_dependant': str(each_items.Task_dependant), 'Task_schedule': each_items.Task_schedule}

            all_task_list.append(jsonDic)

        print("Json response: ")
        print(all_task_list)
        print("json End")

    else:
        all_task_list = ''

    return HttpResponse(json.dumps(str(all_task_list)), content_type="application/json")


# get a record to edit
def get_a_task_to_edit(request, Task_id):
    if request.method == 'GET':
        if not TaskEntry.objects.filter(Task_id=int(Task_id)).count() == 0:

            task = TaskEntry.objects.filter(Task_id=int(Task_id))

            for each_items in task:
                jsonDic = {'Task_id': each_items.Task_id, 'Task_des': each_items.Task_des,
                           'Task_priority': each_items.Task_priority, 'Task_weight': each_items.Task_weight,
                           'Task_dependant': str(each_items.Task_dependant), 'Task_schedule': each_items.Task_schedule}

        else:
            jsonDic = {}

    return HttpResponse(json.dumps(str(jsonDic)), content_type="application/json")


# add a record
@csrf_exempt
def add_a_record(request):
    if request.method == 'POST':
        new_record = TaskEntry()
        new_record.set_details(Task_id = str(request.POST.get("Task_id")),
                               Task_des = str(request.POST.get("Task_des")),
                               Task_priority = int(request.POST.get("Task_priority")),
                               Task_weight = int(request.POST.get("Task_weight")),
                               Task_schedule = int(request.POST.get("Task_schedule")),
                               Task_dependant = str(request.POST.get("Task_dependant"))
                               )

        return HttpResponse(json.dumps(str({'status': 'success'})), content_type="application/json")
    else:
        return HttpResponse(json.dumps(str({'status': 'filed'})), content_type="application/json")


# update a record
@csrf_exempt
def update_a_record(request, Task_id):
    if request.method == 'POST':
        if not TaskEntry.objects.filter(Task_id=int(Task_id)).count() == 0:

            task = TaskEntry.objects.get(pk=int(Task_id))
            if task.set_details(Task_id = str(request.POST.get("Task_id")),
                                Task_des = str(request.POST.get("Task_des")),
                                Task_priority = int(request.POST.get("Task_priority")),
                                Task_weight = int(request.POST.get("Task_weight")),
                                Task_dependant = str(request.POST.get("Task_dependant")),
                                Task_schedule = int(request.POST.get("Task_schedule", 1))
                                   ):

                return HttpResponse(json.dumps(str({'status': 'success'})), content_type="application/json")
        else:
            return HttpResponse(json.dumps(str({'status': 'filed'})), content_type="application/json")


# delete a record
@csrf_exempt
def delete_a_task(request):
    a = request.POST.get("Task_id")
    if request.method == 'POST':
        if not TaskEntry.objects.filter(Task_id = request.POST.get("Task_id")).count() == 0:
            task = TaskEntry.objects.filter(Task_id = request.POST.get("Task_id"))
            task.delete()
            return HttpResponse(json.dumps(str({'status': 'success'})), content_type="application/json")
        else:
            return HttpResponse(json.dumps(str({'status': request.POST.get("Task_id")+a})), content_type="application/json")