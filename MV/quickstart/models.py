from django.db import models
from django.contrib.auth.models import AbstractUser


class Employee(models.Model):
    objects = None
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    user_id = models.ForeignKey('UserStatus', on_delete=models.CASCADE, null=True, blank=True)
    Departament_id = models.ForeignKey('Departament', on_delete=models.DO_NOTHING, null=True, blank=True)
    active = models.BooleanField(null=True)
    create_id = models.IntegerField(null=True, blank=True)
    leave = models.IntegerField()
    manager = models.BooleanField()

    def __str__(self):
        return self.name


class User(AbstractUser):
    person = models.OneToOneField(to=Employee, null=True, blank=True, on_delete=models.DO_NOTHING)
    is_active = models.BooleanField(null=True, default=True)


class Departament(models.Model):
    objects = None
    name = models.CharField(max_length=20)
    manager_id = models.ForeignKey(to=Employee, null=True, blank=True, on_delete=models.DO_NOTHING)
    user_id = models.ForeignKey('Departament', on_delete=models.DO_NOTHING, null=True, blank=True)
    active = models.BooleanField(null=True)

    def __str__(self):
        return self.name


class Holidays(models.Model):
    objects = None
    name = models.CharField(max_length=20)
    date = models.DateField(null=True, blank=True)
    active = models.BooleanField(null=True)

    def __str__(self):
        return self.name


class Permit(models.Model):
    objects = None
    name = models.CharField(max_length=20)
    date = models.DateField(null=True, blank=True)
    employee_id = models.ForeignKey(to=Employee, on_delete=models.DO_NOTHING)
    state = models.CharField(choices=[('draft', 'Draft'), ('approved', 'Approved'), ('cancel', 'Cancel')],
                             max_length=30)

    def __str__(self):
        return self.name


class Status(models.Model):
    objects = None
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UserStatus(models.Model):
    objects = None
    user_id = models.ForeignKey(to=User, on_delete=models.DO_NOTHING, null=True, blank=True, related_name="users")
    status_id = models.ForeignKey(to=Status, on_delete=models.DO_NOTHING, null=True, blank=True)
    active = models.BooleanField(null=True)
