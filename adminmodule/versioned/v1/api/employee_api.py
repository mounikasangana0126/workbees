from rest_framework.response import Response
from rest_framework.views import APIView
from adminmodule.models.user_model import User
from rest_framework import status
from adminmodule.models.employee_model import Employees
from adminmodule.versioned.v1.serializer.employee_serializer import EmployeeSerializer
from rest_framework.permissions import IsAuthenticated
class EmployeeGetAPI(APIView):
    """Handle GET request and return Response"""
    permission_classes=[IsAuthenticated]

    def get(self,request):
        """Handle GET request and return Response"""
        snippet=Employees.objects.filter(user=request.user)
        print(request.user)
        serializer=EmployeeSerializer(snippet, many=True)
        return Response({
            "message":"Employee Details Fetched successfully",
            "data":serializer.data},
            status=status.HTTP_200_OK
        )


    def put(self, request):
        """Handle Patch requests and update data in employees model."""
        
        try:
            queryset = Employees.objects.filter(user=request.user)
        except:
            return Response({"error":"queryset not found"}, status= status.HTTP_400_BAD_REQUEST)
        
        serializer = EmployeeSerializer(queryset, data = request.data, partial= True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
  
        
    
    