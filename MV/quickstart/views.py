#from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser #IsAuthenticated
from rest_framework.response import Response
from self import self

from MV.quickstart.permissions import IsHR
from MV.quickstart import models, serializers


class EmployeeCreate(generics.CreateAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeDetailSerializer
    permission_classes = [IsAdminUser | IsHR]

    def post(self, request, *args, **kwargs):
        _mutable = request.data._mutable
        request.data._mutable = True
        request.data['create_id'] = request.user.id
        request.data._mutable = _mutable

        return EmployeeCreate.create(self, request, *args, **kwargs)


class EmployeeList(generics.ListAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name', 'last_name', 'birth_date', 'user_id', 'departament_id']

   # def get_queryset(self):
    #    queryset = models.

class EmployeeDetail(generics.DetailAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeDetailSerializer
    permission_classes = [IsAdminUser | IsHR]

class EmployeeUpdate(generics.UpdateAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeDetailSerializer
    permission_classes = [IsAdminUser | IsHR]

class EmployeeDelete(generics.DestroyAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeDetailSerializer
    permission_classes = [IsAdminUser | IsHR]

    def delete(selfself, request, *args, **kwargs):
        employee = models.Employee.objects.get(id=kwargs.get('pk'))
        if not employee.active:
            return Response({'error_message':"Could not delete"},
            status = status.HTTP_405_METHOD_NOT_ALLOWED)
        return super(EmployeeDelete, self).delete(request = request, *args, **kwargs)

class UserCreate(generics.CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserDetailSerializer
    permission_classes = [IsAdminUser | IsHR]

    def post(self, request, *args, **kwargs):
        _mutable = request.data._mutable
        request.data._mutable = True
        request.data['create_id'] = request.user.id
        request.data._mutable = _mutable

        return EmployeeCreate.create(self, request, *args, **kwargs)


class UserList(generics.ListAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name', 'last_name', 'birth_date', 'user_id', 'departament_id']

   # def get_queryset(self):
    #    queryset = models.

class UserDetail(generics.DetailAPIView):
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

    def delete(selfself, request, *args, **kwargs):
        user = models.User.objects.get(id=kwargs.get('pk'))
        if not user.active:
            return Response({'error_message':"Could not delete"},
            status = status.HTTP_405_METHOD_NOT_ALLOWED)
        return super(UserDelete, self).delete(request = request, *args, **kwargs)


class DepartamentCreate(generics.CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.DepartamentDetailSerializer

    def post(self, *args, **kwargs):
        return DepartamentCreate.create(self, *args, **kwargs)


class DepartamentDetail(generics.DetailAPIView):
    queryset = models.Departament.objects.all()
    serializer_class = serializers.DepartamentDetailSerializer

class DepartamentUpdate(generics.UpdateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.DepartamentDetailSerializer

class DepartamentDelete(generics.DestroyAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.DepartamentDetailSerializer

    def delete(selfself, request, *args, **kwargs):
        departament = models.Departament.objects.get(id=kwargs.get('pk'))
        if not departament.active:
            return Response({'error_message':"Could not delete"},
            status = status.HTTP_405_METHOD_NOT_ALLOWED)
        return super(DepartamentDelete, self).delete(request = request, *args, **kwargs)

class HolidaysCreate(generics.CreateAPIView):
        queryset = models.Holidays.objects.all()
        serializer_class = serializers.HolidaysDetailSerializer

        def post(self, HolidaysCreate=None, *args, **kwargs):
            return HolidaysCreate.create(self, *args, **kwargs)

class HolidaysList(generics.DetailAPIView):
        queryset = models.Holidays.objects.all()
        serializer_class = serializers.HolidaysDetailSerializer

class HolidaysDetail(generics.DetailAPIView):
    queryset = models.Holidays.objects.all()
    serializer_class = serializers.HolidaysDetailSerializer

class HolidaysUpdate(generics.UpdateAPIView):
        queryset = models.User.objects.all()
        serializer_class = serializers.HolidaysDetailSerializer

class HolidaysDelete(generics.DestroyAPIView):
        queryset = models.Holidays.objects.all()
        serializer_class = serializers.HolidaysDetailSerializer

        def delete(selfself, request, HolidaysDelete=None, *args, **kwargs):
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


class PermitList(generics.DetailAPIView):
    queryset = models.Permit.objects.all()
    serializer_class = serializers.PermitDetailSerializer


class PermitDetail(generics.DetailAPIView):
    queryset = models.Permit.objects.all()
    serializer_class = serializers.PermitDetailSerializer


class PermitUpdate(generics.UpdateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.PermitDetailSerializer


class PermitDelete(generics.DestroyAPIView):
    queryset = models.Permit.objects.all()
    serializer_class = serializers.PermitDetailSerializer

    def delete(selfself, request, PermitDelete=None, *args, **kwargs):
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


class StatusDetail(generics.DetailAPIView):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusDetailSerializer


class StatusDelete(generics.DestroyAPIView):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusDetailSerializer

    def delete(selfself, request, StatusDelete=None, *args, **kwargs):
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
    filter_fields = ['name', 'last_name', 'birth_date', 'user_id', 'departament_id']

   # def get_queryset(self):
    #    queryset = models.

class UserStatusDetail(generics.DetailAPIView):
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

    def delete(selfself, request, *args, **kwargs):
        userstatus = models.UserStatus.objects.get(id=kwargs.get('pk'))
        if not userstatus.active:
            return Response({'error_message':"Could not delete"},
            status = status.HTTP_405_METHOD_NOT_ALLOWED)
        return super(UserStatusDelete, self).delete(request = request, *args, **kwargs)