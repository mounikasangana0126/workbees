from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from adminmodule.models.leave_model import Leave
from adminmodule.versioned.v1.serializer.leave_serializer import LeaveSerializer, Employee
from adminmodule.models.employee_model import Employees
from rest_framework.permissions import IsAuthenticated
class LeaveAPI(APIView):
    """Leave API"""
    permission_classes=[IsAuthenticated]
    def get(self,request):
        """ Handle get request to fetch all leave records of an employee.."""
        query=Employees.objects.filter(user__name=request.user)
        serializer=Employee(query,many=True)
        return Response({
            'message':'Leave records of an employee fetched successfully',
            'data':serializer.data
        }, status= status.HTTP_200_OK)
        
    def post(self,request,*args,**kwargs):
        """ Handle post request to add leave record of an employee.."""
        serializer=LeaveSerializer(data=request.data)
        employee = Employees.objects.get(user__name = request.user)
        if serializer.is_valid():
            serializer.save(employee = employee)
            return Response({
                'message':'leave request sent successfully',
                'data':serializer.data
                }, status=status.HTTP_201_CREATED)
        return Response({
            'message':serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

class LeaveDetailAPI(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,id):
        """ Handle get request to get a particular leave record of an employee"""
        try:
            snippet=Leave.objects.get(id=id)
        except:
            return Response({'message':'Leave not found'},status=status.HTTP_400_BAD_REQUEST)
        serializer=LeaveSerializer(snippet)
        return Response({
            'message':'leave record fetched successfully',
            'data':serializer.data
        }, status=status.HTTP_200_OK)

