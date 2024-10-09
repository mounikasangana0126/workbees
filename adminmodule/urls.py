
from django.urls import path,include
from adminmodule.versioned.v1.api.department_api import DepartmentGetAPI
from adminmodule.versioned.v1.api.time_entry_model_api import TimeGetAPI
from adminmodule.versioned.v1.api.user_model import UserGetAPI
from adminmodule.versioned.v1.api.shift_timings_api import ShiftTimingGetAPI,ShiftTimingDetailGetAPI
from adminmodule.versioned.v1.api.details_api import DetailsGetAPI
from adminmodule.versioned.v1.api.anable_disable_api import enable_or_disable
from adminmodule.versioned.v1.api.employee_api import EmployeeGetAPI, ColourGetAPI

urlpatterns = [
   path('shift_time/',ShiftTimingGetAPI.as_view()),
   path('shift_time/<int:id>/',ShiftTimingDetailGetAPI.as_view()),
   path('department/',DepartmentGetAPI.as_view()),
   path('time_entry/',TimeGetAPI.as_view()),
   path('user/',UserGetAPI.as_view()),
   path('colour/<int:id>/',ColourGetAPI.as_view()),
   path('details/<int:id>/',DetailsGetAPI.as_view()),
   path('enable/<str:auto_clockout>/',enable_or_disable.as_view()),
   path('employee/',EmployeeGetAPI.as_view()),
]