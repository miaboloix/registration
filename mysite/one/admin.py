

from django.contrib import admin

from .models import Choice, Question, StudentUser, Course, Meeting

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(StudentUser)
admin.site.register(Course)
admin.site.register(Meeting)