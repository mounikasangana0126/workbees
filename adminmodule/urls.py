
from django.urls import path,include
from adminmodule.versioned.v1.api.department_api import DepartmentGetAPI,DepartmentGetDetailAPI,ParentGetAPI
from adminmodule.versioned.v1.api.designation_api import DesignationGetAPI
from adminmodule.versioned.v1.api.time_entry_model_api import TimeGetAPI
from adminmodule.versioned.v1.api.user_model import UserGetAPI
from adminmodule.versioned.v1.api.shift_timings_api import ShiftTimingGetAPI,ShiftTimingDetailGetAPI
from adminmodule.versioned.v1.api.details_api import DetailsGetAPI
from adminmodule.versioned.v1.api.employee_api import EmployeeGetAPI, ColourGetAPI
from adminmodule.versioned.v1.api.checkin_checkout_api import CheckInCheckOutAPI, CheckInCheckOutDetailsAPI
from adminmodule.versioned.v1.api.leave_api import  LeaveAPI
from adminmodule.versioned.v1.api.break_continue_api import BreakContinueAPI

urlpatterns = [
   path('break/',BreakContinueAPI.as_view()),
   path('leave/',LeaveAPI.as_view()),
   path('user_details/<int:user>/',CheckInCheckOutDetailsAPI.as_view()),
   path('user_details/<str:date>/',CheckInCheckOutDetailsAPI.as_view()),
   path('inout/',CheckInCheckOutAPI.as_view()),
   path('shift_time/',ShiftTimingGetAPI.as_view()),
   path('shift_time/<int:id>/',ShiftTimingDetailGetAPI.as_view()),
   path('department/',DepartmentGetAPI.as_view()),
   path('parent/',ParentGetAPI.as_view()),
   path('department/<int:id>/',DepartmentGetDetailAPI.as_view()),
   path('designation/',DesignationGetAPI.as_view()),
   path('time_entry/',TimeGetAPI.as_view()),
   path('user/',UserGetAPI.as_view()),
   path('colour/<int:id>/',ColourGetAPI.as_view()),
   path('details/<int:id>/',DetailsGetAPI.as_view()),
   path('employee/',EmployeeGetAPI.as_view()),
   path('employee/<int:id>/',EmployeeGetAPI.as_view()),
]