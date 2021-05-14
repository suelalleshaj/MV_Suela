from django.urls import path
from MV.quickstart import views

urlpatterns = [
    path('employee/create/', views.EmployeeCreate.as_view(), name = 'create_employee'),
    path('employee/list/', views.EmployeeList.as_view(), name = 'list_employee'),
    path('employee/detail/<int:pk>/', views.EmployeeDetail.as_view(), name = 'detail_employee'),
    path('employee/update/<int:pk>/', views.EmployeeUpdate.as_view(), name = 'update_employee'),
    path('employee/delete/<int:pk>/', views.EmployeeDelete.as_view(), name = 'delete_employee'),
]