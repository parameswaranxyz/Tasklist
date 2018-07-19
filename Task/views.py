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
                       'Task_dependant': str(each_items.Task_dependant), 'Task_schedule': each_items.Task_schedule,
                       'Task_created_on': str(each_items.Task_create)}

            all_task_list.append(jsonDic)
    else:
        all_task_list = ''

    response = {'list': all_task_list}

    return HttpResponse(content=json.dumps(response), content_type="application/json")


# get a record to edit
def get_a_task_to_edit(request):
    if request.method == 'GET':
        if not TaskEntry.objects.filter(Task_id=str(request.GET.get("Task_id"))).count() == 0:

            task = TaskEntry.objects.filter(Task_id=str(request.GET.get("Task_id")))

            for each_items in task:
                jsonDic = {'Task_id': each_items.Task_id, 'Task_des': each_items.Task_des,
                           'Task_priority': each_items.Task_priority, 'Task_weight': each_items.Task_weight,
                           'Task_dependant': str(each_items.Task_dependant), 'Task_schedule': each_items.Task_schedule
                           }

        else:
            jsonDic = {}

    return HttpResponse(json.dumps(jsonDic), content_type="application/json")


# add a record
@csrf_exempt
def add_a_record(request):
    response = {}
    if request.method == 'POST':
        new_record = TaskEntry()
        data = json.loads(request.body)
        if new_record.set_details(#Task_id=str(data.get("Task_id")),
                                  Task_des=str(data.get("Task_des")),
                                  Task_priority=int(data.get("Task_priority")),
                                  Task_weight=int(data.get("Task_weight")),
                                  Task_schedule=int(data.get("Task_schedule")),
                                  Task_dependant=str(data.get("Task_dependant"))
                                  ) == "Record Inserted":

            response['status'] = 'success'
        else:
            response['status'] = 'failed'

        return HttpResponse(json.dumps(response), content_type="application/json")
    else:
        response['status'] = 'failed'
        return HttpResponse(json.dumps(response), content_type="application/json")


# update a record
@csrf_exempt
def update_a_record(request):
    response = {}
    if request.method == 'POST':
        data = json.loads(request.body)
        if not TaskEntry.objects.filter(Task_id=data.get("Task_id")).count() == 0:

            new_record = TaskEntry()
            if new_record.update_record(Task_id=data.get("Task_id"),
                                        Task_des=str(data.get("Task_des")),
                                        Task_priority=int(data.get("Task_priority")),
                                        Task_weight=int(data.get("Task_weight")),
                                        Task_schedule=int(data.get("Task_schedule")),
                                        Task_dependant=str(data.get("Task_dependant"))
                                        ) == "Record Inserted":
                response['status'] = 'success'
            else:
                response['status'] = 'failed2'

            return HttpResponse(json.dumps(response), content_type="application/json")
        else:
            response['status'] = 'failed1'
            return HttpResponse(json.dumps(response), content_type="application/json")


# delete a record
@csrf_exempt
def delete_a_task(request):
    response = {}
    if request.method == 'POST':
        data = json.loads(request.body)
        # print(data.get("Task_id"))
        if not TaskEntry.objects.filter(Task_id=data.get("Task_id")).count() == 0:
            task = TaskEntry.objects.filter(Task_id=data.get("Task_id"))
            task.delete()
            response['status'] = 'success'
            return HttpResponse(json.dumps(response), content_type="application/json")
        else:
            response['status'] = 'failed'
            return HttpResponse(json.dumps(response),
                                content_type="application/json")


# check
def check(request):
    if 'GET' == request.method:
        response = {'list': "hai"}
    return HttpResponse(content=json.dumps(response), content_type="application/json")
