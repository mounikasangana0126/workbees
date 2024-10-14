
from django.urls import path,include
from adminmodule.versioned.v1.api.department_api import DepartmentGetAPI,DepartmentGetDetailAPI,ParentGetAPI
from adminmodule.versioned.v1.api.user_model import UserGetAPI,UserPutAPI
from adminmodule.versioned.v1.api.shift_timings_api import ShiftTimingGetAPI,ShiftTimingDetailGetAPI
from adminmodule.versioned.v1.api.employee_api import EmployeeGetAPI,EmployeePutAPI
from adminmodule.versioned.v1.api.checkin_checkout_api import CheckInCheckOutAPI, CheckInCheckOutDetailsAPI
from adminmodule.versioned.v1.api.leave_api import  LeaveAPI
from adminmodule.versioned.v1.api.break_continue_api import BreakContinueAPI

urlpatterns = [
   path('employee_details/<str:id>/',EmployeePutAPI.as_view()),
   path('employee/',EmployeeGetAPI.as_view()),
   path('user_details/<str:id>/',UserPutAPI.as_view()),
   path('users/',UserGetAPI.as_view()),
   path('inout/',CheckInCheckOutAPI.as_view()),
   path('inout_details/<str:id>/',CheckInCheckOutDetailsAPI.as_view()),
   path('inout_details/<str:id>/<str:date>/',CheckInCheckOutDetailsAPI.as_view()),
   






   path('break/',BreakContinueAPI.as_view()),
   path('leave/',LeaveAPI.as_view()),
   
   path('user_details/<str:date>/',CheckInCheckOutDetailsAPI.as_view()),
   
   path('shift_time/',ShiftTimingGetAPI.as_view()),
   path('shift_time/<int:id>/',ShiftTimingDetailGetAPI.as_view()),
   path('department/',DepartmentGetAPI.as_view()),
   path('parent/',ParentGetAPI.as_view()),
   path('department/<int:id>/',DepartmentGetDetailAPI.as_view()),

  
]