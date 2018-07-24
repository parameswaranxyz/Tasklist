import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib import auth

# get all records
from Task.models import TaskEntry
from .tree_view import Node, Tree
from operator import attrgetter

from django.contrib.auth.decorators import login_required


@csrf_exempt
def user_auth(request):
    response = {}
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data['username'], data['password'], data)
        try:
            user = User.objects.get(username=data['username'])
            response['status'] = 'failed'
        except User.DoesNotExist:
            User.objects.create_user(data['username'], password=data['password'])
            response['status'] = 'success'
    else:
        response['status'] = 'failed'
    return HttpResponse(content=json.dumps(response), content_type="application/json")


@csrf_exempt
def login(request):
    response = {}
    if request.method == 'POST':
        data = json.loads(request.body)
        user = auth.authenticate(username=data['username'], password=data['password'])
        if user is not None:
            auth.login(request, user)
            response['status'] = 'success'
        else:
            response['status'] = 'failed'
    else:
        response['status'] = 'failed'
    return HttpResponse(content=json.dumps(response), content_type="application/json")


@csrf_exempt
def logout(request):
    response = {}
    if request.method == 'POST':
        auth.logout(request)
        response['status'] = 'success'
    else:
        response['status'] = 'failed'
    return HttpResponse(content=json.dumps(response), content_type="application/json")


# @login_required
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


def get_task_list_as_tree(request):
    # Parent search(root,new):
    #         If new_depen == None:
    #                 Return root                    // insert // root.child  = new_node
    #         Else if root_id == new_dep:
    #                 Return root                     // insert // root.child.ap(new_node)
    #         Else if root.child.len>0:
    #                 For i in root.child:
    #                         Parent search(I,new)

    if request.method == 'GET':
        task_list = TaskEntry.objects.all()
        tree = Tree()

        task_list = sorted(task_list, key=attrgetter('Task_id'))

        for each_items in task_list:
            new_node = Node(each_items)
            print(new_node.data.Task_id, new_node.data.Task_dependant_id)
            tree.insert_child(tree.Root, new_node)

    response = {'list': tree.print_tree(tree.Root)}

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
        if new_record.set_details(  # Task_id=str(data.get("Task_id")),
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


'''{ None None  None}
[{   2 None dsadnasina 2018-07-20 07:46:14.876368+00:00  }[{11 2 check 2018-07-22 19:23:18.845614+00:00}]
{4 None Task A 2018-07-22 17:07:38.180790+00:00}
[{5 4 TaskB 2018-07-22 17:07:52.857980+00:00}[
 {6 5 Taskc 2018-07-22 17:08:12.935603+00:00}[{7 6 Task D 2018-07-22 17:08:38.587325+00:00}]
{8 5 Task 1 2018-07-22 17:08:54.666120+00:00}{9 5 Task 2 2018-07-22 17:09:18.497849+00:00}
        [{10 9 Task 3 2018-07-22 17:09:37.744749+00:00}]
        ]
]
]
[]
[]'''
