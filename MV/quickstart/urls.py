from django.urls import path
from quickstart import views

urlpatterns = [

    path('employee/create/', views.EmployeeCreate.as_view(), name='create_employee'),
    path('employee/list/', views.EmployeeList.as_view(), name='list_employee'),
    path('employee/detail/<int:pk>/', views.EmployeeDetail.as_view(), name='detail_employee'),
    path('employee/update/<int:pk>/', views.EmployeeUpdate.as_view(), name='update_employee'),
    path('employee/delete/<int:pk>/', views.EmployeeDelete.as_view(), name='delete_employee'),

    path('user/create/', views.UserCreate.as_view(), name='create_user'),
    path('user/list/', views.UserList.as_view(), name='list_user'),
    path('user/detail/<int:pk>/', views.UserDetail.as_view(), name='detail_user'),
    path('user/update/<int:pk>/', views.UserUpdate.as_view(), name='update_user'),
    path('user/delete/<int:pk>/', views.UserDelete.as_view(), name='delete_user'),

    path('departament/create/', views.DepartamentCreate.as_view(), name='create_departament'),
    path('departament/detail/<int:pk>/', views.DepartamentDetail.as_view(), name='detail_departament'),
    path('departament/update/<int:pk>/', views.DepartamentUpdate.as_view(), name='update_departament'),
    path('departament/delete/<int:pk>/', views.DepartamentDelete.as_view(), name='delete_departament'),

    path('holidays/create/', views.HolidaysCreate.as_view(), name='create_holidays'),
    path('holidays/list/', views.HolidaysList.as_view(), name='list_holidays'),
    path('holidays/detail/<int:pk>/', views.HolidaysDetail.as_view(), name='detail_holidays'),
    path('holidays/update/<int:pk>/', views.HolidaysUpdate.as_view(), name='update_holidays'),
    path('holidays/delete/<int:pk>/', views.HolidaysDelete.as_view(), name='delete_holidays'),

    path('permit/create/', views.PermitCreate.as_view(), name='create_permit'),
    path('permit/list/', views.PermitList.as_view(), name='list_permit'),
    path('permit/detail/<int:pk>/', views.PermitDetail.as_view(), name='detail_permit'),
    path('permit/update/<int:pk>/', views.PermitUpdate.as_view(), name='update_permit'),
    path('permit/delete/<int:pk>/', views.PermitDelete.as_view(), name='delete_permit'),
    path('permit/approved/<int:pk>/', views.PermitApproved.as_view(), name='approved_permit'),

    path('status/create/', views.StatusCreate.as_view(), name='create_statust'),
    path('status/detail/<int:pk>/', views.StatusDetail.as_view(), name='detail_status'),
    path('status/delete/<int:pk>/', views.StatusDelete.as_view(), name='delete_status'),

    path('userstatus/create/', views.UserStatusCreate.as_view(), name='create_userstatus'),
    path('userstatus/list/', views.UserStatusList.as_view(), name='list_userstatus'),
    path('userstatus/detail/<int:pk>/', views.UserStatusDetail.as_view(), name='detail_userstatus'),
    path('userstatus/update/<int:pk>/', views.UserStatusUpdate.as_view(), name='update_userstatus'),
    path('userstatus/delete/<int:pk>/', views.UserStatusDelete.as_view(), name='delete_userstatus'),

]
