# Generated by Django 2.0.6 on 2018-07-16 07:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0009_taskentry_task_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskentry',
            name='Task_create',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 7, 16, 7, 19, 3, 704468, tzinfo=utc)),
        ),
    ]