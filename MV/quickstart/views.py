from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .serializers import *

from quickstart.permissions import IsHR, IsEmployee
from quickstart import models, serializers

from .models import Employee, Departament, UserStatus


class EmployeeCreate(generics.CreateAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = EmployeeDetailSerializer
    permission_classes = [IsAdminUser | IsHR]

    def post(self, request, *args, **kwargs):
        _mutable = request.data._mutable
        request.data._mutable = True
        request.data['create_id'] = request.user.id
        request.data._mutable = _mutable

        return EmployeeCreate.create(self, request, *args, **kwargs)


class EmployeeList(generics.ListAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = EmployeeDetailSerializer
    # filter_backends = [DjangoFilterBackend]
    # filter_fields = ['name', 'last_name', 'birth_date', 'user_id', 'Departament_id']

    def get_queryset(self):

        user_status = self.request.user.userstatus_set.all().values_list('status_id_name')

        if 'HR' in user_status:
            return self.queryset
        if 'Departament Manager' in user_status:
            return self.queryset.filter(Departament_id=Employee.objects.get(user_id=self.request.user).Departament_id)
        if 'Employee' in user_status:
            return self.queryset.filter(id=self.request.user.id)

class EmployeeDetail(generics.RetrieveAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = EmployeeDetailSerializer
    permission_classes = [IsHR]


class EmployeeUpdate(generics.UpdateAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = EmployeeDetailSerializer
    permission_classes = [IsHR]


class EmployeeDelete(generics.DestroyAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeDetailSerializer
    permission_classes = [IsAdminUser | IsHR]

    def delete(self, request, *args, **kwargs):
        employee = models.Employee.objects.get(id=kwargs.get('pk'))
        if not employee.active:
            return Response({'error_message': "Could not delete"},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super(EmployeeDelete, self).delete(request=request, *args, **kwargs)


class UserCreate(generics.CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAdminUser | IsHR]

    def post(self, request, *args, **kwargs):
        _mutable = request.data._mutable
        request.data._mutable = True
        request.data['create_id'] = request.user.id
        request.data._mutable = _mutable

        return EmployeeCreate.create(self, request, *args, **kwargs)


class UserList(generics.ListAPIView):
    queryset = models.User.objects.all()
    serializer_class = UserDetailSerializer
    # filter_backends = [DjangoFilterBackend]
    # filter_fields = ['name', 'last_name', 'birth_date', 'user_id', 'Departament_id']


# def get_queryset(self):
#    queryset = models.

class UserDetail(generics.RetrieveAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserDetailSerializer
    permission_classes = [IsAdminUser | IsHR]


class UserUpdate(generics.UpdateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserDetailSerializer
    permission_classes = [IsAdminUser | IsHR]


class UserDelete(generics.DestroyAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserDetailSerializer
    permission_classes = [IsAdminUser | IsHR]

    # def delete(self, request, *args, **kwargs):
    #   user = models.User.objects.get(id=kwargs.get('pk'))
    #  if not user.active:
    #     return Response({'error_message': "Could not delete"},
    #                    status=status.HTTP_405_METHOD_NOT_ALLOWED)
    # return super(UserDelete, self).delete(request=request, *args, **kwargs)


class DepartamentCreate(generics.CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = DepartamentDetailSerializer

    def post(self, *args, **kwargs):
        return DepartamentCreate.create(self, *args, **kwargs)


class DepartamentDetail(generics.RetrieveAPIView):
    queryset = models.Departament.objects.all()
    serializer_class = serializers.DepartamentDetailSerializer


class DepartamentUpdate(generics.UpdateAPIView):
    queryset = models.User.objects.all()
    serializer_class = DepartamentDetailSerializer


class DepartamentDelete(generics.DestroyAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.DepartamentDetailSerializer

    def delete(self, request, *args, **kwargs):
        Departament = models.Departament.objects.get(id=kwargs.get('pk'))
        if not Departament.active:
            return Response({'error_message': "Could not delete"},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super(DepartamentDelete, self).delete(request=request, *args, **kwargs)


class HolidaysCreate(generics.CreateAPIView):
    queryset = models.Holidays.objects.all()
    serializer_class = serializers.HolidaysDetailSerializer

    def post(self, HolidaysCreate=None, *args, **kwargs):
        return HolidaysCreate.create(self, *args, **kwargs)


class HolidaysList(generics.RetrieveAPIView):
    queryset = models.Holidays.objects.all()
    serializer_class = HolidaysDetailSerializer


class HolidaysDetail(generics.RetrieveAPIView):
    queryset = models.Holidays.objects.all()
    serializer_class = serializers.HolidaysDetailSerializer


class HolidaysUpdate(generics.UpdateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.HolidaysDetailSerializer


class HolidaysDelete(generics.DestroyAPIView):
    queryset = models.Holidays.objects.all()
    serializer_class = serializers.HolidaysDetailSerializer

    def delete(self, request, HolidaysDelete=None, *args, **kwargs):
        holidays = models.Holidays.objects.get(id=kwargs.get('pk'))
        if not holidays.active:
            return Response({'error_message': "Could not delete"},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super(HolidaysDelete, self).delete(request=request, *args, **kwargs)


class PermitCreate(generics.CreateAPIView):
    queryset = models.Permit.objects.all()
    serializer_class = serializers.PermitDetailSerializer

    def post(self, PermitCreate=None, *args, **kwargs):
        return PermitCreate.create(self, *args, **kwargs)


class PermitList(generics.RetrieveAPIView):
    queryset = models.Permit.objects.all()
    serializer_class = serializers.PermitDetailSerializer


class PermitDetail(generics.RetrieveAPIView):
    queryset = models.Permit.objects.all()
    serializer_class = serializers.PermitDetailSerializer


class PermitUpdate(generics.UpdateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.PermitDetailSerializer


class PermitDelete(generics.DestroyAPIView):
    queryset = models.Permit.objects.all()
    serializer_class = serializers.PermitDetailSerializer

    def delete(self, request, PermitDelete=None, *args, **kwargs):
        permit = models.Permit.objects.get(id=kwargs.get('pk'))
        if not permit.active:
            return Response({'error_message': "Could not delete"},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super(PermitDelete, self).delete(request=request, *args, **kwargs)


class StatusCreate(generics.CreateAPIView):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusDetailSerializer

    def post(self, PermitCreate=None, *args, **kwargs):
        return PermitCreate.create(self, *args, **kwargs)


class StatusDetail(generics.RetrieveAPIView):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusDetailSerializer


class StatusDelete(generics.DestroyAPIView):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusDetailSerializer

    def delete(self, request, StatusDelete=None, *args, **kwargs):
        status = models.Status.objects.get(id=kwargs.get('pk'))
        if not status.active:
            return Response({'error_message': "Could not delete"},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super(StatusDelete, self).delete(request=request, *args, **kwargs)


class UserStatusCreate(generics.CreateAPIView):
    queryset = models.UserStatus.objects.all()
    serializer_class = serializers.UserStatusDetailSerializer
    permission_classes = [IsAdminUser | IsHR]

    def post(self, request, *args, **kwargs):
        return UserStatusCreate.create(self, request, *args, **kwargs)


class UserStatusList(generics.ListAPIView):
    queryset = models.UserStatus.objects.all()
    serializer_class = serializers.UserStatusDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name', 'last_name', 'birth_date', 'user_id', 'Departament_id']


# def get_queryset(self):
#    queryset = models.

class UserStatusDetail(generics.RetrieveAPIView):
    queryset = models.UserStatus.objects.all()
    serializer_class = serializers.UserStatusDetailSerializer
    permission_classes = [IsAdminUser | IsHR]


class UserStatusUpdate(generics.UpdateAPIView):
    queryset = models.UserStatus.objects.all()
    serializer_class = serializers.UserStatusDetailSerializer
    permission_classes = [IsAdminUser | IsHR]


class UserStatusDelete(generics.DestroyAPIView):
    queryset = models.UserStatus.objects.all()
    serializer_class = serializers.UserStatusDetailSerializer
    permission_classes = [IsAdminUser | IsHR]

    def delete(self, request, *args, **kwargs):
        userstatus = models.UserStatus.objects.get(id=kwargs.get('pk'))
        if not userstatus.active:
            return Response({'error_message': "Could not delete"},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super(UserStatusDelete, self).delete(request=request, *args, **kwargs)
