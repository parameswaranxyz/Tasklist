# Generated by Django 2.0.6 on 2018-07-20 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0001_squashed_0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskentry',
            old_name='Hunter',
            new_name='User',
        ),
    ]
