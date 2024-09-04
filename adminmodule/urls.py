
from django.urls import path,include
from adminmodule.versioned.v1.api.department_api import DepartmentGetAPI


urlpatterns = [
   path('department/',DepartmentGetAPI.as_view()),
   #path("satish")
   
]