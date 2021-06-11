from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from quickstart.models import Employee, User, Departament, Holidays, Permit, Status, UserStatus

admin.site.register(Employee)
admin.site.register(User,UserAdmin)
admin.site.register(Departament)
admin.site.register(Holidays)
admin.site.register(Permit)
admin.site.register(Status)
admin.site.register(UserStatus)
