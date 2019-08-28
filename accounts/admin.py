from django.contrib import admin

from accounts.models import Teacher, Specification, Student, User

admin.site.register(User)

admin.site.register(Student)

admin.site.register(Teacher)

admin.site.register(Specification)

