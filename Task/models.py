from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class TaskEntry(models.Model):
    Task_id = models.CharField(max_length=30,
                               error_messages={'incomplete': 'Enter a country calling code and a phone number.'},
                               primary_key=True)

    Task_des = models.CharField(max_length=200)

    Task_priority = models.PositiveIntegerField(default=1,
                                                validators=[MinValueValidator(1), MaxValueValidator(5)],
                                                error_messages={
                                                    'incomplete': 'Enter a country calling code and a phone number.'})

    Task_weight = models.PositiveIntegerField(default=1,
                                              validators=[MinValueValidator(1), MaxValueValidator(5)])

    Task_dependant = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    Task_schedule = models.PositiveIntegerField(default=1,
                                                validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str(self):
        return self.name

    def set_details(self, Task_id, Task_des, Task_priority, Task_weight, Task_schedule, Task_dependant):
        self.Task_id = Task_id
        self.Task_des = Task_des
        self.Task_priority = Task_priority
        self.Task_weight = Task_weight
        if not Task_dependant == 'NULL':
            self.Task_dependant = Task_dependant
        self.Task_schedule = Task_schedule

        if not self.save_record():
            return "Records Have constraint errors.."

        return True

    def check_record_count(self, record_count_zero):
        if TaskEntry.objects.filter(pk=self.Task_id).count() == record_count_zero:
            return True
        else:
            return False

    def check_record_count_fk(self, record_count_zero):
        if self.Task_dependant is None:
            return True

        if TaskEntry.objects.filter(pk=self.Task_dependant).count() == record_count_zero:
            return False

        return True

    def check_weight(self, mininum_range, maximun_range):
        if self.Task_weight > maximun_range or self.Task_weight < mininum_range:
            return False
        return True

    def check_priority(self, mininum_range, maximun_range):
        if self.Task_priority > maximun_range or self.Task_priority < mininum_range:
            return False
        return True

    def check_schedule(self, mininum_range, maximun_range):
        if self.Task_schedule > maximun_range or self.Task_schedule < mininum_range:
            return False
        return True

    def save_record(self):

        mininum_range = 1
        maximun_range = 5
        record_count_zero = 0

        # self.check_record_count_fk(
        #                 record_count_zero) and

        if self.check_record_count(record_count_zero) and self.check_priority(mininum_range,
                                                                              maximun_range) and self.check_weight(
                mininum_range, maximun_range) and self.check_schedule(mininum_range,
                                                                      maximun_range) and self.check_record_count_fk(
            record_count_zero):

            self.save()
            return True
        else:
            return False