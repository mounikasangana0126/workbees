"""Leave admin api."""

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from adminmodule.models.leave_model import Leave 
from adminmodule.versioned.v1.serializer.leave_serializer import PostLeaveSerializer ,GetLeaveSerializer
from adminmodule.models.employee_model import Employees 
from rest_framework.permissions import IsAuthenticated  
from utils.helper.permission import SuperuserPermission  

class LeaveAdminAPI(APIView):
    """Leave Admin API"""
    permission_classes = [SuperuserPermission]  

    def get(self, request):
        """ Handle get request to fetch all leave records of an employee."""
        leave_status=request.GET.get("status",None)
        query = Leave.objects.all()  
        if leave_status:
            query = Leave.objects.filter(status = leave_status)  
        serializer = GetLeaveSerializer(query, many=True)  
        return Response(
            {
                'message': 'Leave records retrieved successfully',
                'data': serializer.data,
            }, 
            status=status.HTTP_200_OK
        )
    
    def post(self, request, *args, **kwargs):
        """ Handle post request to add leave record of an employee."""

        try:
            data=request.data.get('employee')
            employee= Employees.objects.get(employee_id=data["employee_id"])
            if not employee:
                raise Exception("Employee not found")
        except Exception as e:
            return Response(
                {
                    'message': str(e),
                    'data': [],
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = PostLeaveSerializer(data=request.data) 
        if serializer.is_valid():  
            serializer.save(employee=employee,status="Approved")  
            return Response(
                {
                    'message': 'Leave record created successfully',
                    'data': serializer.data,
                }, 
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            {
                'message': 'Invalid data provided',
                'data': serializer.errors,
            }, 
            status=status.HTTP_400_BAD_REQUEST
        )


class LeaveAdminDetailAPI(APIView):
    """Leave Admin Detail API"""

    permission_classes = [SuperuserPermission] 

    def get(self, request, id):
        """ Handle get request to get a particular leave record of an employee."""

        try:
            snippet = Leave.objects.get(id=id) 
        except Leave.DoesNotExist:
            return Response(
                {
                    'message': 'Leave record not found',
                    'data': None
                }, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = GetLeaveSerializer(snippet)  
        return Response(
            {
                'message': 'Leave record retrieved successfully',
                'data': serializer.data,
            }, 
            status=status.HTTP_200_OK
        )

    def put(self, request, id):
        """ Handle put request to update a particular leave record of an employee."""
        
        try:
            snippet = Leave.objects.get(id=id)  
        except Leave.DoesNotExist:
            return Response(
                {
                    'message': 'Leave record not found',
                    'data': None,
                }, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = GetLeaveSerializer(snippet, data=request.data,partial=True)
        if serializer.is_valid():  
            serializer.save(status="APPROVED")  
            return Response(
                {
                    'message': 'Leave record updated successfully',
                    'data': serializer.data,
                }, 
                status=status.HTTP_200_OK
            )
        
        return Response(
            {
                'message': 'Invalid data provided',
                'data': serializer.errors,
            }, 
            status=status.HTTP_400_BAD_REQUEST
        )
