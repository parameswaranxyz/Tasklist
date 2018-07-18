# Generated by Django 2.0.6 on 2018-07-18 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0014_auto_20180716_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskentry',
            name='Task_dependant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task', to='Task.TaskEntry'),
        ),
        migrations.AlterField(
            model_name='taskentry',
            name='Task_id',
            field=models.CharField(error_messages={'incomplete': 'Enter a country calling code and a phone number.'}, max_length=30, primary_key=True, serialize=False),
        ),
    ]