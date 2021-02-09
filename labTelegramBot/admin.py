from django.contrib import admin
from .models import Lab, Student


class LabAdmin(admin.ModelAdmin):
    list_display = ('labId', 'studentId', 'labNum', 'filePath', 'status', 'messageId')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('studentId', 'fullName', 'groupNum', 'nickname', 'chatId')


admin.site.register(Lab, LabAdmin)
admin.site.register(Student, StudentAdmin)
