from rest_framework.response import Response
from rest_framework.views import APIView
from adminmodule.models.user_model import User
from rest_framework import status
from adminmodule.models.employee_model import Employees
from adminmodule.versioned.v1.serializer.employee_serializer import EmployeeSerializer
from utils.helper.permission import SuperuserPermission
class EmployeeGetAPI(APIView):
    permission_classes=[SuperuserPermission]
    def get(self,request):
        """Handle GET request and return Response"""
        queryset = Employees.objects.all()
        serializer = EmployeeSerializer(queryset,many=True)
        return Response({
            "messege":"Employees fetched successfully",
            "data": serializer.data
            },
            status= status.HTTP_200_OK
        )
        
    def post(self, request):
        """Handle POST requests and post the data in employees model """
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class EmployeePutAPI(APIView):
    permission_classes=[SuperuserPermission]

    def get(self,request,id):
        """Handle GET request and return Response"""
        snippet=Employees.objects.get(id=id)
        self.check_object_permissions(request,snippet)
        serializer=EmployeeSerializer(snippet)
        return Response(serializer.data)

        
    def put(self, request, id):
        """Handle Patch requests and update data in employees model."""
        
        try:
            queryset = Employees.objects.get(pk=id)
        except:
            return Response({"error":"queryset not found"}, status= status.HTTP_400_BAD_REQUEST)
        
        serializer = EmployeeSerializer(queryset, data = request.data, partial= True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        """Handle DELETE requests and delete data from employees model."""
        
        try:
            queryset = Employees.objects.get(pk=id)
        except:
            return Response({"error":"queryset not found"}, status= status.HTTP_400_BAD_REQUEST)
        
        queryset.delete()
        return Response({"message":"Employee deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        
    
    