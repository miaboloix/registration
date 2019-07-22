

from django.contrib import admin

from .models import Choice, Question, Student, Course, Meeting

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Meeting)