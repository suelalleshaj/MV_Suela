from rest_framework import serializers

from quickstart import models


class EmployeeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = '__all__'


class EmployeeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = '__all__'


class EmployeeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = '__all__'


class EmployeeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = '__all__'


class EmployeeDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class DepartamentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Departament
        fields = '__all__'


class DepartamentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Departament
        fields = '__all__'


class DepartamentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Departament
        fields = '__all__'


class DepartamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Departament
        fields = '__all__'


class DepartamentDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Departament
        fields = '__all__'


class HolidaysCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Holidays
        fields = '__all__'


class HolidaysDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Holidays
        fields = '__all__'


class HolidaysUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Holidays
        fields = '__all__'


class HolidaysListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Holidays
        fields = '__all__'


class HolidaysDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Holidays
        fields = '__all__'


class PermitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Permit
        fields = ['name', 'date', 'employee_id']


class PermitDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Permit
        fields = '__all__'


class PermitUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Permit
        fields = ['name', 'date', 'employee_id']


class PermitListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Permit
        fields = '__all__'


class PermitDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Permit
        fields = ['name', 'date', 'employee_id']


class PermitApprovedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Permit
        fields = '__all__'


class StatusCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Status
        fields = '__all__'


class StatusDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Status
        fields = '__all__'


class StatusDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Status
        fields = '__all__'


class UserStatusCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserStatus
        fields = '__all__'


class UserStatusListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserStatus
        fields = '__all__'


class UserStatusDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserStatus
        fields = '__all__'


class UserStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserStatus
        fields = '__all__'


class UserStatusDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserStatus
        fields = '__all__'
