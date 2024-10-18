from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from adminmodule.models.leave_model import Leave  # Import the Leave model
from adminmodule.versioned.v1.serializer.leave_serializer import LeaveSerializer  # Import LeaveSerializer
from adminmodule.models.employee_model import Employees  # Import Employees model
from rest_framework.permissions import IsAuthenticated  # Import permission for authenticated access
from utils.helper.permission import SuperuserPermission  # Custom permission for superusers

# API to handle leave-related operations for admins
class LeaveAdminAPI(APIView):
    permission_classes = [SuperuserPermission]  # Restrict access to superusers only
    
    # GET method to retrieve all leave records
    def get(self, request):
        query = Leave.objects.filter(status = "PENDING")  # Retrieve all leave entries
        if not query.exists():  # Check if no leave records exist
            return Response({
                'message': 'No leave records found',
                'data': [],
                'status': status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = LeaveSerializer(query, many=True)  # Serialize multiple leave records
        return Response({
            'message': 'Leave records retrieved successfully',
            'data': serializer.data,
            'status': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)
    
    # POST method to create a new leave record
    def post(self, request, *args, **kwargs):
        try:
            # Find the employee record linked to the current logged-in user
            employee_id = Employees.objects.filter(employee__user=request.user).first()
            if not employee_id:
                raise Exception("Employee not found")
        except Exception as e:
            return Response({
                'message': str(e),
                'data': None,
                'status': status.HTTP_400_BAD_REQUEST
            }, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = LeaveSerializer(data=request.data)  # Initialize serializer with request data
        if serializer.is_valid():  # Check if data is valid
            serializer.save(employee=employee_id)  # Save the leave record linked to the employee
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

# API to handle operations on individual leave records (view, update)
class LeaveAdminDetailAPI(APIView):
    permission_classes = [SuperuserPermission]  # Restrict access to superusers only

    # GET method to retrieve a specific leave record by its ID
    def get(self, request, id):
        try:
            snippet = Leave.objects.get(id=id)  # Find the leave record by ID
        except Leave.DoesNotExist:
            return Response({
                'message': 'Leave record not found',
                'data': None,
                'status': status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = LeaveSerializer(snippet)  # Serialize the retrieved leave record
        return Response({
            'message': 'Leave record retrieved successfully',
            'data': serializer.data,
            'status': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)

    # PUT method to update a specific leave record
    def put(self, request, id):
        try:
            snippet = Leave.objects.get(id=id)  # Find the leave record by ID
        except Leave.DoesNotExist:
            return Response({
                'message': 'Leave record not found',
                'data': None,
                'status': status.HTTP_404_NOT_FOUND
            }, status=status.HTTP_404_NOT_FOUND)
        
        # Update the leave record with new data from the request
        serializer = LeaveSerializer(snippet, data=request.data)
        if serializer.is_valid():  # Check if updated data is valid
            serializer.save()  # Save the updated leave record
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
