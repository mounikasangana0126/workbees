from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from adminmodule.models.leave_model import Leave 
from adminmodule.versioned.v1.serializer.leave_serializer import LeaveSerializer 
from adminmodule.models.employee_model import Employees 
from rest_framework.permissions import IsAuthenticated  
from utils.helper.permission import SuperuserPermission  

class LeaveAdminAPI(APIView):
    """Leave Admin API"""
    permission_classes = [SuperuserPermission]  
    def get(self, request):
        """ Handle get request to fetch all leave records of an employee."""
        query = Leave.objects.filter(status = "PENDING")  
        if not query.exists():  
            return Response({
                'message': 'No leave records found',
                'data': [],
                'status': status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = LeaveSerializer(query, many=True)  
        return Response({
            'message': 'Leave records retrieved successfully',
            'data': serializer.data,
            'status': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        """ Handle post request to add leave record of an employee."""
        try:
            employee_id = Employees.objects.filter(employee__user=request.user).first()
            if not employee_id:
                raise Exception("Employee not found")
        except Exception as e:
            return Response({
                'message': str(e),
                'data': None,
                'status': status.HTTP_400_BAD_REQUEST
            }, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = LeaveSerializer(data=request.data) 
        if serializer.is_valid():  
            serializer.save(employee=employee_id)  
            return Response({
                'message': 'Leave record created successfully',
                'data': serializer.data,
                'status': status.HTTP_201_CREATED
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            'message': 'Invalid data provided',
            'data': serializer.errors,
            'status': status.HTTP_400_BAD_REQUEST
        }, status=status.HTTP_400_BAD_REQUEST)


class LeaveAdminDetailAPI(APIView):
    """Leave Admin Detail API"""
    permission_classes = [SuperuserPermission] 

    def get(self, request, id):
        """ Handle get request to get a particular leave record of an employee."""
        try:
            snippet = Leave.objects.get(id=id) 
        except Leave.DoesNotExist:
            return Response({
                'message': 'Leave record not found',
                'data': None,
                'status': status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = LeaveSerializer(snippet)  
        return Response({
            'message': 'Leave record retrieved successfully',
            'data': serializer.data,
            'status': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)

    def put(self, request, id):
        """ Handle put request to update a particular leave record of an employee."""
        try:
            snippet = Leave.objects.get(id=id)  
        except Leave.DoesNotExist:
            return Response({
                'message': 'Leave record not found',
                'data': None,
                'status': status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = LeaveSerializer(snippet, data=request.data)
        if serializer.is_valid():  
            serializer.save()  
            return Response({
                'message': 'Leave record updated successfully',
                'data': serializer.data,
                'status': status.HTTP_200_OK
            }, status=status.HTTP_200_OK)
        
        return Response({
            'message': 'Invalid data provided',
            'data': serializer.errors,
            'status': status.HTTP_400_BAD_REQUEST
        }, status=status.HTTP_400_BAD_REQUEST)
