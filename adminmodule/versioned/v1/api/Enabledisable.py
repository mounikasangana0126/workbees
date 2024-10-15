from rest_framework.views import APIView
from rest_framework.response import Response
from adminmodule.models.employee_model import Employees 
from adminmodule.versioned.v1.serializer.employee_serializer import EmployeeSerializer
from rest_framework import status



class Enable_disableGetAPI(APIView):
    def get(self,*args,**kwargs):
        try:
            queryset=Employees.objects.get(auto_clockout="Active")
            
        




   