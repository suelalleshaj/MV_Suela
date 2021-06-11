from asyncio.windows_events import NULL
from tokenize import Token
from django.contrib.auth import authenticate
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from django.views.decorators.csrf import csrf_exempt

from .serializers import *
from quickstart.permissions import IsHR, IsEmployee, IsDepartamentManager
from quickstart import models, serializers

from rest_pandas.renderers import PandasExcelRenderer
from rest_pandas import PandasView
import pandas


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
    serializer_class = EmployeeDetailSerializer
    permission_classes = [IsEmployee | IsHR]


class EmployeeUpdate(generics.UpdateAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = EmployeeUpdateSerializer
    permission_classes = [IsEmployee | IsDepartamentManager | IsHR]


class EmployeeDelete(generics.DestroyAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeDeleteSerializer
    permission_classes = [IsEmployee | IsHR]


class UserCreate(generics.CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [IsEmployee | IsDepartamentManager | IsHR]

    def post(self, request, *args, **kwargs):
        _mutable = request.data._mutable
        request.data._mutable = True
        request.data['create_id'] = request.user.id
        request.data._mutable = _mutable

        return UserCreate.create(self, request, *args, **kwargs)


class UserList(generics.ListAPIView):
    queryset = models.User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsHR]

class UserDetail(generics.RetrieveAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserDetailSerializer
    permission_classes = [IsEmployee | IsDepartamentManager | IsHR]


class UserUpdate(generics.UpdateAPIView):

    def get_queryset(self):
        user = self.request.user.users.all().values_list('status_id__name')

        if ('HR',) in list(user):
            return self.queryset

        if ('Departamen_Manager',) in list(user):
            employee = self.request.user.employee
            manager_employee = models.Departament.objects.filter(departament_manager=employee.employee_no)
            all_employee = models.Employee.objects.filter(department__departament_no__in=manager_employee)
            return all_employee

    queryset = models.User.objects.all()
    serializer_class = serializers.UserUpdateSerializer
    permission_classes = [IsEmployee | IsDepartamentManager | IsHR]


class UserDelete(generics.DestroyAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserDeleteSerializer
    permission_classes = [IsEmployee | IsDepartamentManager | IsHR]


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


class HolidaysCreate(generics.CreateAPIView):
    queryset = models.Holidays.objects.all()
    serializer_class = serializers.HolidaysCreateSerializer
    permission_classes = [IsHR]


def post(self, HolidayCreate=None, *args, **kwargs):
    return HolidayCreate.create(self, *args, **kwargs)


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


class PermitCreate(generics.CreateAPIView):

    def get_queryset(self):

        user = self.request.user.users.all().values_list('role__role_name')
        x = list(user)
        print(x)

        if ('HR',) in list(user):
            return self.queryset.all()

        if ('Departamen_Manager',) in list(user):
            employee = self.request.user.employee
            manager_employee = models.Departament.objects.filter(departament_manager=employee.employee_no)
            all_employee = models.Employee.objects.filter(department__departament_no__in=manager_employee)
            return all_employee

    queryset = models.Permit.objects.all()
    serializer_class = serializers.PermitCreateSerializer
    permission_classes = [IsEmployee | IsDepartamentManager | IsHR]


class PermitList(generics.ListAPIView):

    def get_queryset(self):

        user = self.request.user.users.all().values_list('role__role_name')
        x = list(user)
        print(x)

        if ('HR',) in list(user):
            return self.queryset.all()

        if ('Departamen_Manager',) in list(user):
            employee = self.request.user.employee
            manager_employee = models.Departament.objects.filter(departament_manager=employee.employee_no)
            all_employee = models.Employee.objects.filter(department__departament_no__in=manager_employee)
            return all_employee

    queryset = models.Permit.objects.all()
    serializer_class = serializers.PermitListSerializer
    permission_classes = [IsEmployee | IsDepartamentManager | IsHR]


class PermitDetail(generics.RetrieveAPIView):

    def get_queryset(self):

        user = self.request.user.users.all().values_list('role__role_name')
        x = list(user)
        print(x)

        if ('HR',) in list(user):
            return self.queryset.all()

        if ('Departamen_Manager',) in list(user):
            employee = self.request.user.employee
            manager_employee = models.Departament.objects.filter(departament_manager=employee.employee_no)
            all_employee = models.Employee.objects.filter(department__departament_no__in=manager_employee)
            return all_employee

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


class PermitApproved(generics.UpdateAPIView):
    queryset = models.Permit.objects.all()
    serializer_class = serializers.PermitApprovedSerializer
    permission_classes = [IsDepartamentManager | IsHR]

    def put(self, PermitCreate=None, *args, **kwargs):
        if self.request.data.status == 'approved':
            if self.request.data.holiday == NULL:
                self.request.data.employee.leave -= (self.request.start - self.request.end) * 8

        return PermitCreate.update(self, *args, **kwargs)


class PermitView(PandasView):
    permission_classes = [IsHR | IsDepartamentManager]

    def get_queryset(self):
        user = self.request.user.users.all().values_list('status_id__name')
        x = list(user)
        print(x)

        if ('HR',) in list(user):
            return self.queryset.all()

        if ('Departament_Manager',) in list(user):
            emp = self.request.user.employee
            manager_employee = models.Departament.objects.filter(dept_manager=emp.emp_no)
            all_emp = models.Employee.objects.filter(department__dept_no__in=manager_employee)
            leave = models.Permit.objects.filter(employee__emp_no__in=all_emp)
            return leave

    queryset = models.Permit.objects.all()

    serializer_class = serializers.PermitListSerializer

    renderer_classes = [PandasExcelRenderer]

    def get_pandas_filename(self, request, format):
        if format in ('xls', 'xlsx'):
            return "Leave Report"
        else:
            return None

class StatusCreate(generics.CreateAPIView):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusCreateSerializer


class StatusDetail(generics.RetrieveAPIView):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusDetailSerializer


class StatusDelete(generics.DestroyAPIView):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusDeleteSerializer


class UserStatusCreate(generics.CreateAPIView):

    def get_queryset(self):

        user = self.request.user.users.all().values_list('role__role_name')
        x = list(user)
        print(x)

        if ('HR',) in list(user):
            return self.queryset.all()

        if ('Departamen_Manager',) in list(user):
            employee = self.request.user.employee
            manager_employee = models.Departament.objects.filter(departament_manager=employee.employee_no)
            all_employee = models.Employee.objects.filter(department__departament_no__in=manager_employee)
            return all_employee

        if ('Employee',) in list(user):
            user = self.request.user
            employee = models.Employee.objects.filter(user=user)
            return employee

    queryset = models.UserStatus.objects.all()
    serializer_class = serializers.UserStatusCreateSerializer
    permission_classes = [IsEmployee, IsDepartamentManager, IsHR]


class UserStatusList(generics.ListAPIView):

    def get_queryset(self):

        user = self.request.user.users.all().values_list('role__role_name')
        x = list(user)
        print(x)

        if ('HR',) in list(user):
            return self.queryset.all()

        if ('Departamen_Manager',) in list(user):
            employee = self.request.user.employee
            manager_employee = models.Departament.objects.filter(departament_manager=employee.employee_no)
            all_employee = models.Employee.objects.filter(department__departament_no__in=manager_employee)
            return all_employee

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


@csrf_exempt
@api_view(["POST"])
def log(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)
    if user:
        return Response({"error": "Login failed"}, status=HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key})
