from rest_framework import serializers


from quickstart import models


class EmployeeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        exclude = {'create_id': {'read_only': True}}


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
        exclude = {'create_id': {'read_only': True}}


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
        exclude = {'create_id': {'read_only': True}}


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
        exclude = {'create_id': {'read_only': True}}


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
        exclude = {'create_id': {'read_only': True}}


class PermitDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Permit
        fields = '__all__'


class PermitUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Permit
        fields = '__all__'


class PermitListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Permit
        fields = '__all__'


class PermitDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Permit
        fields = '__all__'


class StatusCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Status
        exclude = {'create_id': {'read_only': True}}


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
        exclude = {'create_id': {'read_only': True}}


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
