
from django.urls import path,include
from adminmodule.versioned.v1.api.department_api import DepartmentGetAPI,DepartmentGetDetailAPI,ParentGetAPI
from adminmodule.versioned.v1.api.shift_timings_api import ShiftTimingGetAPI,ShiftTimingDetailGetAPI
from adminmodule.versioned.v1.api.employee_api import EmployeeGetAPI
from adminmodule.versioned.v1.api.employee_admin_api import EmployeeGetAdminAPI, EmployeeGetAdminDetailAPI
from adminmodule.versioned.v1.api.checkin_checkout_api import TimeEntryCheckInAPI, TimeEntryCheckOutAPI, TimeEntryCheckInCheckOutDetailsAPI
from adminmodule.versioned.v1.api.leave_api import  LeaveAPI,LeaveDetailAPI
from adminmodule.versioned.v1.api.leave_admin_api import LeaveAdminAPI,LeaveAdminDetailAPI
from adminmodule.versioned.v1.api.break_continue_api import BreakAPI, BreakContinueAPI,BreakContinueDetailAPI
from adminmodule.versioned.v1.api.login_api import LoginAPI, ResetPasswordAPI
from adminmodule.versioned.v1.api.designation_api import DesignationGetAPI,DesignationGetDetailAPI
from adminmodule.versioned.v1.api.task_admin import TaskAdminAPI,TaskAdminDetailsAPI
from adminmodule.versioned.v1.api.task_employee import TaskEmployeeAPI, TaskEmployeeDetailsAPI
from adminmodule.versioned.v1.api.logout_api import LogoutAPI
from adminmodule.versioned.v1.api.qrcode_api import QrCodeGeneration,QrCodeValidateAPI
from adminmodule.versioned.v1.api.leavescount_api import LeavesCountGetAPI
from adminmodule.versioned.v1.api.presentemployee_api import PresentEmployeeGetAPI, AbsentEmployeeGetAPI
from adminmodule.versioned.v1.api.recent_logins_api import RecentLoginEmployeeGetAPI, GetSingleDayLoginsTask
from adminmodule.versioned.v1.api.attendence_history_api import AttendanceHistoryGetAPI
from adminmodule.versioned.v1.api.reset_password_api import PasswordResetConfirmAPI, PasswordResetRequestAPI
from adminmodule.versioned.v1.api.qrcode_api import QrCodeGeneration, QrCodeValidateAPI

urlpatterns = [

   path('login/', LoginAPI.as_view(), name='login'),
   path('logout/',LogoutAPI.as_view(),name='logout'),
   path('reset_password/', ResetPasswordAPI.as_view()),
   path('reset_password_request/', PasswordResetRequestAPI.as_view(), name='password_reset_request'),
   path('reset_password/<str:uidb64>/<str:token>/', PasswordResetConfirmAPI.as_view(), name='password_reset_confirm'),
#  User apis
   path('employee/',EmployeeGetAPI.as_view()),
   path('checkin/',TimeEntryCheckInAPI.as_view()),
   path('checkout/', TimeEntryCheckOutAPI.as_view()),
   path('checkout/<uuid:id>/',TimeEntryCheckInCheckOutDetailsAPI.as_view()),
   path('leave_employee/',LeaveAPI.as_view()),
   path('leave_employee/<uuid:id>/',LeaveDetailAPI.as_view()),
   path('break/',BreakAPI.as_view()),
   path('break-continue/',BreakContinueAPI.as_view()),
   path('break/<uuid:id>/',BreakContinueDetailAPI.as_view()),
   path('task_employee/',TaskEmployeeAPI.as_view()),
   path('task_employee/<uuid:id>/',TaskEmployeeDetailsAPI.as_view()),
   path('qrcode_generator/',QrCodeGeneration.as_view()),
   path('qrcode_validator/',QrCodeValidateAPI.as_view()),
   path('leavecount/', LeavesCountGetAPI.as_view() ),
   path('attendencehistory/', AttendanceHistoryGetAPI.as_view()),
   path('qrcodegenerate/', QrCodeGeneration.as_view()),
   path('qrcodevalidate/', QrCodeValidateAPI.as_view()),
   
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
   path('employeepresent/<uuid:id>/',PresentEmployeeGetAPI.as_view()),
   path('employeeabsent/<uuid:id>/',AbsentEmployeeGetAPI.as_view()),
   path('recent_logins/',RecentLoginEmployeeGetAPI.as_view()),
   path('date_logins/<str:date>/', GetSingleDayLoginsTask.as_view()),
  
]