from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from adminmodule.versioned.v1.serializer.employee_user_serializer import EmployeeSeializer1
from adminmodule.models.employee_model import Employees
from adminmodule.models.user_model import User
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
class DetailsGetAPI(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,id,):
        try:
            queryset=Employees.objects.get(id=id)
        except:
            return Response({'error':'data not found'},status=status.HTTP_400_BAD_REQUEST)
        serializer=EmployeeSeializer1(queryset)
        return Response(serializer.data,status=status.HTTP_200_OK)