
from django.urls import path,include
from adminmodule.versioned.v1.api.department_api import DepartmentGetAPI
from adminmodule.versioned.v1.api.shift_timings_api import ShiftTimingGetAPI
from adminmodule.versioned.v1.api.task_model_api import TaskModelGetAPI
from . import views


urlpatterns = [
   path('',views.index),
   path('department/',DepartmentGetAPI.as_view()),
   path('shift_timing/',ShiftTimingGetAPI.as_view()),
   path('task_model/',TaskModelGetAPI.as_view()),
]
