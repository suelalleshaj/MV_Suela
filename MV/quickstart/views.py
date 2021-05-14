from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from self import self

from MV.quickstart.permissions import IsHR, IsDepartamentManager, IsEmployee
from MV.quickstart import models, serializers, serializers


class EmployeeCreate(generics.CreateAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    permission_classes = [IsAdminUser | IsHR]

    def post(self, request, *args, **kwargs):
        _mutable = request.data._mutable
        request.data._mutable = True
        request.data['create_id'] = request.user.id
        request.data._mutable = _mutable

        return EmployeeCreate.create(self, request, *args, **kwargs)


class EmployeeList(generics.ListAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name', 'last_name', 'birth_date', 'user_id', 'departament_id']

   # def get_queryset(self):
    #    queryset = models.

class EmployeeDetail(generics.DetailAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    permission_classes = [IsAdminUser | IsHR]

class EmployeeUpdate(generics.UptadeAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    permission_classes = [IsAdminUser | IsHR]

class EmployeeDelete(generics.DestroyAPIView):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    permission_classes = [IsAdminUser | IsHR]

    def delte(selfself, request, *args, **kwargs):
        employee = models.Employee.objects.get(id=kwargs.get('pk'))
        if not employee.active:
            return Response({'error_message':"Could not delete"},
            status = status.HTTP_405_METHOD_NOT_ALLOWED)
        return super(EmployeeDelete, self).delete(request = request, *args, **kwargs)