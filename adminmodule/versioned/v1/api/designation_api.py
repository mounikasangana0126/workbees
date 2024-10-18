from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from adminmodule.models.designation_model import DesignationModel  # Import Designation model
from adminmodule.versioned.v1.serializer.designation_serializer import DesignationSerializer  # Import Designation serializer
from utils.helper.permission import SuperuserPermission  # Import custom permission for superusers

# API to handle operations on Designation records for admins
class DesignationGetAPI(APIView):
    """Designation Get API View to fetch and create designations."""
    
    permission_classes = [SuperuserPermission]  # Restrict access to superusers only
    
    def get(self, request, *args, **kwargs):
        """Handle GET request and return Response with all designations."""
        queryset = DesignationModel.objects.all()  # Fetch all designation records
        serializer = DesignationSerializer(queryset, many=True)  # Serialize multiple records
        
        # Return response with message, serialized data (replace None with []), and status code
        return Response(
            {
                'message': 'Designations fetched successfully',
                'data': serializer.data if serializer.data else []
            },
            status=status.HTTP_200_OK
        )
        
    def post(self, request):
        """Handle POST requests and save the data in Designation model."""
        serializer = DesignationSerializer(data=request.data)  # Initialize serializer with request data
        
        if serializer.is_valid():  # Check if data is valid
            serializer.save()  # Save the new designation record
            # Return success response with message, data, and status code
            return Response({
                'message': 'Designation created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        
        # Return error response with message and status code for invalid data
        return Response({
            'message': 'Invalid data provided',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

# API to handle operations on individual Designation records (view, update, delete)
class DesignationGetDetailAPI(APIView):
    """Designation Detail API View to handle individual designation records."""
    
    permission_classes = [SuperuserPermission]  # Restrict access to superusers only
    
    def get(self, request, id):
        """Retrieve a specific designation by ID."""
        try:
            designation = DesignationModel.objects.get(id=id)  # Fetch the designation record by ID
            serializer = DesignationSerializer(designation)  # Serialize the designation record
            
            # Return success response with message, data (replace None with []), and status code
            return Response({
                'message': 'Designation fetched successfully',
                'data': serializer.data if serializer.data else []
            }, status=status.HTTP_200_OK)
        
        except DesignationModel.DoesNotExist:
            # Handle case where designation is not found, return error with empty data
            return Response({
                "message": "Designation not found",
                "data": []
            }, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        """Handle PATCH requests and update the data in Designation model."""
        try:
            queryset = DesignationModel.objects.get(id=id)  # Fetch the designation record by ID
        except DesignationModel.DoesNotExist:
            # Return error response with empty data if record is not found
            return Response({
                "message": "Designation not found",
                "data": []
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Partially update the designation record with new data
        serializer = DesignationSerializer(queryset, data=request.data, partial=True)
        
        if serializer.is_valid():  # Check if updated data is valid
            serializer.save()  # Save the updated designation record
            # Return success response with message, data, and status code
            return Response({
                'message': 'Designation updated successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        
        # Return error response with message and status code for invalid data
        return Response({
            'message': 'Invalid data provided',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        """Handle DELETE requests and delete data from Designation model."""
        try:
            queryset = DesignationModel.objects.get(id=id)  # Fetch the designation record by ID
        except DesignationModel.DoesNotExist:
            # Return error response with empty data if record is not found
            return Response({
                "message": "Designation not found",
                "data": []
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Delete the designation record
        queryset.delete()
        # Return success response with message and empty data
        return Response({
            'message': 'Designation deleted successfully',
            'data': []
        }, status=status.HTTP_204_NO_CONTENT)
