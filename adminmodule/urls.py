
from django.urls import path,include
from adminmodule.versioned.v1.api.department_api import DepartmentGetAPI
from adminmodule.versioned.v1.api.time_entry_model_api import TimeGetAPI
from adminmodule.versioned.v1.api.user_model_api import UserGetAPI
from . import views 

urlpatterns = [
   path('authentiation/',views.home),
   path('department/',DepartmentGetAPI.as_view()),
   path('time_entry/',TimeGetAPI.as_view()),
   path('user/',UserGetAPI.as_view()),
]