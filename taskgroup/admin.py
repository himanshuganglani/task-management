from django.contrib import admin
from .models import User
from .models import TaskModel


admin.site.register(TaskModel)
admin.site.register(User)