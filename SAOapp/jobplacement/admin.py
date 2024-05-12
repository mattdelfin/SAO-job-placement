from django.contrib import admin
from .models import JobPlacementAdminUser, StudentUser
# Register your models here.


admin.site.register(JobPlacementAdminUser)
admin.site.register(StudentUser)