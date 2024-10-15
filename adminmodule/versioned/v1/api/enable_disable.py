from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from adminmodule.models.employee_model import Employees
from adminmodule.models.user_model import User
from adminmodule.versioned.v1.serializer. employee_serializer import EmployeeSerializer
from adminmodule.versioned.v1.serializer.user_serializer import UserSerializer


class detailsGetAPI(APIView):
    
    def get(self,request,id):
        try:
            queryset = Employees.objects.get(pk=id)
        except:
            return Response({"error":"Employee not found"}, status.HTTP_404_NOT_FOUND)
        
        try:
            queryset2 = User.objects.get(username = queryset.data['user'])
        except:
            return Response({"error":"Employee not found"}, status.HTTP_404_NOT_FOUND)
        
        serializer = EmployeeSerializer(queryset)
        serializer1 = UserSerializer(queryset2)
        return Response({
            'employee_id':serializer.data['employee_id'],
            'name':serializer1.data['name'],
            'designation':serializer.data['designation'],
            'username':serializer1.data['username'],
            'phone_number':serializer1.data['phone_number']
        })
