from django.test import TestCase
from .models import TaskEntry


class TestForTaskEntry(TestCase):

    def test_for_set_details(self):
        test_object = TaskEntry()
        self.assertEquals(
            test_object.set_details(Task_id='a43', Task_des='dsas', Task_priority=1, Task_weight=2, Task_schedule=1, Task_dependant='NULL'),
            True)

    # def test_for_priority_value_not_greater_than_5(self):
    #     test_object = TaskEntry()
    #     self.assertEquals(
    #         test_object.set_details(Task_id='43',Task_des='dsas',Task_priority=10,Task_weight=2, Task_schedule=1),
    #         "Records Have constraint errors..")

    # def test_for_weight_value_not_greater_than_5(self):
    #     test_object = TaskEntry()
    #     self.assertEquals(
    #         test_object.set_details(Task_id='43',Task_des='dsas',Task_priority=2,Task_weight=10, Task_schedule=1),
    #         "Records Have constraint errors..")
    #
    # def test_for_schedule_value_not_greater_than_5(self):
    #     test_object = TaskEntry()
    #     self.assertEquals(
    #         test_object.set_details(Task_id='43',Task_des='dsas',Task_priority=2,Task_weight=1, Task_schedule=10),
    #         "Records Have constraint errors..")
    #
    # def test_for_primary_key_constraint_on_Task_id(self):
    #     test_object = TaskEntry()
    #     self.assertEquals(
    #         test_object.set_details(Task_id='43',Task_des='dsas',Task_priority=1,Task_weight=2, Task_schedule=1),
    #         True)
    #
    #     test_object_a = TaskEntry()
    #     self.assertFalse(
    #         test_object_a.set_details(Task_id='43', Task_des='dsas', Task_priority=1, Task_weight=2, Task_schedule=1),
    #         False)

    # def test_for_foreign_key_constraint_not_working_on_invalid_Task_id(self):
    #     test_object = TaskEntry()
    #     self.assertEquals(
    #         test_object.set_details(Task_id='43',Task_des='dsas',Task_priority=1,Task_weight=2, Task_schedule=1,
    #                                 Task_dependant='1'),
    #         False)

    # def test_for_foreign_key_constraint_working_on_valid_Task_id(self):
    #     test_object = TaskEntry()
    #     self.assertEquals(
    #         test_object.set_details(Task_id='43',Task_des='dsas',Task_priority=1,Task_weight=2, Task_schedule=1),
    #         True)
    #     self.assertEquals(
    #         test_object.set_details(Task_id='42', Task_des='dsas', Task_priority=1, Task_weight=2, Task_schedule=1,
    #                                 Task_dependant='43'),
    #         True)

    def test_for_set_details_self(self):
        test_object = TaskEntry()

        test_object.set_details(Task_id='146', Task_des='dsas', Task_priority=1, Task_weight=2, Task_schedule=1, Task_dependant='NULL')

        self.assertEquals(test_object.check_schedule(1,5), True)
        self.assertEquals(test_object.check_weight(1,5), True)
        self.assertEquals(test_object.check_priority(1,5), True)
        self.assertEquals(test_object.check_record_count(0), True)
        # self.assertEquals(test_object.check_record_count_fk(0), True)



        # self.assertEquals(test_object.save_record(), True)

    # def sample(self):
    #     test_object = TaskEntry()
    #     test_object.Task_id = ''
    #     self.assertEquals(test_object.check_record_count(0), True)

    # def test_for_check_record_coun_fk(self):
    #     test_object = TaskEntry()
    #     self.assertEquals(test_object.check_record_count_fk(0), True)
