from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from adminmodule.models.employee_model import Employees
from adminmodule.versioned.v1.serializer.employee_serializer import EmployeeSerializer

class EmployeeGetAPI(APIView):
    
    def get(self,request, *args, **kwargs):
        """Handle GET request and return Response"""
        
        queryset = Employees.objects.all()
        serializer = EmployeeSerializer(queryset, many = True)
        return Response({
            "messege":"Employees fetched successfullt",
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
    
    def patch(self, request, id):
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

class ColourGetAPI(APIView):
    def get(self, request, id):
        try:
            queryset = Employees.objects.get(id=id)
        except:
            return Response({'error': 'Data was not found'}, status=status.HTTP_400_BAD_REQUEST)
        
        if queryset.emp_is_active is True:
            return Response({'color': 'Green'}, status=status.HTTP_200_OK)
        
        return Response({'color': 'Red'}, status=status.HTTP_200_OK)
        
    
    