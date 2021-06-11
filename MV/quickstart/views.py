from tokenize import Token

from django.contrib.auth import authenticate
# from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED

# from .models import Employee, EmployeeTask
from .serializers import *

from quickstart.permissions import IsHR, IsEmployee, IsDepartamentManager
from quickstart import models, serializers


class EmployeeCreate(generics.CreateAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = EmployeeCreateSerializer
    permission_classes = [IsEmployee | IsHR]


class EmployeeList(generics.ListAPIView):

    def get_queryset(self):
        user = self.request.user.users.all().values_list('status_id__name')

        if ('HR',) in list(user):
            return self.queryset

        if ('Departamen_Manager',) in list(user):
            employee = self.request.user.employee
            manager_employee = models.Departament.objects.filter(departament_manager=employee.employee_no)
            all_employee = models.Employee.objects.filter(department__departament_no__in=manager_employee)
            return all_employee

        if ('Employee',) in list(user):
            user = self.request.user
            employee = models.Employee.objects.filter(user=user)
            return employee

    queryset = models.Employee.objects.all()
    serializer_class = EmployeeListSerializer
    permission_classes = [IsHR]


class EmployeeDetail(generics.RetrieveAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = EmployeeDetailSerializer
    permission_classes = [IsEmployee | IsHR]


class EmployeeUpdate(generics.UpdateAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = EmployeeUpdateSerializer
    permission_classes = [IsEmployee | IsHR]


class EmployeeDelete(generics.DestroyAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeDeleteSerializer
    permission_classes = [IsEmployee | IsHR]

    def delete(self, request, *args, **kwargs):
        employee = models.Employee.objects.get(id=kwargs.get('pk'))
        if not employee.active:
            return Response({'error_message': "Could not delete"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super(EmployeeDelete, self).delete(request=request, *args, **kwargs)


class UserCreate(generics.CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [IsEmployee | IsDepartamentManager | IsHR]

    def post(self, request, *args, **kwargs):
        _mutable = request.data._mutable
        request.data._mutable = True
        request.data['create_id'] = request.user.id
        request.data._mutable = _mutable

        return EmployeeCreate.create(self, request, *args, **kwargs)


class UserList(generics.ListAPIView):
    queryset = models.User.objects.all()
    serializer_class = UserListSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserDetailSerializer
    permission_classes = [IsEmployee | IsDepartamentManager | IsHR]


class UserUpdate(generics.UpdateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserUpdateSerializer
    permission_classes = [IsEmployee | IsDepartamentManager | IsHR]


class UserDelete(generics.DestroyAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserDeleteSerializer
    permission_classes = [IsEmployee | IsDepartamentManager | IsHR]

    def delete(self, request, *args, **kwargs):
        user.active = models.User.objects.get(id=kwargs.get('pk'))
        if not user.active:
            return Response({'error_message': "Could not delete"},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super(UserDelete, self).delete(request=request, *args, **kwargs)


class DepartamentCreate(generics.CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = DepartamentCreateSerializer

    def post(self, *args, **kwargs):
        return DepartamentCreate.create(self, *args, **kwargs)


class DepartamentDetail(generics.RetrieveAPIView):
    queryset = models.Departament.objects.all()
    serializer_class = serializers.DepartamentDetailSerializer


class DepartamentUpdate(generics.UpdateAPIView):
    queryset = models.User.objects.all()
    serializer_class = DepartamentUpdateSerializer


class DepartamentDelete(generics.DestroyAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.DepartamentDeleteSerializer

    def delete(self, request, *args, **kwargs):
        Departament = models.Departament.objects.get(id=kwargs.get('pk'))
        if not Departament.active:
            return Response({'error_message': "Could not delete"},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super(DepartamentDelete, self).delete(request=request, *args, **kwargs)


class HolidaysCreate(generics.CreateAPIView):
    queryset = models.Holidays.objects.all()
    serializer_class = serializers.HolidaysCreateSerializer
    permission_classes = [IsHR]


class HolidaysList(generics.ListAPIView):
    queryset = models.Holidays.objects.all()
    serializer_class = HolidaysListSerializer


class HolidaysDetail(generics.RetrieveAPIView):
    queryset = models.Holidays.objects.all()
    serializer_class = serializers.HolidaysDetailSerializer


class HolidaysUpdate(generics.UpdateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.HolidaysUpdateSerializer
    permission_classes = [IsHR]


class HolidaysDelete(generics.DestroyAPIView):
    queryset = models.Holidays.objects.all()
    serializer_class = serializers.HolidaysDeleteSerializer
    permission_classes = [IsHR]

    def delete(self, request, HolidaysDelete=None, *args, **kwargs):
        holidays = models.Holidays.objects.get(id=kwargs.get('pk'))
        if not holidays.active:
            return Response({'error_message': "Could not delete"},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super(HolidaysDelete, self).delete(request=request, *args, **kwargs)


class PermitCreate(generics.CreateAPIView):
    queryset = models.Permit.objects.all()
    serializer_class = serializers.PermitCreateSerializer
    permission_classes = [IsEmployee | IsDepartamentManager | IsHR]


class PermitList(generics.ListAPIView):
    queryset = models.Permit.objects.all()
    serializer_class = serializers.PermitListSerializer
    permission_classes = [IsEmployee | IsDepartamentManager | IsHR]


class PermitDetail(generics.RetrieveAPIView):
    queryset = models.Permit.objects.all()
    serializer_class = serializers.PermitDetailSerializer
    permission_classes = [IsEmployee | IsDepartamentManager | IsHR]


class PermitUpdate(generics.UpdateAPIView):
    queryset = models.Permit.objects.all()
    serializer_class = serializers.PermitUpdateSerializer
    permission_classes = [IsDepartamentManager | IsHR]


class PermitDelete(generics.DestroyAPIView):
    queryset = models.Permit.objects.all()
    serializer_class = serializers.PermitDeleteSerializer
    permission_classes = [IsDepartamentManager | IsHR]

    def delete(self, request, PermitDelete=None, *args, **kwargs):
        permit = models.Permit.objects.get(id=kwargs.get('pk'))
        if not permit.active:
            return Response({'error_message': "Could not delete"},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super(PermitDelete, self).delete(request=request, *args, **kwargs)


class PermitApproved(generics.UpdateAPIView):
    queryset = models.Permit.objects.all()
    serializer_class = serializers.PermitApprovedSerializer
    permission_classes = [IsDepartamentManager | IsHR]


class StatusCreate(generics.CreateAPIView):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusCreateSerializer


class StatusDetail(generics.RetrieveAPIView):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusDetailSerializer


class StatusDelete(generics.DestroyAPIView):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusDeleteSerializer

    def delete(self, request, StatusDelete=None, *args, **kwargs):
        status = models.Status.objects.get(id=kwargs.get('pk'))
        if not status.active:
            return Response({'error_message': "Could not delete"},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super(StatusDelete, self).delete(request=request, *args, **kwargs)


class UserStatusCreate(generics.CreateAPIView):
    queryset = models.UserStatus.objects.all()
    serializer_class = serializers.UserStatusCreateSerializer
    permission_classes = [IsEmployee, IsDepartamentManager, IsHR]


class UserStatusList(generics.ListAPIView):
    queryset = models.UserStatus.objects.all()
    serializer_class = serializers.UserStatusListSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name', 'last_name', 'birth_date', 'user_id', 'Departament_id']


class UserStatusDetail(generics.RetrieveAPIView):
    queryset = models.UserStatus.objects.all()
    serializer_class = serializers.UserStatusDetailSerializer
    permission_classes = [IsEmployee, IsDepartamentManager, IsHR]


class UserStatusUpdate(generics.UpdateAPIView):
    queryset = models.UserStatus.objects.all()
    serializer_class = serializers.UserStatusUpdateSerializer
    permission_classes = [IsEmployee, IsDepartamentManager, IsHR]


class UserStatusDelete(generics.DestroyAPIView):
    queryset = models.UserStatus.objects.all()
    serializer_class = serializers.UserStatusDeleteSerializer
    permission_classes = [IsAdminUser | IsHR]

    def delete(self, request, *args, **kwargs):
        userstatus = models.UserStatus.objects.get(id=kwargs.get('pk'))
        if not userstatus.active:
            return Response({'error_message': "Could not delete"},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super(UserStatusDelete, self).delete(request=request, *args, **kwargs)


@api_view(["POST"])
def log(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)
    if user:
        return Response({"error": "Login failed"}, status=HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key})
