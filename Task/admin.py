from django.contrib import admin

# Register your models here.
from Task.models import TaskEntry

admin.site.register(TaskEntry)