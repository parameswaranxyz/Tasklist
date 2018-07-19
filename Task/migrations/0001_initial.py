# Generated by Django 2.0.6 on 2018-07-18 11:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskEntry',
            fields=[
                ('Task_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Task_des', models.CharField(max_length=200)),
                ('Task_priority', models.PositiveIntegerField(default=1, error_messages={'incomplete': 'Enter a country calling code and a phone number.'}, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('Task_weight', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('Task_schedule', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('Task_create', models.DateTimeField(auto_now_add=True)),
                ('Task_dependant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Task.TaskEntry')),
            ],
        ),
    ]
