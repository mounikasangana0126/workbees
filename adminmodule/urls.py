
from django.urls import path,include
from adminmodule.api.department_api import DepartmentGetAPI


urlpatterns = [
   path('department/',DepartmentGetAPI.as_view()),
]