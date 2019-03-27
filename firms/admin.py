from django.contrib import admin
from .models import Firm, Employee, Job

admin.site.register(Firm)
admin.site.register(Employee)
admin.site.register(Job)