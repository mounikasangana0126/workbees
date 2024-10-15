
from django.urls import path
from adminmodule.versioned.v1.api.department_api import DepartmentGetAPI
from adminmodule.versioned.v1.api.time_entry_model_api import TimeGetAPI,patch_modelGetAPI
from adminmodule.versioned.v1.api.user_model import UserGetAPI

from adminmodule.versioned.v1.api.enable_disable import detailsGetAPI





urlpatterns = [
   path('department/',DepartmentGetAPI.as_view()),
   path('time_entry/',TimeGetAPI.as_view()),
   path('user/',UserGetAPI.as_view()),
   path('details/<int:id>/',detailsGetAPI.as_view()),
   #path('enableGetAPI/',enableGetAPI.as_view()),
   path('patch_model/<int:id>/',patch_modelGetAPI.as_view()),
   
]