
from django.urls import path,include
from adminmodule.versioned.v1.api.department_api import DepartmentGetAPI,DepartmentGetDetailAPI,ParentGetAPI
from adminmodule.versioned.v1.api.shift_timings_api import ShiftTimingGetAPI,ShiftTimingDetailGetAPI
from adminmodule.versioned.v1.api.employee_api import EmployeeGetAPI
from adminmodule.versioned.v1.api.employee_admin_api import EmployeeGetAdminAPI, EmployeeGetAdminDetailAPI
from adminmodule.versioned.v1.api.checkin_checkout_api import TimeEntryCheckInAPI, TimeEntryCheckOutAPI, TimeEntryCheckInCheckOutDetailsAPI
from adminmodule.versioned.v1.api.leave_api import  LeaveAPI,LeaveDetailAPI
from adminmodule.versioned.v1.api.leave_admin_api import LeaveAdminAPI,LeaveAdminDetailAPI
from adminmodule.versioned.v1.api.break_continue_api import BreakAPI, BreakContinueAPI,BreakContinueDetailAPI
from adminmodule.versioned.v1.api.login_api import LoginAPI
from adminmodule.versioned.v1.api.designation_api import DesignationGetAPI,DesignationGetDetailAPI
from adminmodule.versioned.v1.api.task_admin import TaskAdminAPI,TaskAdminDetailsAPI
from adminmodule.versioned.v1.api.task_employee import TaskEmployeeAPI

urlpatterns = [

   path('login/', LoginAPI.as_view(), name='login'),

#  User apis
   path('employee/',EmployeeGetAPI.as_view()),
   path('checkin/',TimeEntryCheckInAPI.as_view()),
   path('checkout/', TimeEntryCheckOutAPI.as_view()),
   path('checkout/<uuid:id>/',TimeEntryCheckInCheckOutDetailsAPI.as_view()),
   path('leave/',LeaveAPI.as_view()),
   path('leave/<uuid:id>/',LeaveDetailAPI.as_view()),
   path('break/',BreakAPI.as_view()),
   path('break-continue/',BreakContinueAPI.as_view()),
   path('break/<uuid:id>/',BreakContinueDetailAPI.as_view()),
   path('task_employee/',TaskEmployeeAPI.as_view()),
   path('task_employee/<uuid:id>/',TaskEmployeeAPI.as_view()),
   
#  Admin apis
   path('shift_time/',ShiftTimingGetAPI.as_view()),
   path('shift_time/<uuid:id>/',ShiftTimingDetailGetAPI.as_view()),
   path('parent/',ParentGetAPI.as_view()),
   path('department/',DepartmentGetAPI.as_view()),
   path('department/<uuid:id>/',DepartmentGetDetailAPI.as_view()),
   path('designation/',DesignationGetAPI.as_view()),
   path('designation/<uuid:id>/',DesignationGetDetailAPI.as_view()),
   path('employee_admin/',EmployeeGetAdminAPI.as_view()),
   path('employee_admin/<uuid:id>/',EmployeeGetAdminDetailAPI.as_view()),
   path('leave_admin/',LeaveAdminAPI.as_view()),
   path('leave_admin/<uuid:id>/',LeaveAdminDetailAPI.as_view()),
   path('task_admin/',TaskAdminAPI.as_view()),
   path('task_admin/<uuid:id>/',TaskAdminDetailsAPI.as_view()),
  
]