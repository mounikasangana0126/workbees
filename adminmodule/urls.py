
from django.urls import path,include
from adminmodule.versioned.v1.api.department_api import DepartmentGetAPI,DepartmentGetDetailAPI,ParentGetAPI
from adminmodule.versioned.v1.api.designation_api import DesignationGetAPI
from adminmodule.versioned.v1.api.time_entry_model_api import TimeGetAPI
from adminmodule.versioned.v1.api.user_model import UserGetAPI


urlpatterns = [
   path('department/',DepartmentGetAPI.as_view()),
   path('parent/',ParentGetAPI.as_view()),
   path('department/<int:id>/',DepartmentGetDetailAPI.as_view()),
   path('designation/',DesignationGetAPI.as_view()),
   path('time_entry/',TimeGetAPI.as_view()),
   path('user/',UserGetAPI.as_view()),
]