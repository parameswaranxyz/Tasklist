# Generated by Django 2.0.6 on 2018-07-07 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskentry',
            name='Task_dependant',
            field=models.ForeignKey(default='NULL', on_delete=django.db.models.deletion.CASCADE, to='Task.TaskEntry'),
        ),
    ]