from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User


class TaskEntry(models.Model):

    # id = models.AutoField(primary_key=True)

    Task_id = models.AutoField(auto_created=True, primary_key=True)
    Task_des = models.CharField(max_length=200)
    Task_priority = models.PositiveIntegerField(default=1,
                                                validators=[MinValueValidator(1), MaxValueValidator(5)],
                                                error_messages={
                                                    'incomplete': 'Enter a country calling code and a phone number.'})
    Task_weight = models.PositiveIntegerField(default=1,
                                              validators=[MinValueValidator(1), MaxValueValidator(5)])
    Task_dependant = models.ForeignKey('self', on_delete=models.CASCADE, null=True,blank=True)
    Task_schedule = models.PositiveIntegerField(default=1,
                                                validators=[MinValueValidator(1), MaxValueValidator(5)])

    Task_create = models.DateTimeField(auto_now_add=True,blank=True)

    User = models.ForeignKey(User,on_delete=models.CASCADE)

    MINIMUM_RANGE = 1
    MAXIMUM_RANGE = 5
    RECORD_COUNT_ZERO = 0

    def __str(self):
        return self.name

    # def set_details(self, Task_id, Task_des, Task_priority, Task_weight, Task_schedule, Task_dependant):
    def set_details(self, Task_des, Task_priority, Task_weight, Task_schedule, Task_dependant):
        # self.Task_id = Task_id
        self.Task_des = Task_des
        self.Task_priority = Task_priority
        self.Task_weight = Task_weight
        self.Task_schedule = Task_schedule

        # print("Date and time", datetime.datetime.now(pytz.timezone('Asia/Kolkata')))
        if not Task_dependant == 'NULL':
            if self.check_record_count_fk(Task_dependant):
                self.Task_dependant_id = Task_dependant
            else:
                return "Records Have constraint errors"

        # if self.check_record_count() \
        if self.check_priority() \
            and self.check_weight() \
            and self.check_schedule():

            try:
                self.save()
            except Exception as e:
                return "Records Have constraint errors"

            return "Record Inserted"
        else:
            return "Records Have constraint errors"

    def check_record_count(self):
        if TaskEntry.objects.filter(pk=self.Task_id).count() == self.RECORD_COUNT_ZERO:
            return True
        else:
            return False

    def check_record_count_fk(self, Task_dependant):

        if TaskEntry.objects.filter(pk=Task_dependant).count() == self.RECORD_COUNT_ZERO:
            return False

        return True

    def check_weight(self):
        if self.Task_weight > self.MAXIMUM_RANGE or self.Task_weight < self.MINIMUM_RANGE:
            return False
        return True

    def check_priority(self):
        if self.Task_priority > self.MAXIMUM_RANGE or self.Task_priority < self.MINIMUM_RANGE:
            return False
        return True

    def check_schedule(self):
        if self.Task_schedule > self.MAXIMUM_RANGE or self.Task_schedule < self.MINIMUM_RANGE:
            return False
        return True

    def update_record(self, Task_id, Task_des, Task_priority, Task_weight, Task_schedule, Task_dependant):

        self.Task_id = Task_id
        self.Task_des = Task_des
        self.Task_priority = Task_priority
        self.Task_weight = Task_weight
        self.Task_schedule = Task_schedule

        if not Task_dependant == 'NULL':
            if self.check_record_count_fk(Task_dependant):
                self.Task_dependant_id = Task_dependant
            else:
                return "Records Have constraint errors1"

        if self.check_priority() \
                and self.check_weight() \
                and self.check_schedule():

            try:

                if Task_dependant == 'NULL':
                    TaskEntry.objects.filter(pk=self.Task_id).update(
                        Task_des=self.Task_des,
                        Task_priority=self.Task_priority,
                        Task_weight=self.Task_weight,
                        Task_schedule=self.Task_schedule,
                        Task_dependant_id=None
                    )
                else:
                    TaskEntry.objects.filter(pk=self.Task_id).update(
                        Task_des=self.Task_des,
                        Task_priority=self.Task_priority,
                        Task_weight=self.Task_weight,
                        Task_schedule=self.Task_schedule,
                        Task_dependant_id=self.Task_dependant
                    )
            except Exception as e:
                return "Records Have constraint errors2" + str(e)

            return "Record Inserted"
        else:
            return "Records Have constraint errors3"