
from django.urls import path,include
from adminmodule.versioned.v1.api.department_api import DepartmentGetAPI
from adminmodule.versioned.v1.api.designation_api import DesignationGetAPI
from adminmodule.versioned.v1.api.employee_api import EmployeeGetAPI
from adminmodule.versioned.v1.api.breakentry_api import BreakEntryGetAPI
from . import views

urlpatterns = [
   path('',views.home),
   path('login/',views.login_view, name="authenticate"),
   path('department/',DepartmentGetAPI.as_view()),
   path('designation/',DesignationGetAPI.as_view()),
   path('employees/',EmployeeGetAPI.as_view()),
   path('breakentry/',BreakEntryGetAPI.as_view()),
]
