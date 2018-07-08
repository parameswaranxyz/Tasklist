from django.test import TestCase
from .models import TaskEntry


class TestForTaskEntry(TestCase):

    def test_for_set_details(self):
        test_object = TaskEntry()
        self.assertEquals(
            test_object.set_details(Task_id='a43', Task_des='dsas', Task_priority=1, Task_weight=2, Task_schedule=1,
                                    Task_dependant='NULL'),
            "Record Inserted")

    def test_for_update_details(self):
        test_object = TaskEntry()
        self.assertEquals(
            test_object.update_record(Task_id='a43', Task_des='dsas', Task_priority=1, Task_weight=2, Task_schedule=1,
                                      Task_dependant='NULL'),
            "Record Inserted")

    def test_for_priority_value_not_greater_than_5(self):
        test_object = TaskEntry()
        self.assertEquals(
            test_object.set_details(Task_id='43', Task_des='dsas', Task_priority=10, Task_weight=2, Task_schedule=1,
                                    Task_dependant='NULL'),
            "Records Have constraint errors")

    def test_for_weight_value_not_greater_than_5(self):
        test_object = TaskEntry()
        self.assertEquals(
            test_object.set_details(Task_id='43', Task_des='dsas', Task_priority=1, Task_weight=6, Task_schedule=1,
                                    Task_dependant='NULL'),
            "Records Have constraint errors")

    def test_for_schedule_value_not_greater_than_5(self):
        test_object = TaskEntry()
        self.assertEquals(
            test_object.set_details(Task_id='43', Task_des='dsas', Task_priority=1, Task_weight=6, Task_schedule=1,
                                    Task_dependant='NULL'),
            "Records Have constraint errors")

    def test_for_primary_key_constraint_on_Task_id(self):
        test_object = TaskEntry()
        self.assertEquals(
            test_object.set_details(Task_id='43', Task_des='dsas', Task_priority=1, Task_weight=3, Task_schedule=1,
                                    Task_dependant='NULL'),
            "Record Inserted")
        self.assertEquals(
            test_object.set_details(Task_id='43', Task_des='dsas', Task_priority=1, Task_weight=3, Task_schedule=1,
                                    Task_dependant='NULL'),
            "Records Have constraint errors")

    def test_for_foreign_key_constraint_not_working_on_invalid_Task_id(self):
        test_object = TaskEntry()
        self.assertEquals(
            test_object.set_details(Task_id='43', Task_des='dsas', Task_priority=1, Task_weight=6, Task_schedule=1,
                                    Task_dependant='NULL'),
            "Records Have constraint errors")

    def test_for_foreign_key_constraint_working_on_valid_Task_id(self):
        test_object = TaskEntry()
        test_object.set_details(Task_id='43', Task_des='dsas', Task_priority=1, Task_weight=3, Task_schedule=1,
                                Task_dependant='NULL')
        self.assertEquals(
            test_object.set_details(Task_id='54', Task_des='dsas', Task_priority=1, Task_weight=3, Task_schedule=1,
                                    Task_dependant='43'),
            "Record Inserted")

    def test_for_foreign_key_constraint_should_not_working_on_invalid_Task_id(self):
        test_object = TaskEntry()
        self.assertEquals(
            test_object.set_details(Task_id='43', Task_des='dsas', Task_priority=1, Task_weight=3, Task_schedule=1,
                                    Task_dependant='4'),
            "Records Have constraint errors")

    # REST END POINT checking

    def test_get_list(self):
        test_object = TaskEntry()
        test_object.set_details(Task_id='43', Task_des='dsas', Task_priority=1, Task_weight=2, Task_schedule=1,
                                Task_dependant='NULL')

        response = self.client.get('/api/getTaskList')
        self.assertJSONEqual(response.content, {
            "list": "[{'Task_id': '43', 'Task_des': 'dsas', 'Task_priority': 1, 'Task_weight': 2, 'Task_dependant': "
                    "'None', 'Task_schedule': 1}]"})

    def test_get_a_record(self):
        test_object = TaskEntry()
        test_object.set_details(Task_id='43', Task_des='dsas', Task_priority=1, Task_weight=2, Task_schedule=1,
                                Task_dependant='NULL')
        test_object.set_details(Task_id='4', Task_des='dsas', Task_priority=1, Task_weight=2, Task_schedule=1,
                                Task_dependant='NULL')
        test_object.set_details(Task_id='5', Task_des='dsas', Task_priority=1, Task_weight=2, Task_schedule=1,
                                Task_dependant='NULL')

        response = self.client.get('/api/getTask', {'Task_id': '43'})
        self.assertJSONEqual(response.content,
                             {'Task_id': '43', 'Task_des': 'dsas', 'Task_priority': 1, 'Task_weight': 2,
                              'Task_dependant': 'None',
                              'Task_schedule': 1})

    def test_add_task(self):
        response = self.client.post('/api/addTask',
                                    {'Task_id': '43', 'Task_des': 'dsas', 'Task_priority': 1, 'Task_weight': 2,
                                     'Task_dependant': 'NULL', 'Task_schedule': 1})
        self.assertJSONEqual(response.content, {'status': 'success'})
        response = self.client.get('/api/getTask', {'Task_id': '43'})
        self.assertJSONEqual(response.content,
                             {'Task_id': '43', 'Task_des': 'dsas', 'Task_priority': 1, 'Task_weight': 2,
                              'Task_dependant': 'None',
                              'Task_schedule': 1})

    def test_update_task(self):
        test_object = TaskEntry()
        test_object.set_details(Task_id='43', Task_des='dsas', Task_priority=1, Task_weight=2, Task_schedule=1,
                                Task_dependant='NULL')

        response = self.client.post('/api/updateTask',
                                    {'Task_id': '43', 'Task_des': 'personal', 'Task_priority': 1, 'Task_weight': 2,
                                     'Task_dependant': 'NULL', 'Task_schedule': 1})
        self.assertJSONEqual(response.content, {'status': 'success'})

        response = self.client.get('/api/getTask', {'Task_id': '43'})
        self.assertJSONEqual(response.content,
                             {'Task_id': '43', 'Task_des': 'personal', 'Task_priority': 1, 'Task_weight': 2,
                              'Task_dependant': 'None',
                              'Task_schedule': 1})

    def test_update_task_which_have_dependant(self):
        test_object = TaskEntry()
        test_object.set_details(Task_id='4', Task_des='dsas', Task_priority=1, Task_weight=2, Task_schedule=1,
                                Task_dependant='NULL')

        test_object = TaskEntry()
        test_object.set_details(Task_id='5', Task_des='dsas', Task_priority=1, Task_weight=2, Task_schedule=1,
                                Task_dependant='NULL')

        test_object = TaskEntry()
        test_object.set_details(Task_id='43', Task_des='dsas', Task_priority=1, Task_weight=2, Task_schedule=1,
                                Task_dependant='4')

        response = self.client.post('/api/updateTask',
                                    {'Task_id': '43', 'Task_des': 'personal', 'Task_priority': 1, 'Task_weight': 2,
                                     'Task_dependant': '5', 'Task_schedule': 1})
        self.assertJSONEqual(response.content, {'status': 'success'})

        response = self.client.get('/api/getTask', {'Task_id': '43'})
        self.assertJSONEqual(response.content,
                             {'Task_id': '43', 'Task_des': 'personal', 'Task_priority': 1, 'Task_weight': 2,
                              'Task_dependant': 'TaskEntry object (5)',
                              'Task_schedule': 1})

    def test_delete_task(self):
        test_object = TaskEntry()
        test_object.set_details(Task_id='43', Task_des='dsas', Task_priority=1, Task_weight=2, Task_schedule=1,
                                Task_dependant='NULL')

        response = self.client.post('/api/deleteTask',
                                    {'Task_id': '43'})
        self.assertJSONEqual(response.content, {'status': 'success'})
        response = self.client.get('/api/getTask', {'Task_id': '43'})
        self.assertJSONEqual(response.content, {})

    def test_delete_task_for_invalid_id(self):
        response = self.client.post('/api/deleteTask',
                                    {'Task_id': '43'})
        self.assertJSONEqual(response.content, {'status': 'failed'})
