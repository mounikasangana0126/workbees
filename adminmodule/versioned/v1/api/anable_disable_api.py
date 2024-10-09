from adminmodule.models.employee_model import Employees
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from adminmodule.versioned.v1.serializer.employee_serializer import EmployeeSerializer
class enable_or_disable(APIView):
    def get(self,request,auto_clockout):
        try:
            queryset=Employees.objects.filter(auto_clockout=auto_clockout)
        except:
            return Response({'error':'data does not foud'},status=status.HTTP_400_BAD_REQUEST)
        serializer=EmployeeSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    